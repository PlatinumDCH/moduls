from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, select

class BaseModel(DeclarativeBase):
    pass

class Contacts(BaseModel):
    __tablename__ = 'contacts'
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name:Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String, default=None)