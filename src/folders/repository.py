import logging
from typing import Optional, List

from sqlalchemy import update, select, delete

from folders.schemas import UpdateFolder
from utils.repository import BaseRepository
from folders.models import Folder
from folders import schemas


class FolderRepo(BaseRepository):
    model = Folder
    action_schema = {
        "retrieve": schemas.Folder,
    }

    def list(self, filter_condition=None) -> List[schemas.Folder]:
        query = select(self.model).where(Folder.depth == 1)
        instances = self.session.execute(query).scalars().all()
        return [schemas.Folder.model_validate(instance) for instance in instances]

    def list_folder_children(self, parent_folder_id: int) -> List[Folder]:
        parent_folder = self.session.get(self.model, parent_folder_id)
        query = (
            select(self.model)
            .where((Folder.path.like(f"{parent_folder.path}/%")) & (Folder.depth == parent_folder.depth + 1))
        )
        folders = self.session.execute(query).scalars().all()
        return [schemas.Folder.model_validate(folder) for folder in folders]

    def update(self, instance_id: int, body: UpdateFolder) -> schemas.Folder:
        instance = self._get_object(instance_id)
        old_path = instance.path
        old_name = instance.name
        update_query = (
            update(Folder)
            .where(Folder.id == instance_id)
            .values(**body.model_dump())
        )
        folder = self.session.execute(update_query)
        self.session.commit()
        related_folders = self.session.execute(select(Folder).where(Folder.path.like(f"{old_path}%"))).scalars().all()
        for folder in related_folders:
            folder_names = folder.path[1:].split("/")
            try:
                folder_names[folder_names.index(old_name)] = body.name
                folder.path = f"/{'/'.join(folder_names)}"
            except ValueError:
                print(f"Can not update folder Folder({folder.id}, {folder.path}) with {old_name} -> {body.name}")

        self.session.bulk_save_objects(related_folders)
        self.session.commit()
        return schemas.Folder.model_validate(folder)

    def create(self, folder: schemas.CreateFolder) -> schemas.Folder:
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
        self.session.flush()
        self.session.refresh(folder_instance)
        self.session.commit()

        if folder.parent_path:
            update_query = (
                update(Folder)
                .where(Folder.name.in_(folder.parent_path[1:].split("/")))
                .values(is_leaf=False)
            )
            self.session.execute(update_query)
            self.session.commit()
        return schemas.Folder.model_validate(folder_instance)

    def delete(self, id: int) -> int:
        instance = self._get_object(id)
        if instance.is_leaf:
            self._update_leaf(instance)
        delete_query = delete(Folder).where((Folder.path.like(f"%{instance.path}/%")) | (Folder.id == id))
        self.session.execute(delete_query)
        self.session.commit()
        return id

    def _update_leaf(self, instance: Folder):
        path = f"/{'/'.join(instance.path[1:].split('/')[:-1])}"
        leafs_in_path = self.session.execute(
            select(Folder)
            .where(Folder.path.like(f"{path}/%"))
        ).scalars().all()
        if len(leafs_in_path) == 1:
            update_query = (
                update(Folder)
                .where(Folder.path == path)
                .values(is_leaf=True)
            )
            self.session.execute(update_query)
            self.session.commit()

    def _get_object(self, instance_id: int) -> Optional[Folder]:
        return self.session.get(Folder, instance_id)
