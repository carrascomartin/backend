"""Controller Project (HTTP)."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.shared.db import get_session
from app.projects.schemas import ProjectCreate, ProjectRead, ProjectUpdate
from app.projects.service import ProjectService
from app.projects.repository import SqlModelProjectRepository

router = APIRouter(prefix="/api/projects", tags=["projects"])


def get_project_service(session=Depends(get_session)) -> ProjectService:
    return ProjectService(SqlModelProjectRepository(session))


@router.get("", response_model=list[ProjectRead])
def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    project = service.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail=f"Proyecto {project_id} no encontrado")
    return project


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(body: ProjectCreate, service: ProjectService = Depends(get_project_service)):
    return service.create_project(body)


@router.patch("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, body: ProjectUpdate, service: ProjectService = Depends(get_project_service)):
    project = service.update_project(project_id, body)
    if project is None:
        raise HTTPException(status_code=404, detail=f"Proyecto {project_id} no encontrado")
    return project


@router.delete("/{project_id}")
def delete_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    if not service.delete_project(project_id):
        raise HTTPException(status_code=404, detail=f"Proyecto {project_id} no encontrado")
    return {"ok": True}
