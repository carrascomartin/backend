"""Controller Project (HTTP). STUB."""

from fastapi import APIRouter, Depends

from app.dependencies import get_project_service
from app.models.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("", response_model=list[ProjectRead])
def list_projects(service: ProjectService = Depends(get_project_service)):
    raise NotImplementedError("TODO")
