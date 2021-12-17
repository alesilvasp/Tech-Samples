from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from app.exceptions.types_exceptions import InvalidInputDataError, InvalidTypeInputDataError


@dataclass
class TypeModel(db.Model):
    id: int
    name: str
    parameters: list

    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    @classmethod
    def check_data(cls, **data):
        avaliable_keys = {'name', 'class_id'}
        data_keys = set(data.keys())
        validate_keys = avaliable_keys.issubset(data_keys)
        if validate_keys == False or len(data_keys) > 2:
            raise InvalidInputDataError
        if type(data['name']) != str or type(data['class_id']) != int:
            raise InvalidTypeInputDataError
        ...

    @validates('name')
    def validate_values(self, key, value: str):
        return value.lower()

    parameters = db.relationship(
        'ParameterModel', backref='types')
