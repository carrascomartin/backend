"""Tests del service de Project: corren SIN base de datos."""

from app.projects.schemas import ProjectCreate, ProjectUpdate
from app.projects.service import ProjectService
from tests.fakes import FakeProjectRepository


def test_create_normaliza_nombre():
    svc = ProjectService(FakeProjectRepository())
    p = svc.create_project(ProjectCreate(name="  backend  "))
    assert p.name == "backend"


def test_list_vacio():
    svc = ProjectService(FakeProjectRepository())
    assert svc.list_projects() == []


def test_get_inexistente_devuelve_none():
    svc = ProjectService(FakeProjectRepository())
    assert svc.get_project(999) is None


def test_update_parcial_no_pisa_name():
    svc = ProjectService(FakeProjectRepository())
    p = svc.create_project(ProjectCreate(name="original"))
    upd = svc.update_project(p.id, ProjectUpdate(description="desc"))
    assert upd.name == "original"
    assert upd.description == "desc"


def test_delete_existente():
    svc = ProjectService(FakeProjectRepository())
    p = svc.create_project(ProjectCreate(name="a borrar"))
    assert svc.delete_project(p.id) is True
    assert svc.get_project(p.id) is None
