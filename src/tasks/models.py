from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from utils.model_constants import default_id


class Task(Base):
    __tablename__ = "task"

    id: Mapped[default_id]
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(default="")
    folder_id: Mapped[int] = mapped_column(ForeignKey("folder.id"))

    # relationships
    folder = relationship("Folder", back_populates="tasks")
