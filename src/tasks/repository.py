from tasks.models import Task
from utils.repository import BaseRepository
from tasks import schemas


class TaskRepo(BaseRepository):
    model = Task
    action_schema = {
        "create": schemas.CreateTask,
        "create_response": schemas.Task,
        "list": schemas.Task,
        "retrieve": schemas.Task,
        "update": schemas.UpdateTask,
        "update_response": schemas.Task,
    }
