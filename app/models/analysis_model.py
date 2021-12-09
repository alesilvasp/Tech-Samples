from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from datetime import datetime

from app.exceptions.analysis_exceptions import InvalidKeysError, MissingKeysError, TypeError, ForeignKeyNotFoundError
from app.models.classes_model import ClassModel
from app.models.user_analyst_model import UserAnalystModel


@dataclass
class AnalysisModel(db.Model):
    id: int
    batch: str
    made: datetime
    category: str
    is_concluded: bool

    __tablename__ = 'analysis'

    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String, unique=True, nullable=False)
    made = db.Column(db.DateTime)
    category = db.Column(db.String, nullable=False)
    is_concluded = db.Column(db.Boolean)
    
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    analyst_id = db.Column(db.Integer, db.ForeignKey('users_analysts.id'))

    @classmethod
    def check_data(cls, **data):
        valid_keys = [
            'batch',
	        'made',
	        'category',
	        'class_id',
        ]

        for key in data:
            if not key in valid_keys:
                raise InvalidKeysError()

            if key in ['category', 'batch']:
                if type(data[key]) != str:
                    raise TypeError()
            
            if key in ['class_id']:
                if type(data[key]) != int:
                    raise TypeError()
            
            if key in ['made']:
                try:
                    data[key] = datetime.strptime(data[key], '%d-%m-%Y')
                except:
                    raise TypeError()

        for key in valid_keys:
            if not key in data:
                raise MissingKeysError()
        
        analysis_class = ClassModel.query.filter_by(id=data['class_id']).first()
        analysis_analyst = UserAnalystModel.query.filter_by(id=data['analyst_id']).first()

        if not analysis_analyst or not analysis_class:
            raise ForeignKeyNotFoundError()
        


    @validates('category')
    def validate_values(self, key, value: str):
        return value.lower()
