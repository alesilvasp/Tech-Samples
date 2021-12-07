from flask import Blueprint
from app.controllers.parameters_controller import (
    create_parameter,
    read_parameters_by_type_id,
    delete_parameter
)

bp = Blueprint("bp_parameters", __name__)

bp.post("/classes/types/<int:type_id>/parameters")(create_parameter)
bp.get("/classes/types/<int:type_id>/parameters")(read_parameters_by_type_id)
bp.delete("/classes/types/parameters/<int:parameter_id>")(delete_parameter)