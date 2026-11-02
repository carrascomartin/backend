"""Health check."""

from fastapi import APIRouter, Depends

from app.dependencies import get_task_service, get_project_service
from app.services.task_service import TaskService
from app.services.project_service import ProjectService

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health_check(
    task_service: TaskService = Depends(get_task_service),
    project_service: ProjectService = Depends(get_project_service),
):
    return {
        "status": "Funciona",
        "service": "03.5-arquitectura-modular",
        "tasks_count": task_service.count_tasks(),
        "projects_count": project_service.count_projects(),
    }
