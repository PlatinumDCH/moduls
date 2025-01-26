import ci.base
import ci.user

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Integer, Text, String, Boolean, DateTime, Date, ForeignKey, func
from typing import Optional

class Blog(ci.base.BaseModel):
    __tablename__ = 'blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    slug: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    author: Mapped["ci.user.User"] = relationship("User", back_populates="blogs", lazy="joined")
    created_at: Mapped[Date] = mapped_column(DateTime, default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

