from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from datetime import datetime


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

    @validates('category')
    def validate_values(self, key, value: str):
        return value.lower()
