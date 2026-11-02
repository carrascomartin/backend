# Guía del Alumno — 03.5 Arquitectura Modular (taller por grupos)

> **Modalidad**: taller por grupos con descubrimiento. **60 minutos.**
> Ya leíste el `MATERIAL_PREVIO.md`. Ahora a construir.

## Cómo funciona este taller

1. Tu fork trae el scaffold **V1 (por capa)** con 2 features y stubs.
2. Tu grupo completa el CRUD de ambos recursos en V1 (capas).
3. Después **reorganizás** `app/` a V2 (por feature) y comparás.
4. Corrés los tests de la solución y verificás que pasan **sin base**.

**Roles**: Piloto (escribe), Navegante (lee consignas), Investigador (busca en la doc).

---

## Fase 0 — Setup (5 min)

```bash
cd 03.5-arquitectura-modular/backend
cp .env.example .env
uv sync
uv run -m app.main        # :8000
curl http://localhost:8000/api/health
```

## Fase 1 — V1 por capa: completar CRUD (20 min)

Completá los stubs en `backend/app/`:

- `repositories/task_repository.py` y `project_repository.py`
- `services/task_service.py` y `project_service.py`
- `controllers/task_controller.py` y `project_controller.py`

Mismo patrón que el Módulo 03, pero **dos features**. Verificá con Swagger
(`http://localhost:8000/docs`): CRUD de tasks y projects.

## Fase 2 — El test del cambio (15 min)

1. Agregá una tercera feature `billing` (solo el esqueleto: model + repo + service + controller + ruta).
2. Contá cuántos archivos y carpetas tocás.
3. Ahora **reorganizá** `app/` a V2 (por feature): cada feature en su carpeta con
   sus 4 archivos, y un `shared/` con la base.
4. Contá de nuevo. ¿Cuántos archivos tocás ahora para agregar `billing`?

Anotá los dos números. Esa es la métrica que decide.

## Fase 3 — Hexagonal: el puerto (10 min)

En V2, hacé que `TaskService` dependa de un `Protocol` (`TaskRepository`) en
lugar de `SqlModelTaskRepository`. Creá un fake in-memory que implemente el
protocolo y corré un test del service **sin base**.

Mirá la solución (`solucion/`) para ver cómo queda: `app/tasks/ports.py`,
`tests/fakes.py`, `tests/test_task_service.py`.

## Fase 4 — Verificación (10 min)

```bash
cd ../solucion
uv sync --extra dev
uv run pytest            # 12 passed, sin base
```

Preparate para responder:

1. ¿Qué es partición horizontal y qué es vertical?
2. ¿Por qué "por feature" no elimina las capas?
3. ¿Qué mide el test del cambio?
4. ¿Qué diferencia hay entre "capas" y "hexagonal"?
5. ¿Qué es un `Protocol` y para qué sirve en tests?
6. **¿Cuándo elegirías cada eje?** (la pregunta que vale la nota)

---

## 🔐 La solución

> **Si trabajás en un fork**, la carpeta `solucion/` llega cuando sincronizás
> tu fork con la cátedra (`upstream`). Si nunca agregaste `upstream`:
>
> ```bash
> git remote add upstream https://github.com/desasoftfrlptn/backend.git
> git fetch upstream
> git checkout main
> git merge upstream/main
> git push origin main
> ```
>
> Después de eso, `solucion/` aparece en tu repo y podés comparar.



La solución completa (V2 por feature + tests) está en `solucion/`. Comparala con
tu reorganización. La gracia está en haberla hecho vos primero.

> *"La Universidad te da el mapa. El recorrido lo hacés vos."*
