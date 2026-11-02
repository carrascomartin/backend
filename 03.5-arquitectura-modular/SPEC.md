# 📘 SPEC — Módulo 03.5: Arquitectura Modular

> Anexo del Módulo 03. Leé `MATERIAL_PREVIO.md` antes de la clase.

## 1. Qué vas a construir

La misma API de Tareas + **Proyectos** del Módulo 03, pero con **dos features**
(`tasks` y `projects`), en **dos layouts** distintos:

- **V1 (scaffold, por capa)**: `controllers/`, `services/`, `repositories/`,
  `models/` — todo lo HTTP del sistema junto, todo el negocio junto, etc.
- **V2 (solución, por feature)**: `tasks/{controller,service,repository,schemas,ports}.py`
  y `projects/{...}`, más un `shared/` con la base.

Y una prueba: **12 tests que corren sin base de datos**, usando un `Protocol`
(puerto) y un fake in-memory. Esa es la prueba de que la promesa del Módulo 03
("se puede testear cada capa por separado") es verdad o era discurso.

## 2. El test del cambio (la métrica que decide)

Agregá una tercera feature (`billing`) y contá:

| Pregunta | V1 (por capa) | V2 (por feature) |
|----------|---------------|------------------|
| Archivos/carpetas tocados | 4 (una por capa) | 1 (la feature nueva) |
| Conflictos de merge con otro equipo | altos (archivos compartidos) | bajos (carpetas separadas) |
| "¿Qué hace el sistema?" | hay que leer todo | el árbol lo grita |
| Reusar entre features | fácil (ya separado) | cuidado: `shared/` se vuelve basurero |

> No hay ganador universal. Dominio chico + un equipo → V1. Dominio que crece +
> varios equipos → V2 paga solo.

## 3. Screaming Architecture

El árbol de arriba tiene que gritar el **dominio**, no el framework:

```
# Grita FRAMEWORK (mal)
app/  routers/  models/  utils/

# Grita DOMINIO (bien)
app/  tasks/  projects/  billing/  shared/
```

## 4. Puertos y adaptadores (el escalón siguiente)

En V1 el service depende de una **clase concreta** (`TaskRepository`). En V2
depende de un `Protocol` (`TaskRepository`). Esa diferencia es la línea entre
"capas" y "hexagonal": con el puerto podés inyectar un fake y testear el
negocio sin base.

## 5. Endpoints

Mismos que el Módulo 03, más los de `projects`:

| Recurso | Métodos |
|---------|---------|
| `/api/tasks` | GET, POST, GET/{id}, PATCH/{id}, DELETE/{id} |
| `/api/projects` | GET, POST, GET/{id}, PATCH/{id}, DELETE/{id} |
| `/api/health` | GET (cuenta tareas y proyectos) |

## 6. Cómo verificar

```bash
cd solucion
uv sync --extra dev
uv run pytest                  # 12 passed, sin base
uv run -m app.main             # http://localhost:8000
```

Checkpoints:

1. `pytest` pasa los 12 tests sin levantar Postgres.
2. `/api/health` responde con `tasks_count` y `projects_count`.
3. El CRUD de ambos recursos funciona por HTTP.

## 7. Dónde seguir

- `MATERIAL_PREVIO.md` §1-§4 (capas vs features, test del cambio, screaming, hexagonal)
- `GUIA_ALUMNO.md` (taller: reorganizar V1 → V2 y medir)
- `GUIA_DOCENTE.md`
