from flask import request, current_app, jsonify
from app.models.types_model import TypeModel
from app.exceptions.types_exceptions import InvalidInputDataError, InvalidTypeInputDataError, TypeNotFoundError, InvalidUpdateDataError
import sqlalchemy
import psycopg2
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def create_type():
    logged_user = get_jwt_identity()
    data = request.json
    try:
        if logged_user['is_admin']:
            raise PermissionError
        TypeModel.check_data(**data)
        new_type = TypeModel(**data)
        current_app.db.session.add(new_type)
        current_app.db.session.commit()
        return jsonify(new_type), 201
    except (InvalidInputDataError, InvalidTypeInputDataError) as err:
        return err.message
    except sqlalchemy.exc.IntegrityError as err:
        if type(err.orig) == psycopg2.errors.ForeignKeyViolation:
            return {'error': str(err.orig).split('\n')[1]}, 422
    except PermissionError as err:
        return {"error": "User not allowed"}, 403

@jwt_required()
def update_type(type_id: int):
    logged_user = get_jwt_identity()
    data = request.json
    try:
        if logged_user['is_admin']:
            raise PermissionError
        avaliable_keys = {'name'}
        data_keys = set(data.keys())
        validate_keys = data_keys.issubset(avaliable_keys)
        if validate_keys == False or type(data['name']) != str:
            raise InvalidUpdateDataError
        TypeModel.query.filter_by(id=type_id).update(data)
        current_app.db.session.commit()
        updated_type = TypeModel.query.filter_by(
            id=type_id).first()
        if updated_type == None:
            raise TypeNotFoundError
        return jsonify(updated_type), 200
    except (InvalidUpdateDataError, TypeNotFoundError) as err:
        return err.message
    except PermissionError as err:
        return {"error": "User not allowed"}, 403
