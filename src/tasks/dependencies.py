from fastapi import Depends
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session

from database import get_db
from tasks.filters import TaskFilter
from tasks.schemas import CreateTask, UpdateTask, UpdateTaskFinishedDate, UpdateTaskStartedDate
from utils.dependencies import BaseDependency


class TaskFilterListDep(BaseDependency):
    def __call__(self, session: Session = Depends(get_db), task_filter: TaskFilter = FilterDepends(TaskFilter)):
        self.repo.session = session
        return self.repo.list(task_filter)


class CreateTaskDep(BaseDependency):
    def __call__(self, task: CreateTask, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.create(task)


class UpdateTaskDep(BaseDependency):
    def __call__(self, id: int, task: UpdateTask, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, task)


class UpdateStartedTaskDep(BaseDependency):
    def __call__(self, id: int, task: UpdateTaskStartedDate, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, task)


class UpdateFinishedTaskDep(BaseDependency):
    def __call__(self, id: int, task: UpdateTaskFinishedDate, session: Session = Depends(get_db)):
        self.repo.session = session
        return self.repo.update(id, task)
