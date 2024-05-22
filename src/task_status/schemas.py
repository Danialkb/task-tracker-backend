from utils.schemas_config import BaseSchema


class BaseTaskStatus(BaseSchema):
    name: str


class CreateTaskStatus(BaseTaskStatus):
    pass


class UpdateTaskStatus(BaseTaskStatus):
    pass


class TaskStatus(BaseTaskStatus):
    id: int
