from flask import request, current_app, jsonify
from app.exceptions.types_exceptions import TypeNotFoundError
from app.models.parameters_model import ParameterModel

from app.exceptions.parameters_exceptions import (
    InvalidInputDataError,
    InvalidDataTypeError,
    ParametersNotFoundError
)
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_parameter():

    logged_user = get_jwt_identity()

    session = current_app.db.session

    req_data = request.get_json()

    try:

        if not logged_user['is_admin']:
            raise PermissionError

        ParameterModel.check_data(**req_data)

        new_parameter = ParameterModel(**req_data)

        session.add(new_parameter)
        session.commit()

        return jsonify(new_parameter), 201

    except (InvalidDataTypeError, InvalidInputDataError, TypeNotFoundError) as err:

        return err.message

    except PermissionError as err:
        return {"error": "User not allowed"}, 403


@jwt_required()
def delete_parameter(parameter_id: int):

    logged_user = get_jwt_identity()
    session = current_app.db.session

    try:

        if not logged_user['is_admin']:
            raise PermissionError

        found_parameter = (
            ParameterModel
            .query
            .filter_by(id=parameter_id)
            .first()
        )

        if found_parameter == None:

            raise ParametersNotFoundError

    except ParametersNotFoundError as err:

        return err.message

    except PermissionError as err:
        return {"error": "User not allowed"}, 403

    session.delete(found_parameter)
    session.commit()

    return "", 204
