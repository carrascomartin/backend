"""Controller Task (HTTP). STUB."""

from fastapi import APIRouter, Depends

from app.dependencies import get_task_service
from app.models.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskRead])
def list_tasks(service: TaskService = Depends(get_task_service)):
    raise NotImplementedError("TODO")
