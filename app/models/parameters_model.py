from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates

from app.exceptions import (
    InvalidInputDataError
)

@dataclass
class ParameterModel(db.Model):
    id: int
    name: str
    unity: str
    min: str
    max: str
    result: str

    __tablename__ = 'parameters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    unity = db.Column(db.String, nullable=False)
    min = db.Column(db.String, nullable=False)
    max = db.Column(db.String, nullable=False)
    result = db.Column(db.String)

    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))

    @classmethod
    def check_data(cls, **req_data):
        keys = [
            "name",
            "unity",
            "min",
            "max",
            "result",
        ]

        for key in req_data:
            if key not in keys or req_data[key] != str:

                raise InvalidInputDataError
        
        ...
            

    @validates('name')
    def validate_values(self, key, value: str):
        return value.lower()
