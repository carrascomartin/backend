# 📖 Material Previo — 03.5 Arquitectura Modular

> **Leé esto ANTES de la clase.** La clase es un taller: si no venís con esto
> leído, no vas a poder construir.

## 1. Capas vs features (los dos ejes)

**Partición HORIZONTAL — por capa técnica** (lo que hiciste en el 03):

```
app/
├── controllers/   ← TODO lo HTTP
├── services/      ← TODO el negocio
├── repositories/  ← TODO el acceso a datos
└── models/        ← TODO el vocabulario
```

**Partición VERTICAL — por feature** (package by feature):

```
app/
├── tasks/
│   ├── controller.py
│   ├── service.py
│   ├── repository.py
│   ├── schemas.py
│   └── ports.py
├── projects/
│   └── ...
└── shared/          ← db, config: el kernel
```

Por feature **no desaparecen las capas**: cada feature tiene adentro su
controller, service y repository. Cambia el **eje de agrupación**, no la
cantidad de capas.

## 2. El test del cambio

El mejor argumento no es teórico, es medible:

> **Agregá una segunda feature y contá cuántos archivos y carpetas tocás en
> cada layout.**

- Por capa: tocás 4 carpetas (una por capa) por cada feature nueva.
- Por feature: tocás 1 carpeta (la feature nueva).

## 3. Screaming Architecture

Robert C. Martin: la estructura tiene que gritar los **casos de uso del
negocio**, no el framework. Si mañana cambiás FastAPI por Django, el árbol del
dominio no debería moverse.

## 4. Puertos y adaptadores (hexagonal)

En el 03 el service depende de una **clase concreta** (`TaskRepository`). En
hexagonal depende de una **interfaz** (puerto) y el repositorio es un
**adaptador** que la implementa. Esa es la diferencia exacta entre "capas" y
"hexagonal" — y es lo que permite testear el negocio **sin base de datos**.

## 5. `Protocol` en Python

`typing.Protocol` define una interfaz estructural: cualquier clase que tenga
los métodos correctos "cumple" el protocolo, sin heredar de nada. Así el
service depende del puerto y el fake in-memory lo satisface automáticamente.

## Autoevaluación

1. ¿Qué es partición horizontal y qué es partición vertical?
2. ¿Por qué "por feature" no elimina las capas?
3. ¿Qué es el test del cambio y qué mide?
4. ¿Qué diferencia hay entre "capas" y "hexagonal"?
5. ¿Qué es un `Protocol` y para qué sirve en tests?

## Bibliografía

- Martin Fowler — *Patterns of Enterprise Application Architecture* (Layered Architecture).
- [Package by feature, not by layer](https://phauer.com/2021/package-by-feature/) — Philip Hauer.
- [Screaming Architecture (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html).
- [Hexagonal Architecture (Alistair Cockburn)](https://alistair.cockburn.us/hexagonal-architecture/).
- [typing.Protocol (PEP 544)](https://peps.python.org/pep-0544/).
