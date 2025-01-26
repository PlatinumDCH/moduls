from ci.base import BaseModel
from ci.user import User
from ci.blog import Blog
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
BaseModel.metadata.create_all(engine)