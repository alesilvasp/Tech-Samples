from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from app.models.types_model import TypeModel
from app.exceptions.types_exceptions import TypeNotFoundError
from app.exceptions.parameters_exceptions import (
    InvalidInputDataError,
    InvalidDataTypeError
)


@dataclass
class ParameterModel(db.Model):
    id: int
    name: str
    unit: str
    min: str
    max: str
    result: str
    is_approved: str

    __tablename__ = 'parameters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False)
    min = db.Column(db.String, nullable=False)
    max = db.Column(db.String, nullable=False)
    result = db.Column(db.String, default="")
    is_approved = db.Column(db.Boolean, nullable=False, default=False)

    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))

    @classmethod
    def check_data(cls, **req_data):
        valid_post = [
            "name",
            "unit",
            "min",
            "max",
            "type_id"
        ]

        for key in req_data:
            if key not in valid_post:
                raise InvalidInputDataError

        for key in valid_post:
            if key not in req_data:
                raise InvalidInputDataError

        type_ref = TypeModel.query.filter_by(
            id=req_data['type_id']).one_or_none()
        if not type_ref:
            raise TypeNotFoundError
        ...

    @validates('name')
    def validate_name(self, key, name):
        if type(name) == str:
            return name.lower()
        else:
            raise InvalidDataTypeError

    @validates('unit')
    def validate_unit(self, key, unit):
        if type(unit) == str:
            return unit.lower()
        else:
            raise InvalidDataTypeError

    @validates('min')
    def validate_min(self, key, min):
        if type(min) == str:
            return min.lower()
        else:
            raise InvalidDataTypeError

    @validates('max')
    def validate_max(self, key, max):
        if type(max) == str:
            return max.lower()
        else:
            raise InvalidDataTypeError

    @validates('result')
    def validate_result(self, key, result):
        if type(result) == str:
            return result.lower()
        else:
            raise InvalidDataTypeError

    @validates('is_approved')
    def validate_is_approved(self, key, is_approved):
        if type(is_approved) == bool:
            return is_approved
        else:
            raise InvalidDataTypeError

    @validates('type_id')
    def validate_type_id(self, key, type_id):
        if type(type_id) == int:
            return type_id
        else:
            raise InvalidDataTypeError
