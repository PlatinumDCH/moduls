from sqlalchemy import Column, Integer, String, Boolean
from pattern.creational.singleton_pattern.sengletonFastAPI.database import base

class Todo(base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


