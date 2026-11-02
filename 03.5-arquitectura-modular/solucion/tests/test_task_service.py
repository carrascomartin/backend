"""Tests del service de Task: corren SIN base de datos."""

from app.tasks.schemas import TaskCreate, TaskUpdate
from app.tasks.service import TaskService
from tests.fakes import FakeTaskRepository


def test_create_normaliza_titulo():
    svc = TaskService(FakeTaskRepository())
    task = svc.create_task(TaskCreate(title="  hola  "))
    assert task.title == "hola"


def test_list_vacio():
    svc = TaskService(FakeTaskRepository())
    assert svc.list_tasks() == []


def test_get_inexistente_devuelve_none():
    svc = TaskService(FakeTaskRepository())
    assert svc.get_task(999) is None


def test_update_parcial_no_pisa_title():
    svc = TaskService(FakeTaskRepository())
    t = svc.create_task(TaskCreate(title="original"))
    upd = svc.update_task(t.id, TaskUpdate(completed=True))
    assert upd.title == "original"
    assert upd.completed is True


def test_update_inexistente_devuelve_none():
    svc = TaskService(FakeTaskRepository())
    assert svc.update_task(999, TaskUpdate(completed=True)) is None


def test_delete_inexistente_devuelve_false():
    svc = TaskService(FakeTaskRepository())
    assert svc.delete_task(999) is False


def test_delete_existente():
    svc = TaskService(FakeTaskRepository())
    t = svc.create_task(TaskCreate(title="a borrar"))
    assert svc.delete_task(t.id) is True
    assert svc.get_task(t.id) is None
