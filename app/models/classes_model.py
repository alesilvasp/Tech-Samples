from sqlalchemy.orm import validates
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class ClassModel(db.Model):
    id: int
    name: str
    
    __tablename__ = 'classes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    
    admin_id = db.Column(db.Integer, db.ForeignKey('users_admin.id'))
    
    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()