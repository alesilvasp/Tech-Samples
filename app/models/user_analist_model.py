from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates


@dataclass
class UserAnalistModel(db.Model):
    id: int
    name: str
    email: str
    
    __tablename__ = 'users_analists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    
    analisys = db.relationship("AnalisysModel", backref='analist', uselist=False)
    
    @validates('name, email')
    def validate_values(self, key, value):
        return value.lower()
    
    