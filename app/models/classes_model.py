from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates, relationship
from app.exceptions.classes_exceptions import InvalidTypeInputDataError, InvalidInputDataError


@dataclass
class ClassModel(db.Model):
    id: int
    name: str
    types: list

    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def check_data(cls, **data):
        avaliable_keys = {'name', 'admin_id'}
        data_keys = set(data.keys())
        validate_keys = avaliable_keys.issubset(data_keys)
        if validate_keys == False:
            raise InvalidInputDataError
        ...

    @validates('name')
    def validate_name(self, key, value):
        print(value)
        if type(value) != str:
            raise InvalidTypeInputDataError
        return value.lower()

    @validates('admin_id')
    def validate_admin_id(self, key, value):
        if key == 'admin_id' and type(value) != int:
            raise InvalidTypeInputDataError
        return value

    types = relationship('TypeModel', backref='classes')
