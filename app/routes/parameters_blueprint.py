from flask import Blueprint
from app.controllers.parameters_controller import (
    create_parameter,
    delete_parameter

)

bp_parameters = Blueprint("bp_parameters", __name__)

bp_parameters.post("/classes/types/parameters")(create_parameter)
bp_parameters.delete(
    "/classes/types/parameters/<int:parameter_id>")(delete_parameter)
