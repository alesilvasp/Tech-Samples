
from datetime import datetime
from flask import jsonify, request, current_app
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.analysis_model import AnalysisModel
from app.models.user_analyst_model import UserAnalystModel
from app.exceptions.analysis_exceptions import InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError

@jwt_required()
def create_analysis():
    data = request.json
    session = current_app.db.session

    try:
        AnalysisModel.check_data(**data)
    except (InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError) as err:
        return err.message
    
    analyst: UserAnalystModel = get_jwt_identity()

    analysis = AnalysisModel(**data, is_concluded=False, aanalyst_id=analyst.id)

    try:
        session.add(analysis)
        session.commit()
    except IntegrityError as err:
        return {'error': f'Analysis with batch id {analysis.batch} already exists.'}, 409

    return jsonify(analysis), 201    

@jwt_required()
def read_analysis():
    analyst: UserAnalystModel = get_jwt_identity()

    analysis = AnalysisModel.query.filter_by(analyst_id=analyst.id).all()
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
    analyst: UserAnalystModel = get_jwt_identity()
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

    try:
        valid_keys = [
	        'made',
	        'category',
	        'class_id',
	        'analyst_id',
            'is_concluded'
        ]

        for key in data:
            if not key in valid_keys:
                raise InvalidKeysError()

            if key in ['category'] and type(data[key]) != str:
                    raise TypeError()
            
            if key in ['class_id', 'analyst_id'] and type(data[key]) != int:
                    raise TypeError()
            
            if key in ['made']:
                try:
                    data[key] = datetime.strptime(data[key], '%d-%m-%Y')
                except:
                    raise TypeError()       

            if key in ['is_concluded'] and type(data[key]) != bool:
                raise TypeError()

    except (InvalidKeysError, TypeError, ForeignKeyNotFoundError) as err:
        return err.message

    analyst: UserAnalystModel = get_jwt_identity()
    analysis = AnalysisModel.query.filter_by(id=id).first()

    if not analysis:
        return {'error': f'Analysis with id {id} was not found.'}, 404
    
    analyst = UserAnalystModel.query.filter_by(id=analyst.id).first()

    if not analyst:
        return {'error': f'Analyst with id {analyst.id} was not found.'}, 404
    
    if analysis.analyst_id != analyst.id: 
        return {'error': f'Analyst with id {analyst.id} has no access to analysis {id}'}, 401
    
    for key in data:
        setattr(analysis, key, data[key])
    
    session.commit()
    
    return jsonify(analysis)