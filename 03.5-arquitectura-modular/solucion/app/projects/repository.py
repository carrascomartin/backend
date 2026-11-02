"""Adaptador concreto: SQLModel."""

from sqlalchemy import func
from sqlmodel import Session, select

from app.projects.schemas import Project, ProjectUpdate


class SqlModelProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_all(self) -> list[Project]:
        statement = select(Project).order_by(Project.id)
        return list(self.session.exec(statement).all())

    def get_by_id(self, project_id: int) -> Project | None:
        return self.session.get(Project, project_id)

    def create(self, name: str, description: str | None = None) -> Project:
        project = Project(name=name.strip(), description=description)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project

    def update(self, project: Project, data: ProjectUpdate) -> Project:
        changes = data.model_dump(exclude_unset=True)
        for field, value in changes.items():
            setattr(project, field, value)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project

    def delete(self, project: Project) -> None:
        self.session.delete(project)
        self.session.commit()

    def count(self) -> int:
        statement = select(func.count()).select_from(Project)
        return self.session.exec(statement).one()
