from flask import request, current_app, jsonify
from app.exceptions.parameters_exceptions import ParametersNotFoundError
from app.models.parameters_model import ParameterModel
from app.models.types_model import TypeModel

from app.exceptions import (
    InvalidInputDataError,
    ParametersNotFoundError
)

def create_parameter(type_id: int):
    """
    This function takes a "type_id" wich will be the type the new parameter will be asigned to.  
    """

    session = current_app.db.session

    req_data = request.get_json()

    try:
        validate_keys = ParameterModel.check_data(**req_data)
    
    except InvalidInputDataError as err:

        return err.msg

    req_data['type_id'] = type_id

    new_parameter = ParameterModel(**req_data)

    session.add(new_parameter)
    session.commit()

    return jsonify(new_parameter)


def read_parameters_by_type_id(type_id: int):

    try:
        found_parameters = (
            ParameterModel
                .query
                .filter_by(type_id=type_id)
                .all()
        )
        
        if found_parameters == None:

            raise ParametersNotFoundError

    except ParametersNotFoundError as err:

        return err.message

    return jsonify(found_parameters), 200


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

