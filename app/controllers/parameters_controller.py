from flask import request, current_app, jsonify
from app.exceptions.types_exceptions import TypeNotFoundError
from app.models.parameters_model import ParameterModel

from app.exceptions.parameters_exceptions import (
    InvalidInputDataError,
    InvalidDataTypeError,
    InvalidUpdateDataError,
    ParametersNotFoundError
)
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_parameter():

    logged_user = get_jwt_identity()

    session = current_app.db.session

    req_data = request.get_json()

    try:

        if logged_user['is_admin']:
            raise PermissionError

        ParameterModel.check_data(**req_data)

        new_parameter = ParameterModel(**req_data)

        session.add(new_parameter)
        session.commit()

        return jsonify(new_parameter), 201

    except (InvalidInputDataError, TypeNotFoundError) as err:

        return err.message

    except PermissionError as err:
        return {"error": "User not allowed"}, 403


@jwt_required()
def delete_parameter(parameter_id: int):

    logged_user = get_jwt_identity()
    session = current_app.db.session

    try:

        if logged_user['is_admin']:
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


@jwt_required()
def update_parameter(parameter_id: int):
    logged_user = get_jwt_identity()
    session = current_app.db.session

    req_data = request.get_json()

    try:
        if logged_user['is_admin']:
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

    try:
        valid_update = [
            "result",
            "is_approved"
        ]

        valid_inputs = [key for key in req_data if key in valid_update]

        if len(valid_inputs) == 0:

            raise InvalidUpdateDataError

    except InvalidUpdateDataError as err:

        return err.message

    # deleting unused request keys

    for key in req_data.copy():

        if key not in valid_update:

            del req_data[key]

    # changing values

    try:
        for key, value in req_data.items():

            setattr(found_parameter, key, value)

    except InvalidDataTypeError as err:

        return err.message

    session.add(found_parameter)
    session.commit()

    return jsonify(found_parameter), 200
