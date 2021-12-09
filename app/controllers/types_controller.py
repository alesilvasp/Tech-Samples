from flask import request, current_app, jsonify
from app.models.types_model import TypeModel
from app.exceptions.types_exceptions import InvalidInputDataError, InvalidTypeInputDataError, TypeNotFoundError, InvalidUpdateDataError
import sqlalchemy
import psycopg2


def create_type():
    data = request.json
    try:
        new_type = TypeModel.check_data(**data)
        new_type = TypeModel(**data)
        current_app.db.session.add(new_type)
        current_app.db.session.commit()
        return jsonify(new_type), 201
    except (InvalidInputDataError, InvalidTypeInputDataError) as e:
        return e.message
    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.ForeignKeyViolation:
            return {'error': str(e.orig).split('\n')[1]}, 422


def update_type(type_id: int):

    data = request.json
    try:
        avaliable_keys = {'name'}
        data_keys = set(data.keys())
        validate_keys = data_keys.issubset(avaliable_keys)
        if validate_keys == False or type(data['name']) != str:
            raise InvalidUpdateDataError
        TypeModel.query.filter_by(id=type_id).update(data)
        current_app.db.session.commit()
        updated_type = TypeModel.query.get(type_id)
        if update_type == None:
            raise TypeNotFoundError
        return jsonify(updated_type), 200
    except (InvalidUpdateDataError, TypeNotFoundError) as e:
        return e.message
