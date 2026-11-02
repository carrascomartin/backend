# 🧩 Módulo 03.5 — Arquitectura Modular (Feature-Based / Screaming)

> **Anexo del Módulo 03.** No reemplaza al 03: lo complementa.
> El 03 te enseña a **separar en capas**. Este módulo te enseña a **elegir el eje**
> de partición: por capa técnica (horizontal) vs por feature (vertical), y a
> defender la decisión con un número, no con una opinión.

---

## ¿De qué se trata?

En el Módulo 03 construiste la API de Tareas en 3 capas: `controllers/`,
`services/`, `repositories/`. Todo lo HTTP del sistema en una carpeta, todo el
negocio en otra, todo el acceso a datos en otra. Eso es **Layered Architecture**
(Fowler, *PoEAA*) — partición **horizontal**.

Funciona… hasta que el sistema crece. Cuando agregás `projects`, tocás las 4
carpetas. Cuando un segundo equipo entra, pisan archivos. El **otro eje**
posible es **partición vertical por feature**: `tasks/`, `projects/`, cada una
con sus 3 capas adentro. Y **Screaming Architecture** es el criterio de nombres:
el árbol de arriba tiene que gritar el **dominio**, no el framework.

Este módulo te hace construir **las dos** versiones del mismo sistema y medir
cuál cuesta menos cuando crece. Y te deja un **test que corre sin base de datos**
— la prueba de que la promesa "se puede testear cada capa por separado" del 03
es verdad o era solo discurso.

---

## Estructura

```
03.5-arquitectura-modular/
├── README.md
├── SPEC.md
├── MATERIAL_PREVIO.md
├── GUIA_ALUMNO.md
├── GUIA_DOCENTE.md
├── PRESENTACION.md
├── backend/            # V1 — scaffold LAYERED (por capa), con 2 features, stubs
├── solucion/           # V2 — solución FEATURE-BASED + tests sin base
└── postman/
```

- **`backend/`** = el punto de partida del taller (V1, por capa, 2 features).
- **`solucion/`** = la V2 (por feature) + tests. Se libera al final.

---

## Cómo empezar

```bash
cd 03.5-arquitectura-modular/backend
cp .env.example .env
uv sync
uv run -m app.main          # http://localhost:8000
```

La solución (V2) y los tests:

```bash
cd 03.5-arquitectura-modular/solucion
uv sync --extra dev
uv run pytest               # 12 tests, sin base de datos
uv run -m app.main          # http://localhost:8000
```

---

## La lección en una frase

> **"Capas" es un eje. "Features" es el otro. La arquitectura es elegir el eje
> correcto para el tamaño del dominio y del equipo — y saber qué cuesta cada uno.**

*"La Universidad te da el mapa. El recorrido lo hacés vos."*
