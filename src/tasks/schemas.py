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


class Task(BaseTask):
    id: int
    folder: Folder
    status: TaskStatus
