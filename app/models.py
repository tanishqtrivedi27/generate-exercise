from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class UserError(Base):
    __tablename__ = "user_errors"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    category = Column(String)
    sub_category = Column(String)
    frequency = Column(Integer)
    last_updated = Column(DateTime)
