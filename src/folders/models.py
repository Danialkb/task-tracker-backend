from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from utils.model_constants import default_id


class Folder(Base):
    __tablename__ = "folder"

    id: Mapped[default_id]
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    path: Mapped[str]
    is_leaf: Mapped[bool] = mapped_column(default=True)
    depth: Mapped[int] = mapped_column(default=1)

    # relationships
    tasks = relationship("Task", back_populates="folder")
