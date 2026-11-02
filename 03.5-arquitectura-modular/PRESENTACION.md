---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #e2e8f0
style: |
  /* ---- Base ---- */
  section {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    padding: 36px 56px;
    background-color: #0f172a;
    color: #e2e8f0;
  }
  h1 { color: #f8fafc; font-size: 1.55em; }
  h2 { color: #f1f5f9; font-size: 1.25em; }
  h3 { color: #94a3b8; font-size: 1em; }
  h4 { color: #93c5fd; }
  strong { color: #f1f5f9; }
  em { color: #cbd5e1; }
  a { color: #93c5fd; }

  /* ---- Slides densas: un escalón SUAVE (0.95, no 0.92) ----
     Ojo: `smaller` se multiplica con pre/table. Antes
     0.92 x 0.82 x 29px = 21.9px de código -> chico en proyector. */
  section.smaller { font-size: 0.95em; }
  section.smaller h1 { font-size: 1.45em; }
  section.smaller h2 { font-size: 1.2em; }

  /* ---- Código ---- */
  code {
    color: #93c5fd;
    background: #1e293b;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.88em;
  }
  pre {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 0.88em;
    line-height: 1.35;
    color: #e2e8f0;
    /* Red de seguridad: si una línea es muy larga se envuelve,
       nunca se recorta (el overflow de Marp corta el texto en silencio). */
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  pre code {
    background: none;
    padding: 0;
    color: #e2e8f0;
  }

  /* ---- Resaltado sintáctico (paleta clara sobre fondo oscuro) ---- */
  pre code :is(.hljs-keyword, .hljs-doctag, .hljs-template-tag, .hljs-template-variable, .hljs-variable.language_, .hljs-selector-tag) { color: #f472b6 !important; }
  pre code :is(.hljs-string, .hljs-regexp, .hljs-meta .hljs-string) { color: #86efac !important; }
  pre code :is(.hljs-title, .hljs-title.function_, .hljs-title.class_, .hljs-name, .hljs-quote, .hljs-selector-pseudo) { color: #7dd3fc !important; }
  pre code :is(.hljs-attr, .hljs-attribute, .hljs-literal, .hljs-meta, .hljs-selector-attr, .hljs-selector-class, .hljs-selector-id, .hljs-variable) { color: #93c5fd !important; }
  pre code :is(.hljs-number, .hljs-symbol) { color: #fcd34d !important; }
  pre code :is(.hljs-operator, .hljs-params, .hljs-subst, .hljs-type) { color: #cbd5e1 !important; }
  pre code :is(.hljs-comment, .hljs-code, .hljs-formula) { color: #94a3b8 !important; font-style: italic; }
  pre code :is(.hljs-section, .hljs-bullet) { color: #f0abfc !important; font-weight: 700; }
  pre code .hljs-built_in { color: #fca5a5 !important; }

  /* ---- Tablas ---- */
  table {
    /* Marp pone display:block + width:max-content: el fondo ocupa 100%
       pero las columnas no se estiran y queda un bloque muerto. */
    display: table;
    font-size: 0.85em;
    background: #1e293b;
    border-radius: 8px;
    overflow: hidden;
    border-collapse: collapse;
    width: 100%;
  }
  thead { background: #334155; }
  th {
    color: #93c5fd;
    padding: 5px 10px;
    text-align: left;
    border-bottom: 2px solid #3b82f6;
    background: #334155;
  }
  td {
    color: #cbd5e1;
    padding: 5px 10px;
    border-bottom: 1px solid #334155;
    background: #1e293b;
  }
  tr:hover td { background: #263348; }

  /* ---- Blockquote ---- */
  blockquote {
    border-left: 4px solid #3b82f6;
    background: #1e293b;
    padding: 8px 14px;
    border-radius: 0 8px 8px 0;
    margin: 8px 0;
  }
  blockquote p {
    color: #94a3b8;
    font-style: italic;
  }

  /* ---- Listas ---- */
  ul { list-style-type: none; padding-left: 0; }
  ul li::before { content: "▸ "; color: #93c5fd; font-weight: bold; }
  ul li { color: #cbd5e1; line-height: 1.5; }
  ol li { color: #cbd5e1; line-height: 1.5; }

  /* ---- Lead slides ---- */
  section.lead h1 { font-size: 2.2em; }
  section.lead p { color: #94a3b8; }

  /* ---- Checkpoint ---- */
  section.checkpoint {
    background-color: #052e16;
  }
  section.checkpoint h1 {
    color: #34d399;
    font-size: 1.7em;
  }
  section.checkpoint p, section.checkpoint li {
    color: #a7f3d0;
  }

  /* ---- Fase ---- */
  section.fase {
    background-color: #1e1b4b;
  }
  section.fase h1 { color: #c4b5fd; font-size: 1.7em; }
  section.fase h2 { color: #ddd6fe; }

  /* ---- Desbloqueo (errores comunes) ---- */
  section.desbloqueo {
    background-color: #2a1a1a;
  }
  section.desbloqueo h1 { color: #fca5a5; font-size: 1.6em; }

  /* ---- Checklists de checkpoint: el bullet ES el checkbox ----
     Marp NO convierte "- [ ]" en checkbox: lo deja como texto "[ ]",
     y encima el ::before de ul le agrega "▸ " -> se ve "▸ [ ]". */
  section.check ul li::before { content: "☐  "; color: #34d399; font-weight: 700; }

  /* ---- Footer ---- */
  footer { color: #64748b; font-size: 0.65em; }
---
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
