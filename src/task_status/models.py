from sqlalchemy.orm import Mapped, mapped_column

from database import Base
from utils.model_constants import default_id


class TaskStatus(Base):
    __tablename__ = "task_status"

    id: Mapped[default_id]
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
