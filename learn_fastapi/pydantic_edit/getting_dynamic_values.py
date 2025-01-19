from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str
    creates_at: datetime = datetime.now()
    is_active: bool

print(Blog(title='Our first blog', is_active=True))
# title='Our first blog' creates_at=datetime.datetime(2025, 1, 18, 11, 51, 29, 113740) is_active=True