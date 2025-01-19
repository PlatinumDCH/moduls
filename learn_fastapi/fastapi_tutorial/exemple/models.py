from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String, select, Integer, ForeignKey

class BaseModel(DeclarativeBase):
    pass

class Contacts(BaseModel):
    __tablename__ = 'contacts'
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name:Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String, default=None)
    # users_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey("users.id"), nullable=True)
    # user: Mapped["Users"] = relationship("Users", backref="todos", lazy="joined")

                                         
# class Users(BaseModel):
#     __tablename__ = "users"
    
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
#     password: Mapped[str] = mapped_column(String(255), nullable=False)
    