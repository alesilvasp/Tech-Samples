from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates


@dataclass
class UserAdminModel(db.Model):
    id: int
    name: str
    email: str

    __tablename__ = 'users_admin'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    admin = relationship("ClassModel", backref='admin', uselist=False)

    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()
