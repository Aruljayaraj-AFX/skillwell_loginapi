from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

user_Base = declarative_base()

class users(user_Base):
    __tablename__='users'
    user_email = Column(String, primary_key=True,nullable=False)
    password=Column(String,nullable=False)
    created_at = Column(DateTime, default=func.now())  