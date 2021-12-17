from flask import json
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from app.exceptions.analysis_exceptions import InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError
from app.models.classes_model import ClassModel
from app.models.users_model import UserModel


@dataclass
class AnalysisModel(db.Model):
    id: int
    name: str
    batch: str
    made: datetime
    category: str
    is_concluded: bool
    classe: dict
    analyst_id: int

    __tablename__ = 'analysis'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    batch = db.Column(db.String, nullable=False)
    made = db.Column(db.DateTime)
    category = db.Column(db.String, nullable=False)
    is_concluded = db.Column(db.Boolean)
    classe = db.Column(JSON)

    analyst_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def check_data_creation(cls, token_id, **data):
        valid_keys = [
            'name',
            'batch',
            'made',
            'category',
            'classe',
        ]

        for key in data:
            if key not in valid_keys:
                raise InvalidKeysError()

            if key in ['category', 'batch', 'name']:
                if type(data[key]) != str:
                    raise TypeError()

            if key in ['classe']:
                if type(data[key]) != dict:
                    raise TypeError()

            if key in ['made']:
                try:
                    data[key] = datetime.strptime(data[key], '%d/%m/%Y')
                except:
                    raise TypeError()

        for key in valid_keys:
            if key not in data:
                raise MissingKeysError()

        analysis_analyst = UserModel.query.filter_by(
            id=token_id).first()

        if not analysis_analyst:
            raise ForeignKeyNotFoundError()

    @classmethod
    def check_data_update(cls, **data):
        valid_keys = [
            'made',
            'category',
            'classe',
            'is_concluded',
            'type_to_update',
            'parameter_to_update',
            'result',
        ]

        for key in data:
            if not key in valid_keys:
                raise InvalidKeysError()

            if key in ['category'] and type(data[key]) != str:
                raise TypeError()

            if key in ['made']:
                try:
                    data[key] = datetime.strptime(data[key], '%d/%m/%Y')
                except:
                    raise TypeError()

            if key in ['is_concluded'] and type(data[key]) != bool:
                raise TypeError()

    @validates('category')
    def validate_values(self, key, value: str):
        return value.lower()
