from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from app.configs.database import db
from sqlalchemy import Column, String, Integer, Boolean
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import validates


@dataclass
class AnalisysModel(db.Model):
    id: int
    batch: str
    made: datetime
    category: str
    is_concluded: bool

    __tablename__ = 'analisys'

    id = Column(Integer, primary_key=True)
    batch = Column(String, unique=True, nullable=False)
    made = Column(DateTime)
    category = Column(String, nullable=False)
    is_concluded = Column(Boolean)

    analist_id = Column(Integer, ForeignKey('users_analists.id'))

    @validates('category')
    def validate_values(self, key, value: str):
        return value.lower()
