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
  section.smaller { font-size: 0.95em; }
  section.smaller h1 { font-size: 1.45em; }
  section.smaller h2 { font-size: 1.2em; }
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
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  pre code { background: none; padding: 0; color: #e2e8f0; }
  table {
    display: table;
    font-size: 0.85em;
    background: #1e293b;
    border-radius: 8px;
    overflow: hidden;
    border-collapse: collapse;
    width: 100%;
  }
  thead { background: #334155; }
  th { color: #93c5fd; padding: 5px 10px; text-align: left; border-bottom: 2px solid #3b82f6; background: #334155; }
  td { color: #cbd5e1; padding: 5px 10px; border-bottom: 1px solid #334155; background: #1e293b; }
  tr:hover td { background: #263348; }
  blockquote { border-left: 4px solid #3b82f6; background: #1e293b; padding: 8px 14px; border-radius: 0 8px 8px 0; margin: 8px 0; }
  blockquote p { color: #94a3b8; font-style: italic; }
  ul { list-style-type: none; padding-left: 0; }
  ul li::before { content: "▸ "; color: #93c5fd; font-weight: bold; }
  ul li { color: #cbd5e1; line-height: 1.5; }
  ol li { color: #cbd5e1; line-height: 1.5; }
  section.lead h1 { font-size: 2.2em; }
  section.lead p { color: #94a3b8; }
  footer { color: #64748b; font-size: 0.65em; }
---

<!-- _class: lead -->
<!-- note: |
  Bienvenida al anexo 03.5. Hoy NO construimos una API nueva: reorganizamos
  la del 03 para entender por qué elegimos un layout y no otro.
  Recordar: este módulo es ANEXO. Si alguien no hizo el 03, enviarlo a leer
  el MATERIAL_PREVIO del 03 antes.
  Timing: apertura 0-2 min
-->

# Arquitectura Modular

### Módulo 03.5 — Desarrollo de Software 2026

Hoy no aprendés un layout. **Aprendés a elegir uno.**

---

<!-- note: |
  Objetivos medibles. Decirlos en voz alta. Son la promesa del taller:
  al final, cada alumno tiene que poder tildar los 4.
  Timing: apertura 2-4 min
-->

## Objetivos

1. Conocer los **dos ejes** de partición: por capa (horizontal) vs por feature (vertical).
2. **Medir** el costo de agregar una feature en cada layout (el test del cambio).
3. Entender **Screaming Architecture** y **Hexagonal** como escalones siguientes.
4. Probar la promesa del Módulo 03: testear el negocio **sin base de datos**.

> Cuatro objetivos, 60 minutos de actividad. Los construís vos en grupo.

---

<!-- note: |
  Activar con una pregunta al aire: "¿cuántos archivos tocaron para agregar
  `projects` en el 03?". Esperar respuestas. La respuesta es 4 carpetas.
  Eso es el gancho del problema.
  Timing: apertura 4-7 min
-->

## El problema: cuando el sistema crece

En el Módulo 03 construiste 3 capas. Funcionaba… hasta que agregaste `projects`.
Para agregar `projects` en el layout por capa tuviste que tocar:

- `models/` → nuevo modelo
- `repositories/` → nuevo repository
- `services/` → nuevo service
- `controllers/` → nuevo controller

**4 carpetas por cada feature nueva.** Y si dos equipos trabajan en paralelo,
pisan los mismos archivos.

> El costo no es el número de archivos: es la **localidad del cambio**. Cuanto
> más disperso, más conflictos de merge y más miedo a tocar.

---

<!-- note: |
  Mostrar los dos árboles lado a lado. Preguntar: "¿qué cambia?".
  Respuesta clave: NO desaparecen las capas. Cambia el eje de agrupación.
  Si alguien dice "en V2 ya no hay capas", corregirlo: cada feature tiene
  adentro controller, service y repository.
  Timing: apertura 7-10 min
-->

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

<!-- note: |
  LA slide del módulo. Dejarla visible y pedir que anoten los números.
  La tabla es la métrica que decide: no es opinión, es conteo.
  Preguntar: "¿cuántos archivos tocás para agregar `billing` en V1? ¿y en V2?".
  Timing: apertura 10-13 min (fin de apertura)
-->

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

<!-- note: |
  Activar: "¿qué grita el árbol de su proyecto actual?".
  Respuesta esperada: framework (routers, models, utils). El objetivo es que
  grite el dominio. Conectar con el Módulo 03: ahí el árbol gritaba capas.
  Timing: actividad 13-15 min (transición)
-->

## Screaming Architecture

El árbol de arriba tiene que gritar el **dominio**, no el framework.

```
# Grita FRAMEWORK (mal)
app/  routers/  models/  utils/

# Grita DOMINIO (bien)
app/  tasks/  projects/  billing/  shared/
```

Si mañana cambiás FastAPI por Django, el árbol del dominio no debería moverse.

> Robert C. Martin: la estructura tiene que gritar los **casos de uso del
> negocio**, no el framework con el que lo implementaste.

---

<!-- note: |
  El escalón siguiente. Mostrar el código del puerto (Protocol) y el fake.
  La pregunta clave: "¿por qué esto permite testear sin base?".
  Respuesta: porque el service no conoce la clase concreta, solo el contrato.
  Timing: actividad 15-18 min
-->

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

> La diferencia exacta entre "capas" y "hexagonal": el service depende de una
> abstracción, no de una clase concreta. `Depends()` ya era IoC; esto es IoC
> contra un contrato.

---

<!-- note: |
  El plan de la actividad. Fijar expectativas: 60 min de sprint.
  Recordar roles rotativos (piloto/navegante/investigador).
  Timing: actividad 18-20 min (fin apertura)
-->

## El plan — 60 min

| Min | Fase | Qué construyen |
|-----|------|----------------|
| 0-5 | Setup | Levantar V1 |
| 5-25 | V1 por capa | CRUD de tasks y projects |
| 25-40 | Test del cambio | Agregar billing + reorganizar a V2 |
| 40-50 | Hexagonal | Puerto + fake + test sin base |
| 50-60 | Cierre | Reflexión + descubrimientos |

> **Regla del taller**: el docente NO da respuestas. Hace preguntas.
> *"¿Cuántos archivos tocás?"* es la pregunta que lo destraba todo.

---

<!-- note: |
  Explicar el flujo de trabajo antes del setup.
  Cada alumno trabaja en SU fork. La solución se libera al final en solucion/.
  Timing: actividad 0-1 min (transición)
-->

## El plan: fork → clonar → desarrollar

```bash
git clone https://github.com/TU_USUARIO/backend.git
cd backend/03.5-arquitectura-modular
```

La solución (V2 + tests) se libera al final en `solucion/`.

> Si trabajás en un fork, sincronizalo primero:
> `git fetch upstream && git merge upstream/main`.

---

<!-- _class: lead -->
<!-- note: |
  Reflexión final. Preguntas al aire (5 min). Cerrar con la frase.
  Anunciar los ejercicios de cierre (en GUIA_DOCENTE/GUIA_ALUMNO).
  Timing: actividad 50-60 min
-->

## Capas es un eje. Features es el otro.

### La arquitectura es elegir el eje correcto — y saber qué cuesta cada uno.

> *"La Universidad te da el mapa. El recorrido lo hacés vos."*
