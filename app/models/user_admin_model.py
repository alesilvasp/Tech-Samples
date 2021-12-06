from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates


@dataclass
class UserAdminModel(db.Model):
    id: int
    name: str
    email: str

    __tablename__ = 'users_admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    classes = db.relationship("ClassModel", backref='admin', uselist=False)

    @validates('name, email')
    def validate_values(self, key, value: str):
        return value.lower()
