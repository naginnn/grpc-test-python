import uuid
from datetime import timedelta, datetime

from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.collections import InstrumentedList

Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    created_at = Column(DateTime, nullable=True)
    last_login = Column(DateTime, nullable=True)

    # {
    #     "id": 8,
    #     "username": "user2",
    #     "password": "123",
    #     "email": "user2@gmail.com",
    #     "created_at": "2024-02-24 15:10:09.000000",
    #     "last_login": "2024-02-24 15:10:15.000000"
    # }
