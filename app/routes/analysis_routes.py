
from flask import Blueprint

from app.controllers.analysis_controller import create_analysis, download_certificate, read_analysis, read_by_id_analysis, update_analysis

bp_analysis = Blueprint('bp_analysis', __name__, url_prefix='/analysis')

bp_analysis.post('')(create_analysis)

bp_analysis.get('')(read_analysis)

bp_analysis.get('/<int:id>')(read_by_id_analysis)

bp_analysis.patch('/<int:id>')(update_analysis)

bp_analysis.get('/download/<int:id>')(download_certificate)
