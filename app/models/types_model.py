from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.orm import validates


@dataclass
class TypeModel(db.Model):
    id: int
    name: str
    
    __tablename__ = 'types'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    class_id = Column(Integer, ForeignKey('classes.id'))
    
    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()