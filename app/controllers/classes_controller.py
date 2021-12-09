from flask import request, current_app, jsonify
from app.models.classes_model import ClassModel
from app.exceptions.classes_exceptions import InvalidTypeInputDataError, InvalidInputDataError
import sqlalchemy
import psycopg2


def create_class():
    data = request.json
    try:
        new_class = ClassModel.check_data(**data)
        new_class = ClassModel(**data)
        current_app.db.session.add(new_class)
        current_app.db.session.commit()
        return jsonify(new_class)
    except (InvalidInputDataError, InvalidTypeInputDataError) as e:
        return e.message
    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.ForeignKeyViolation:
            return {'error': str(e.orig).split('\n')[1]}, 422
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'error': 'class already exists'}, 409


def read_all_class():
    classes = ClassModel.query.all()

    return jsonify(classes)
