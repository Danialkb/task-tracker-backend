from typing import List, Optional

from utils.schemas_config import BaseSchema


class BaseFolder(BaseSchema):
    id: int
    name: str


class CreateFolder(BaseSchema):
    name: str
    parent_path: Optional[str] = None


class UpdateFolder(BaseSchema):
    id: int
    name: str


class Folder(BaseFolder):
    depth: int
    is_leaf: bool
