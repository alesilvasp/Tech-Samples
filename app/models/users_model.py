from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
from app.exceptions.user_exceptions import DataContentError, EmailFormatError
import re


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    email: str
    is_admin: bool

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String, nullable=True)

    classes = db.relationship("ClassModel", backref='admin', uselist=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @classmethod
    def check_data(cls, data):
        keys = ['name', 'email', 'is_admin', 'password']

        for key in keys:
            if key not in data:
                raise DataContentError(key)

        for key in data:
            if key not in keys:
                raise DataContentError(key)

    @classmethod
    def check_login_data(cls, data):
        keys = ['email', 'password']

        for key in keys:
            if key not in data:
                raise DataContentError(key)

        for key in data:
            if key not in keys:
                raise DataContentError(key)

    @validates('name')
    def validate_values(self, key, name: str):
        return name.lower()

    @validates('email')
    def validate_email(self, key, email: str):
        if not re.match(r'^[a-zA-Z0-9]+([.-_]?[a-zA-Z0-9]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', email):
            raise EmailFormatError
        return email.lower()
