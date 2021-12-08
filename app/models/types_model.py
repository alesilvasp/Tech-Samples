from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates


@dataclass
class TypeModel(db.Model):
    id: int
    name: str
    
    __tablename__ = 'types'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    
    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()