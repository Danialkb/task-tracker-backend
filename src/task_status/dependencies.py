from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from task_status.schemas import CreateTaskStatus, UpdateTaskStatus
from utils.repository import AbcRepository


class CreateTaskStatusDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, folder: CreateTaskStatus, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(folder)


class UpdateTaskStatusDep:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, id: int, folder: UpdateTaskStatus, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, folder)
