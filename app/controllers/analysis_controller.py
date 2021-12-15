from flask import jsonify, request, current_app, send_from_directory
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from app.models.analysis_model import AnalysisModel
from app.models.classes_model import ClassModel
from app.models.users_model import UserModel
from app.exceptions.analysis_exceptions import InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError

from app.models.certificate_model import CertificateModel
from fpdf import FPDF

@jwt_required()
def create_analysis():
    data = request.json
    session = current_app.db.session

    analyst = get_jwt_identity()
    analyst_id = analyst['id']
    analyst: UserModel = UserModel.query.filter_by(id=analyst_id).first()
    
    try:
        AnalysisModel.check_data_creation(analyst_id, **data)
    except (InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError) as err:
        return err.message


    if not analyst:
        return {'error': f'Analyst with id {analyst_id} was not found.'}, 404

    if analyst.is_admin:
        return {'error': f'User {analyst_id} is not a analyst.'}, 401

    analysis = AnalysisModel(
        **data, is_concluded=False, analyst_id=analyst.id)

    try:
        session.add(analysis)
        session.commit()
    except IntegrityError as err:
        return {'error': f'Analysis with batch id {analysis.batch} already exists.'}, 409

    return jsonify(analysis), 201


@jwt_required()
def read_analysis():
    analyst = get_jwt_identity()
    analyst_id = analyst['id']
    analyst: UserModel = UserModel.query.filter_by(id=analyst_id).first()

    if not analyst:
        return {'error': f'Analyst with id {analyst_id} was not found.'}, 404

    if analyst.is_admin:
        return {'error': f'User {analyst.id} is not a analyst.'}, 401

    analysis: list[AnalysisModel] = AnalysisModel.query.filter_by(
        analyst_id=analyst.id).all()
    concluded_analysis = list()
    pending_analysis = list()

    if analysis != None:
        for a in analysis:
            if a.is_concluded:
                concluded_analysis.append(a)
            else:
                pending_analysis.append(a)

    return jsonify({
        'concluded_analysis': concluded_analysis,
        'pending_analysis': pending_analysis
    })


@jwt_required()
def read_by_id_analysis(id: int):
    analyst = get_jwt_identity()
    analyst_id = analyst['id']
    analyst: UserModel = UserModel.query.filter_by(id=analyst_id).first()

    if not analyst:
        return {'error': f'Analyst with id {analyst_id} was not found.'}, 404

    if analyst.is_admin:
        return {'error': f'User {analyst.id} is not a analyst.'}, 401

    analysis = AnalysisModel.query.filter_by(id=id).first()

    if not analysis:
        return {'error': f'Analysis with id {id} was not found.'}, 404

    if analysis.analyst_id == analyst.id:
        return jsonify(analysis)

    return {'error': f'Analyst with id {analyst.id} has no access to analysis {id}'}, 401


@jwt_required()
def update_analysis(id: int):
    data = request.json
    session = current_app.db.session
    
    analyst = get_jwt_identity()
    analyst_id = analyst['id']
    analyst: UserModel = UserModel.query.filter_by(id=analyst_id).first()

    try:
        AnalysisModel.check_data_update(**data)
    except (InvalidKeysError, TypeError, ForeignKeyNotFoundError) as err:
        return err.message

    if not analyst:
        return {'error': f'Analyst with id {analyst_id} was not found.'}, 404

    if analyst.is_admin:
        return {'error': f'User {analyst.id} is not a analyst.'}, 401

    analysis = AnalysisModel.query.filter_by(id=id).first()

    if not analysis:
        return {'error': f'Analysis with id {id} was not found.'}, 404

    analyst = UserModel.query.filter_by(id=analyst.id).first()

    if analysis.analyst_id != analyst.id:
        return {'error': f'Analyst with id {analyst.id} has no access to analysis {id}'}, 401

    for key in data:
        setattr(analysis, key, data[key])

    session.commit()

    return jsonify(analysis)


def download_certificate(id: int):

    analysis: AnalysisModel = (
        AnalysisModel
            .query
            .filter_by(id=id)
            .first()
    )

    if not analysis:
        return {'error': f'Analysis with id {id} was not found.'}, 404

    if not analysis.is_concluded:
        return {'error': f'Analysis was not concluded, certificate unavailable'}, 404

    analysis_class: ClassModel = (
        ClassModel
            .query
            .filter_by(id=analysis.class_id)
            .first()
    )

    analyst: UserModel = (
        UserModel
            .query
            .filter_by(id=analysis.analyst_id)
            .first()
    )

    certificate_data = {
    "id": analysis.id,
    "batch": analysis.batch,
    "made": analysis.made.strftime('%d/%m/%Y'),
    "category": analysis.category,
    "class": {
        "id": analysis_class.id,
        "name": analysis_class.name,
        "types": [{
            "id": type.id,
            "name": type.name,
            "parameters": [{
                "id": parameter.id,
                "name": parameter.name,
                "min": parameter.min,
                "max": parameter.max,
                "result": parameter.result,
                "is_approved": parameter.is_approved,
                "unit": parameter.unit
                }for parameter in type.parameters],
        }for type in analysis_class.types],
    },
    "analyst_name": analyst.name,
    }

    certificate = CertificateModel()

    certificate.add_page()

    certificate.lines()

    certificate.titles()

    certificate.subtitles()

    certificate.logo_image()

    certificate.texts(certificate_data)

    certificate.output('Certificate.pdf', 'F')

    certificate.close()

    return send_from_directory(directory='../', path='Certificate.pdf', as_attachment=False), 200
