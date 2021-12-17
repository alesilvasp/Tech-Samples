from flask import Blueprint
from app.controllers.types_controller import create_type, update_type

bp_types = Blueprint('bp_types', __name__, url_prefix='/classes/types')

bp_types.post('')(create_type)
bp_types.patch('/<int:type_id>')(update_type)
