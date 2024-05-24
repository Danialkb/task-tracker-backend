from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from database import Base


class AbcRepository(ABC):
    model: Base = None
    action_schema: dict[str, BaseModel] = {}
    session: Session = None

    def __init__(self, session=None):
        self.session = session

    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def retrieve(self, id: int):
        raise NotImplementedError()

    @abstractmethod
    def create(self, body: BaseModel):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError()

    @abstractmethod
    def update(self, id: int, body: BaseModel):
        raise NotImplementedError()

    def get_schema(self, action_key: str):
        schema = self.action_schema.get(action_key)
        if not schema:
            raise KeyError(f"No schema assigned for action {action_key}")
        return schema


class BaseRepository(AbcRepository):

    def list(self, filter_condition=None):
        query = select(self.model)
        instances = self.session.execute(query).scalars().all()
        schema: BaseModel = self.get_schema("list")
        return [schema.model_validate(instance) for instance in instances]

    def retrieve(self, id: int):
        instance = self.session.get(self.model, id)
        schema: BaseModel = self.get_schema("retrieve")
        return schema.model_validate(instance)

    def create(self, body: BaseModel):
        instance = self.model(**body.model_dump())
        self.session.add(instance)
        self.session.flush()
        self.session.refresh(instance)
        self.session.commit()

        schema: BaseModel = self.get_schema("create_response")
        return schema.model_validate(instance)

    def update(self, instance_id: int, body: BaseModel):
        update_query = (
            update(self.model)
            .where(self.model.id == instance_id)
            .values(**body.model_dump())
        )
        self.session.execute(update_query)
        self.session.commit()
        updated_instance = self.session.get(self.model, instance_id)
        return self.get_schema("update_response").model_validate(updated_instance)

    def delete(self, id: int):
        self.session.execute(delete(self.model).where(self.model.id == id))
        self.session.commit()
        return id
