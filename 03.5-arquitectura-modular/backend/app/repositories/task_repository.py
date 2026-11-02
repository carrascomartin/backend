"""Repository Task (ORM). STUB: completá los métodos."""

from sqlmodel import Session, select

from app.models.task import Task, TaskUpdate


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_all(self) -> list[Task]:
        raise NotImplementedError("TODO")

    def get_by_id(self, task_id: int) -> Task | None:
        raise NotImplementedError("TODO")

    def create(self, title: str, project_id: int | None = None) -> Task:
        raise NotImplementedError("TODO")

    def update(self, task: Task, data: TaskUpdate) -> Task:
        raise NotImplementedError("TODO")

    def delete(self, task: Task) -> None:
        raise NotImplementedError("TODO")

    def count(self) -> int:
        from sqlalchemy import func
        statement = select(func.count()).select_from(Task)
        return self.session.exec(statement).one()
