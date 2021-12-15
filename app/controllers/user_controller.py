import sqlalchemy
from flask import request, current_app, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.exceptions.user_exceptions import DataContentError, EmailFormatError, InvalidUpdateDataError
from app.models.users_model import UserModel
from app.utils.email import send_login_information


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

    except (DataContentError, EmailFormatError) as err:
        return err.message
    except sqlalchemy.exc.IntegrityError as err:
        return {"error": "Email already registred"}, 409


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

        send_login_information(data['email'], password_to_hash, data['name'])

        return jsonify(new_analyst), 201

    except (DataContentError, EmailFormatError) as err:
        return err.message
    except sqlalchemy.exc.IntegrityError as err:
        return {"error": "Email already registred"}, 409
    except PermissionError as err:
        return {"error": "User not allowed"}, 403


@jwt_required()
def change_password():
    user = get_jwt_identity()

    data = request.get_json()

    try:

        avaliable_keys = {'password'}
        data_keys = set(data.keys())
        validate_keys = data_keys.issubset(avaliable_keys)
        if validate_keys == False or type(data['password']) != str:
            raise InvalidUpdateDataError

        user_to_update = UserModel.query.filter_by(id=user['id']).first()

        for key, value in data.items():
            setattr(user_to_update, key, value)

        current_app.db.session.add(user_to_update)
        current_app.db.session.commit()
        return {'msg': 'Password changed'}, 200

    except InvalidUpdateDataError as err:
        return err.message
    except PermissionError as err:
        return {"error": "User not allowed"}, 403


def read_users():
    data = UserModel.query.all()

    if data:
        return jsonify(data), 200
    else:
        return {'msg': 'Empty database'}, 200
