"""Schemas del feature projects (ORM + DTOs)."""

from datetime import datetime

from pydantic import field_validator
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class ProjectBase(SQLModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class Project(ProjectBase, table=True):
    __tablename__ = "projects"

    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )


class ProjectCreate(ProjectBase):
    @field_validator("name")
    @classmethod
    def name_no_vacio(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        return value


class ProjectUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = None

    @field_validator("name")
    @classmethod
    def name_no_vacio(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        return value


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime
