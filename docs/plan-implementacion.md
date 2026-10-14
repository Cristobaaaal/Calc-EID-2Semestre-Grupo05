# Plan de implementación: descarga GTA VI

> Ejecución: superpowers:executing-plans, por bloques. El usuario realiza cada commit.

**Objetivo:** visualizar acumulación desde una tasa variable mediante una descarga simulada.
**Arquitectura:** escenas independientes en `descarga_gta.py`; constantes compartidas, sin recursos externos.
**Tecnología:** Python 3.12+, Manim Community 0.22.0 y LaTeX.
**Diseño:** `docs/diseno-manim.md`.

## Restricciones

- Español; GB decimales y MB/s, tiempo matemático en segundos.
- Plan contratado de 600 Mbps: máximo teórico 75 MB/s.
- Descarga simulada de 150 GB, tamaño hipotético no oficial.
- Tasa idealizada 20 + 0.007t MB/s durante 30000/7 s.
- Detenerse en cada bloque; no hacer commits ni push.

## Revisión

Comprobar legibilidad, separación entre Mbps y MB/s, aclaración de los 150 GB, funcionamiento de LaTeX y ausencia de videos/entornos en Git.

## Bloque 1: introducción

- [x] Crear `.gitignore`, `requirements.txt` y `manim.cfg`.
- [x] Crear `IntroduccionDescarga(Scene)` en `descarga_gta.py`: contexto, conversión de unidades y pregunta central. Sin gráfica ni avance de descarga todavía.
- [x] Actualizar README con instalación, render y fuentes.
- [x] Renderizar con `manim -ql descarga_gta.py IntroduccionDescarga`, revisar fotogramas y `git diff --check`.
- [ ] Entregar al usuario para su commit y detenerse.

## Bloques siguientes (se ejecutarán tras los commits del usuario)

2. Añadir `TasaVariable`: r(t), gráfica y panel sincronizado; verificar extremos y 150 GB al final.
3. Añadir `AportesDescarga`: rectángulos izquierdos y unidades; verificar 137.142857, 143.571429 y 146.785714 GB (redondeados) con n = 5, 10 y 20.
4. Añadir `IntegralDescarga`: límite, cálculo y respuesta final; renderizar el conjunto y revisar continuidad.

## Estado del bloque 1

Render de 26 segundos completado con Manim 0.22.0 y LaTeX. Revisadas visualmente las tres pantallas; sin recortes ni superposiciones. `git diff --check` correcto. Se utilizó el entorno Manim ya instalado en el equipo para esta validación. Commit pendiente del usuario.
