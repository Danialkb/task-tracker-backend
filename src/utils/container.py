import punq

from folders.dependencies import CreateFolderDep, UpdateFolderDep
from utils.dependencies import ListDependency, RetrieveDependency, DeleteDependency
from utils.repository import AbcRepository


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()

    container.register(AbcRepository, repository, instance=repository())

    container.register(ListDependency)
    container.register(RetrieveDependency)
    container.register(DeleteDependency)

    container.register(CreateFolderDep)
    container.register(UpdateFolderDep)

    return container
