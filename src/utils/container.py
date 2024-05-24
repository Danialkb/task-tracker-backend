import punq

from folders.dependencies import CreateFolderDep, UpdateFolderDep
from task_status.dependencies import CreateTaskStatusDep, UpdateTaskStatusDep
from tasks.dependencies import UpdateTaskDep, CreateTaskDep, TaskFilterListDep
from utils.dependencies import ListDependency, RetrieveDependency, DeleteDependency
from utils.repository import AbcRepository


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()

    container.register(AbcRepository, repository, instance=repository())

    container.register(ListDependency)
    container.register(RetrieveDependency)
    container.register(DeleteDependency)

    # register folder deps
    container.register(CreateFolderDep)
    container.register(UpdateFolderDep)

    # register task status deps
    container.register(CreateTaskStatusDep)
    container.register(UpdateTaskStatusDep)

    # register task deps
    container.register(CreateTaskDep)
    container.register(UpdateTaskDep)
    container.register(TaskFilterListDep)

    return container
