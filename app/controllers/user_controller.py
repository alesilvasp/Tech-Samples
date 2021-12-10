from flask import request, current_app, jsonify
import sqlalchemy
from app.exceptions.user_exceptions import DataContentError
from app.models.users_model import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity

def create_user_admin():
    data = request.get_json()
    try:

        UserModel.check_data(data)

        password_to_hash = data.pop("password")
        new_admin = UserModel(**data)
        new_admin.password = password_to_hash
        
        current_app.db.session.add(new_admin)
        current_app.db.session.commit()
        
        return jsonify(new_admin), 201

    except DataContentError as error:
        return error.message
    except sqlalchemy.exc.IntegrityError as error:
        return {"Error": "email already registred"}, 409

@jwt_required()
def create_user_analyst():
    user = get_jwt_identity()
    
    data = request.get_json()
    try:
        
        if not user['is_admin']:
            raise PermissionError
        
        UserModel.check_data(data)

        password_to_hash = data.pop("password")
        new_analyst = UserModel(**data)
        new_analyst.password = password_to_hash
        
        current_app.db.session.add(new_analyst)
        current_app.db.session.commit()
        
        return jsonify(new_analyst), 201

    except DataContentError as error:
        return error.message
    except sqlalchemy.exc.IntegrityError as error:
        return {"Error": "email already registred"}, 409
    except PermissionError as error:
        return {"Error": 'User not allowed'}, 403