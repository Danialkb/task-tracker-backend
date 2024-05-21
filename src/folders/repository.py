from pydantic import BaseModel
from sqlalchemy import update, select

from folders.schemas import UpdateFolder
from utils.repository import BaseRepository
from folders.models import Folder
from folders import schemas


class FolderRepo(BaseRepository):
    model = Folder
    action_schema = {
        "list": schemas.Folder,
        "retrieve": schemas.Folder,
        "update": schemas.UpdateFolder,
    }

    def list(self, filter_condition=None):
        query = select(self.model).where(Folder.depth == 1)
        instances = self.session.execute(query).scalars().all()
        return [schemas.Folder.model_validate(instance) for instance in instances]

    def list_folder_children(self, parent_folder_id: int):
        parent_folder = self.session.get(self.model, parent_folder_id)
        query = (
            select(self.model)
            .where((Folder.path.like(f"{parent_folder.path}%")) & (Folder.depth == parent_folder.depth + 1))
        )
        folders = self.session.execute(query).scalars().all()
        return [schemas.Folder.model_validate(folder) for folder in folders]

    def update(self, instance_id: int, body: UpdateFolder):
        instance = self.session.get(Folder, instance_id)
        old_path = instance.path
        update_query = (
            update(Folder)
            .where(Folder.id == id)
            .values(**body.model_dump())
        )
        self.session.execute(update_query)
        self.session.commit()
        "/".join(old_path.split("/").replace())


    def create(self, folder: schemas.CreateFolder):
        if folder.parent_path:
            folder_instance = Folder(
                name=folder.name,
                path=f"{folder.parent_path}/{folder.name}",
                is_leaf=True,
                depth=len(folder.parent_path.split("/")),
            )
        else:
            folder_instance = Folder(name=folder.name, path=f"/{folder.name}", is_leaf=True)

        self.session.add(folder_instance)
        self.session.commit()

        if folder.parent_path:
            update_query = (
                update(Folder)
                .where(Folder.name.in_(folder.parent_path[1:].split("/")))
                .values(is_leaf=False)
            )
            self.session.execute(update_query)
            self.session.commit()
        return folder
