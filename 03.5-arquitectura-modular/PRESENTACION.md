---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #e2e8f0
---

<!-- _class: lead -->

# Arquitectura Modular

### Módulo 03.5 — Desarrollo de Software 2026

Hoy no aprendés un layout. **Aprendés a elegir uno.**

---

## Objetivos

1. Conocer los **dos ejes** de partición: por capa (horizontal) vs por feature (vertical).
2. **Medir** el costo de agregar una feature en cada layout (el test del cambio).
3. Entender **Screaming Architecture** y **Hexagonal** como escalones siguientes.
4. Probar la promesa del Módulo 03: testear el negocio **sin base de datos**.

---

## El problema: cuando el sistema crece

En el Módulo 03 construiste 3 capas. Funcionaba… hasta que agregaste `projects`.
Para agregar `projects` en el layout por capa tuviste que tocar:

- `models/` → nuevo modelo
- `repositories/` → nuevo repository
- `services/` → nuevo service
- `controllers/` → nuevo controller

**4 carpetas por cada feature nueva.** Y si dos equipos trabajan en paralelo,
pisan los mismos archivos.

---

## Los dos ejes

**HORIZONTAL — por capa técnica** (V1, lo que ya tenés):

```
app/  controllers/  services/  repositories/  models/
```

**VERTICAL — por feature** (V2, lo que vas a construir):

```
app/  tasks/{controller,service,repository,schemas,ports}.py
      projects/{...}
      shared/   (db, config — el kernel)
```

> Por feature **no desaparecen las capas**. Cada feature tiene adentro su
> controller, service y repository. Cambia el **eje de agrupación**.

---

## El test del cambio

> **Agregá `billing` y contá cuántos archivos y carpetas tocás.**

| Pregunta | V1 (por capa) | V2 (por feature) |
|----------|---------------|------------------|
| Archivos/carpetas tocados | 4 | 1 |
| Conflictos de merge | altos | bajos |
| "¿Qué hace el sistema?" | hay que leer todo | el árbol lo grita |
| Reusar entre features | fácil | cuidado: `shared/` se vuelve basurero |

> No hay ganador universal. Dominio chico + un equipo → V1. Dominio que crece
> + varios equipos → V2 paga solo.

---

## Screaming Architecture

El árbol de arriba tiene que gritar el **dominio**, no el framework.

```
# Grita FRAMEWORK (mal)
app/  routers/  models/  utils/

# Grita DOMINIO (bien)
app/  tasks/  projects/  billing/  shared/
```

Si mañana cambiás FastAPI por Django, el árbol del dominio no debería moverse.

---

## Puertos y adaptadores (hexagonal)

En V1 el service depende de una **clase concreta** (`TaskRepository`).

En V2 depende de un `Protocol` (`TaskRepository`) y el repositorio concreto es
un **adaptador**.

```
class TaskService:
    def __init__(self, repository: TaskRepository):  # ← puerto (Protocol)
        self.repository = repository
```

Con el puerto podés inyectar un **fake in-memory** y testear el negocio **sin
base de datos**. Esa es la prueba de que la promesa del Módulo 03 era verdad.

---

## El plan — 60 min

| Min | Fase | Qué construyen |
|-----|------|----------------|
| 0-5 | Setup | Levantar V1 |
| 5-25 | V1 por capa | CRUD de tasks y projects |
| 25-40 | Test del cambio | Agregar billing + reorganizar a V2 |
| 40-50 | Hexagonal | Puerto + fake + test sin base |
| 50-60 | Cierre | Reflexión + descubrimientos |

---

## El plan: fork → clonar → desarrollar

```bash
git clone https://github.com/TU_USUARIO/backend.git
cd backend/03.5-arquitectura-modular
```

La solución (V2 + tests) se libera al final en `solucion/`.

---

<!-- _class: lead -->

## Capas es un eje. Features es el otro.

### La arquitectura es elegir el eje correcto — y saber qué cuesta cada uno.

> *"La Universidad te da el mapa. El recorrido lo hacés vos."*
