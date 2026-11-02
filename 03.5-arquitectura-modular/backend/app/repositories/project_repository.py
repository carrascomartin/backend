"""Repository Project (ORM). STUB: completá los métodos."""

from sqlmodel import Session, select

from app.models.project import Project, ProjectUpdate


class ProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_all(self) -> list[Project]:
        raise NotImplementedError("TODO")

    def get_by_id(self, project_id: int) -> Project | None:
        raise NotImplementedError("TODO")

    def create(self, name: str, description: str | None = None) -> Project:
        raise NotImplementedError("TODO")

    def update(self, project: Project, data: ProjectUpdate) -> Project:
        raise NotImplementedError("TODO")

    def delete(self, project: Project) -> None:
        raise NotImplementedError("TODO")

    def count(self) -> int:
        from sqlalchemy import func
        statement = select(func.count()).select_from(Project)
        return self.session.exec(statement).one()
