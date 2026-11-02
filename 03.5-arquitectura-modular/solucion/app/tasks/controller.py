"""Controller Task (HTTP)."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.shared.db import get_session
from app.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from app.tasks.service import TaskService
from app.tasks.repository import SqlModelTaskRepository

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


def get_task_service(session=Depends(get_session)) -> TaskService:
    return TaskService(SqlModelTaskRepository(session))


@router.get("", response_model=list[TaskRead])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Tarea {task_id} no encontrada")
    return task


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(body)


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, body: TaskUpdate, service: TaskService = Depends(get_task_service)):
    task = service.update_task(task_id, body)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Tarea {task_id} no encontrada")
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    if not service.delete_task(task_id):
        raise HTTPException(status_code=404, detail=f"Tarea {task_id} no encontrada")
    return {"ok": True}
