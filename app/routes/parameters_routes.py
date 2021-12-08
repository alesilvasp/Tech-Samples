from flask import Blueprint
from app.controllers.parameters_controller import (
    create_parameter,
    delete_parameter
)

bp = Blueprint("bp_parameters", __name__)

bp.post("/classes/types/parameters")(create_parameter)
bp.delete("/classes/types/parameters/<int:parameter_id>")(delete_parameter)