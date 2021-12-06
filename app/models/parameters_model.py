from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.orm import validates

@dataclass
class ParameterModel(db.Model):
    id: int
    name: str
    unity: str
    min: str
    max: str
    result: str

    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unity = Column(String, nullable=False)
    min = Column(String, nullable=False)
    max = Column(String, nullable=False)
    result = Column(String)

    type_id = Column(Integer, ForeignKey('types.id'))

    @validates('name')
    def validate_values(self, key, value: str):
        return value.lower()
