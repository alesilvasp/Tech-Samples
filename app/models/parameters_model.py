from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates

from app.exceptions import (
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

    __tablename__ = 'parameters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False) #unit
    min = db.Column(db.String, nullable=False)
    max = db.Column(db.String, nullable=False)
    result = db.Column(db.String)

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
            if key not in valid_post.keys():

                raise InvalidInputDataError
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

    @validates('type_id')
    def validate_type_id(self, key, type_id):
        if type(type_id) == int:
            return type_id
        else:
            raise InvalidDataTypeError