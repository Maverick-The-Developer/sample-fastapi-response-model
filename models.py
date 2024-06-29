from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) 
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
    name: Mapped[str] = mapped_column(default='')
    role: Mapped[int] = mapped_column(default=0)