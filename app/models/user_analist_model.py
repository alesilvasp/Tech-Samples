from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates


@dataclass
class UserAnalistModel(db.Model):
    id: int
    name: str
    email: str
    
    __tablename__ = 'users_analists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    analist = relationship("AnalisysModel", backref='analist', uselist=False)
    
    @validates('name, email')
    def validate_values(self, key, value):
        return value.lower()
    
    