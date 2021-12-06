from sqlalchemy.orm.mapper import validates
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass

@dataclass
class ClassModel(db.Model):
    id: int
    name: str
    
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    admin_id = Column(Integer, ForeignKey('users_admin.id'))
    
    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()