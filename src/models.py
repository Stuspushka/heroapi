from sqlalchemy.orm import Mapped,mapped_column

from src.database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True, index=True)
    intelligence: Mapped[int]
    strength: Mapped[int]
    speed: Mapped[int]
    power: Mapped[int]
