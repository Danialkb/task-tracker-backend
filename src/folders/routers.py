from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from folders.dependencies import CreateFolderDep, UpdateFolderDep
from folders.repository import FolderRepo
from utils.container import get_container
from utils.dependencies import ListDependency, RetrieveDependency, DeleteDependency

router = APIRouter(prefix="/folder", tags=["Folders"])

router.add_api_route(
    "/", get_container(FolderRepo).resolve(CreateFolderDep),
    methods=["POST"], name="create_folder",
)

router.add_api_route(
    "/", get_container(FolderRepo).resolve(ListDependency),
    methods=["GET"], name="list_folders",
)

router.add_api_route(
    "/{id}", get_container(FolderRepo).resolve(RetrieveDependency),
    methods=["GET"], name="retrieve_folder",
)

router.add_api_route(
    "/{id}", get_container(FolderRepo).resolve(UpdateFolderDep),
    methods=["PUT"], name="update_folder",
)

router.add_api_route(
    "/{id}", get_container(FolderRepo).resolve(DeleteDependency),
    methods=["DELETE"], name="delete_folder",
)


@router.get("/{id}/list_children/")
async def list_children(id: int, session: Session = Depends(get_db)):
    return FolderRepo(session).list_folder_children(parent_folder_id=id)
