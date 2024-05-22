from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from tasks.models import Task
from utils.model_constants import default_id


class TaskStatus(Base):
    __tablename__ = "task_status"

    id: Mapped[default_id]
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    # relationships
    tasks = relationship(Task, back_populates="status")
