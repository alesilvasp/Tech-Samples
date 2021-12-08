from flask import request
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from app.exceptions.user_exceptions import DataContentError


def login():
    data = request.get_json()
    try:
        UserModel.check_login_data(data)

        user: UserModel = UserModel.query.filter_by(
            email=data["email"]).first()

        if not user:
            return {"message": "User not found"}, 404

        if user.verify_password(data["password"]):
            access_token = create_access_token(identity=user)
            return {"token": access_token}, 200
        else:
            return {"message": "Unauthorized"}, 401
    except DataContentError as error:
        return error.message
