from flask import Blueprint
from app.controllers.classes_controller import create_class, read_all_class

bp_classes = Blueprint('classes_bp', __name__, url_prefix='/classes')

bp_classes.post('')(create_class)
bp_classes.get('')(read_all_class)
