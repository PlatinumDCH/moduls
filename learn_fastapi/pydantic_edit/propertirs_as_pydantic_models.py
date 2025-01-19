from pydantic import BaseModel
from typing import Optional

class Comment(BaseModel):
    text: Optional[str]= None

class Blog(BaseModel):
    title: str
    comment: Optional[list[Comment]]
    is_active: bool

