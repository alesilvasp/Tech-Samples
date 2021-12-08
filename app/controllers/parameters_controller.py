from flask import request, current_app, jsonify
from app.exceptions.parameters_exceptions import InvalidUpdateDataError, ParametersNotFoundError
from app.models.parameters_model import ParameterModel
from app.models.types_model import TypeModel

from app.exceptions import (
    InvalidInputDataError,
    ParametersNotFoundError
)

def create_parameter():

    session = current_app.db.session

    req_data = request.get_json()

    try:
        validate_keys = ParameterModel.check_data(**req_data)
    
    except InvalidInputDataError as err:

        return err.msg

    new_parameter = ParameterModel(**req_data)

    session.add(new_parameter)
    session.commit()

    return jsonify(new_parameter)


def delete_parameter(parameter_id: int):

    session = current_app.db.session

    try:
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

    session.delete(found_parameter)
    session.commit()

    return "", 204


def update_parameter(parameter_id: int):

    session = current_app.db.session

    req_data = request.get_json()

    try:
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

    try:
        valid_update = [
            "result",
        ]

        valid_inputs = [key for key in req_data if key in valid_update]

        if len(valid_inputs) == 0:

            raise InvalidUpdateDataError
    
    except InvalidUpdateDataError as err:

        return err.message

    # deleting unused 

    for key in req_data.copy():

        if key not in valid_update:

            del req_data[key]

    # changing values

    for key, value in req_data.items():

        setattr(found_parameter, key, value)

    session.add(found_parameter)
    session.commit()

    return jsonify(found_parameter), 200



    
    

