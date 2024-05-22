from fastapi import APIRouter
from task_status.dependencies import CreateTaskStatusDep, UpdateTaskStatusDep
from task_status.repository import TaskStatusRepo
from utils.container import get_container
from utils.dependencies import ListDependency, RetrieveDependency, DeleteDependency

router = APIRouter(prefix="/task_status", tags=["Task Status"])


router.add_api_route(
    "/", get_container(TaskStatusRepo).resolve(CreateTaskStatusDep),
    methods=["POST"], name="create_task_status",
)

router.add_api_route(
    "/", get_container(TaskStatusRepo).resolve(ListDependency),
    methods=["GET"], name="list_task_statuses",
)

router.add_api_route(
    "/{id}", get_container(TaskStatusRepo).resolve(RetrieveDependency),
    methods=["GET"], name="retrieve_task_status",
)

router.add_api_route(
    "/{id}", get_container(TaskStatusRepo).resolve(UpdateTaskStatusDep),
    methods=["PUT"], name="update_task_status",
)

router.add_api_route(
    "/{id}", get_container(TaskStatusRepo).resolve(DeleteDependency),
    methods=["DELETE"], name="delete_task_status",
)

