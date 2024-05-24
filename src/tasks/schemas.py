from datetime import datetime
from typing import Optional

from task_status.schemas import TaskStatus

from folders.schemas import Folder
from utils.schemas_config import BaseSchema


class BaseTask(BaseSchema):
    title: str
    description: str


class CreateTask(BaseTask):
    folder_id: int
    status_id: int


class UpdateTask(BaseTask):
    title: str
    description: str
    folder_id: int
    status_id: int
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class UpdateTaskStartedDate(BaseSchema):
    started_at: datetime = datetime.now()


class UpdateTaskFinishedDate(BaseSchema):
    finished_at: datetime = datetime.now()


class Task(BaseTask):
    id: int
    folder: Folder
    status: TaskStatus
