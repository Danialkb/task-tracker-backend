from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from utils.model_constants import default_id


class Task(Base):
    __tablename__ = "task"

    id: Mapped[default_id]
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(default="")

    folder_id: Mapped[int] = mapped_column(ForeignKey("folder.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("task_status.id"))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    started_at: Mapped[datetime] = mapped_column(nullable=True)
    finished_at: Mapped[datetime] = mapped_column(nullable=True)

    # relationships
    folder = relationship("Folder", back_populates="tasks")
    status = relationship("TaskStatus", back_populates="tasks")
