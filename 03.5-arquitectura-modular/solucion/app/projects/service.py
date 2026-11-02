"""Service Project — depende del puerto."""

from app.projects.ports import ProjectRepository
from app.projects.schemas import Project, ProjectCreate, ProjectUpdate


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def list_projects(self) -> list[Project]:
        return self.repository.list_all()

    def get_project(self, project_id: int) -> Project | None:
        return self.repository.get_by_id(project_id)

    def create_project(self, body: ProjectCreate) -> Project:
        name = body.name.strip()
        return self.repository.create(name, body.description)

    def update_project(self, project_id: int, body: ProjectUpdate) -> Project | None:
        project = self.repository.get_by_id(project_id)
        if project is None:
            return None
        if body.name is not None:
            body = body.model_copy(update={"name": body.name.strip()})
        return self.repository.update(project, body)

    def delete_project(self, project_id: int) -> bool:
        project = self.repository.get_by_id(project_id)
        if project is None:
            return False
        self.repository.delete(project)
        return True

    def count_projects(self) -> int:
        return self.repository.count()
