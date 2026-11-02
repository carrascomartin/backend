"""Schemas del feature tasks (ORM + DTOs)."""

from datetime import datetime

from pydantic import field_validator
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    project_id: int | None = Field(default=None)


class Task(TaskBase, table=True):
    __tablename__ = "tasks"

    id: int | None = Field(default=None, primary_key=True)
    completed: bool = Field(default=False)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )


class TaskCreate(TaskBase):
    @field_validator("title")
    @classmethod
    def title_no_vacio(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("El título no puede estar vacío")
        return value


class TaskUpdate(SQLModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    completed: bool | None = None
    project_id: int | None = None

    @field_validator("title")
    @classmethod
    def title_no_vacio(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if not value.strip():
            raise ValueError("El título no puede estar vacío")
        return value


class TaskRead(TaskBase):
    id: int
    completed: bool
    created_at: datetime
