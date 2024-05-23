from fastapi import APIRouter

from tasks.dependencies import UpdateTaskDep, CreateTaskDep
from tasks.repository import TaskRepo
from utils.container import get_container
from utils.dependencies import ListDependency, DeleteDependency, RetrieveDependency

router = APIRouter(prefix="/tasks", tags=["Tasks"])

router.add_api_route(
    "/", get_container(TaskRepo).resolve(CreateTaskDep),
    methods=["POST"], name="create_task",
)

router.add_api_route(
    "/", get_container(TaskRepo).resolve(ListDependency),
    methods=["GET"], name="list_tasks",
)

router.add_api_route(
    "/{id}", get_container(TaskRepo).resolve(RetrieveDependency),
    methods=["GET"], name="retrieve_task",
)

router.add_api_route(
    "/{id}", get_container(TaskRepo).resolve(UpdateTaskDep),
    methods=["PUT"], name="update_task",
)

router.add_api_route(
    "/{id}", get_container(TaskRepo).resolve(DeleteDependency),
    methods=["DELETE"], name="delete_task",
)
