from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from tasks.schemas import CreateTask, UpdateTask
from utils.repository import AbcRepository


class CreateTaskDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, folder: CreateTask, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(folder)


class UpdateTaskDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, id: int, folder: UpdateTask, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, folder)
