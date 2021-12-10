from flask import request, current_app, jsonify
from app.models.classes_model import ClassModel
from app.exceptions.classes_exceptions import ConflictError, InvalidTypeInputDataError, InvalidInputDataError
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
    except (ConflictError, InvalidInputDataError, InvalidTypeInputDataError) as err:
        return err.message
    except sqlalchemy.exc.IntegrityError as err:
        if type(err.orig) == psycopg2.errors.ForeignKeyViolation:
            return {'error': str(err.orig).split('\n')[1]}, 422


def read_all_class():
    classes = ClassModel.query.all()

    return jsonify(classes)
