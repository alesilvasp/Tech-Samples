from flask import jsonify, request, current_app
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from app.models.analysis_model import AnalysisModel
from app.models.users_model import UserModel
from app.models.classes_model import ClassModel
from app.exceptions.analysis_exceptions import InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError


@jwt_required()
def create_analysis():
    data = request.json
    session = current_app.db.session
    found_class = (
        ClassModel
        .query
        .filter_by(id=data['class_id'])
        .first()
    )
    classe = {
        'class_name': found_class.name,
        'class_id': found_class.id,
        'types': [{
            'type_name': type.name,
            'parameters': [{
                'parameter_name': parameter.name,
                'min': parameter.min,
                'max': parameter.max,
                'unit': parameter.unit,
                'result': parameter.result,
                'is_approved': parameter.is_approved,
            } for parameter in type.parameters],
        } for type in found_class.types],
    }

    data['classe'] = classe
    del data['class_id']
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
    
    
    print(data.items())
    # to_update = data['classe']['types'][0]['parameters'][0]
    # to_update2 = data['classe']['types'][1]['parameters'][0]
    # print(to_update2)

    # analysis.classe['types'][0]['parameters'][0].update(to_update)
    # analysis.classe['types'][1]['parameters'][0].update(to_update2)
    # print('-' * 50)
    # print(analysis.classe)
    return ''
    # for key in data:
    #     setattr(analysis, key, data[key])
    
    # analysis.update(analysis.classe)

    # session.commit()

    # return jsonify(analysis)
