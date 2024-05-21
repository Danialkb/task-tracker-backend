from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from folders.schemas import CreateFolder, UpdateFolder
from utils.repository import AbcRepository


class CreateFolderDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, folder: CreateFolder, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(folder)


class UpdateFolderDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, id: int, folder: UpdateFolder, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, folder)
