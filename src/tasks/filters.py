from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from tasks.models import Task


class TaskFilter(Filter):
    folder_id: Optional[int] = None
    title__ilike: Optional[str] = None
    created_at_gte: Optional[datetime] = None
    created_at_lte: Optional[datetime] = None
    status_id: Optional[int] = None

    class Constants(Filter.Constants):
        model = Task
