from flask import request, current_app, jsonify
import sqlalchemy
from app.exceptions.user_admin_exceptions import DataContentError
from app.models.users_model import UserModel


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
    
def create_user_analyst():
    data = request.get_json()
    try:

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