from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates

@dataclass
class ParameterModel(db.Model):
    id: int
    name: str
    unit: str
    min: str
    max: str
    result: str

    __tablename__ = 'parameters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    unit = db.Column(db.String, nullable=False) #unit
    min = db.Column(db.String, nullable=False)
    max = db.Column(db.String, nullable=False)
    result = db.Column(db.String)

    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))

    @validates('name')
    def validate_values(self, key, value: str):
        return value.lower()
