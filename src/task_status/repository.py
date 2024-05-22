from task_status.models import TaskStatus
from utils.repository import BaseRepository
from task_status import schemas


class TaskStatusRepo(BaseRepository):
    model = TaskStatus
    action_schema = {
        "list": schemas.TaskStatus,
        "retrieve": schemas.TaskStatus,
        "create": schemas.CreateTaskStatus,
        "update": schemas.UpdateTaskStatus,
    }

