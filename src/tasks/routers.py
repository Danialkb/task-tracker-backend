from fastapi import APIRouter, Depends

from tasks.dependencies import UpdateTaskDep, CreateTaskDep, UpdateStartedTaskDep, UpdateFinishedTaskDep, \
    TaskFilterListDep
from tasks.repository import TaskRepo
from utils.container import get_container
from utils.dependencies import ListDependency, DeleteDependency, RetrieveDependency

router = APIRouter(prefix="/tasks", tags=["Tasks"])

router.add_api_route(
    "/", get_container(TaskRepo).resolve(CreateTaskDep),
    methods=["POST"], name="create_task",
)

router.add_api_route(
    "/", get_container(TaskRepo).resolve(TaskFilterListDep),
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


# @router.put("/{id}/start_task")
# async def start_task(update_dep: Depends(UpdateStartedTaskDep)):
#     return update_dep
#
#
# @router.put("/{id}/start_task")
# async def finish_task(update_dep: Depends(UpdateFinishedTaskDep)):
#     return update_dep
