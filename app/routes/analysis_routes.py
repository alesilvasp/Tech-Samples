
from flask import Blueprint

from app.controllers.analysis_controller import create_analysis, read_analysis, read_by_id_analysis, update_analysis

analysis_blueprint = Blueprint('analysis_blueprint', __name__, url_prefix='/analysis')

analysis_blueprint.post('')(create_analysis)

analysis_blueprint.get('')(read_analysis)

analysis_blueprint.get('/<int:id>')(read_by_id_analysis)

analysis_blueprint.patch('/<int:id>/<int:analyst_id>')(update_analysis)
