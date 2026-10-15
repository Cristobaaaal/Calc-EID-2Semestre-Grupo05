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
- [x] Entregar al usuario para su commit y detenerse.

## Bloques siguientes (se ejecutarán tras los commits del usuario)

2. Añadir `TasaVariable`: r(t), gráfica y panel sincronizado; verificar extremos y 150 GB al final.
3. Añadir `AportesDescarga`: rectángulos izquierdos y unidades; verificar 137.142857, 143.571429 y 146.785714 GB (redondeados) con n = 5, 10 y 20.
4. Añadir `IntegralDescarga`: límite, cálculo y respuesta final; renderizar el conjunto y revisar continuidad.

## Estado del bloque 1

Render de 26 segundos completado con Manim 0.22.0 y LaTeX. Revisadas visualmente las tres pantallas; sin recortes ni superposiciones. `git diff --check` correcto. Se utilizó el entorno Manim ya instalado en el equipo para esta validación. Commit del usuario: `8cc085b`.

## Estado del bloque 2

Implementada `TasaVariable` y separado el modelo en `modelo_descarga.py` para comprobarlo sin dependencias gráficas. Un solo ValueTracker sincroniza los indicadores y el punto de la gráfica. No se implementaron todavía los bloques 3 y 4.

Pruebas: inicio (0 MB, 20 MB/s), punto intermedio (23500 MB y 27 MB/s a los 1000 s) y final (150 GB, 50 MB/s, bajo el máximo teórico del plan). Render de 29 s, revisión visual al inicio, durante la descarga y al final. Porcentaje inicialmente centrado fuera del panel: corregido fijando su posición antes de la primera actualización. Commit del bloque 2 realizado por el usuario: `85c3264`.

## Estado del bloque 3

Implementada `AportesDescarga`: primer rectángulo, ancho temporal, muestra izquierda, unidades MB/s × s = MB y suma progresiva de cinco aportes. `aportes_izquierdos_mb(n)` comparte la partición numérica con el criterio de la visualización. El total 137.14 GB se compara con los 150 GB del modelo y se explica la subestimación.

Verificación: seis pruebas aprobadas, render de 32.73 s y revisión visual del primer aporte, una suma intermedia y el resultado. `git diff --check` sin errores. No se avanzó al bloque 4 ni se hicieron commits. Commit del usuario: `6ba4a35`.

## Bloque 4: refinamiento y cierre

Implementada `IntegralDescarga`: comparación de 5/10/20/40/80 rectángulos izquierdos, límite de las sumas, evaluación de la integral y respuesta a la pregunta central. `VideoCompleto` reúne las cuatro escenas y retira sus actualizadores entre transiciones. Se conserva la aclaración de que 150 GB es un supuesto no oficial.

Pruebas: siete comprobaciones matemáticas, incluida la reducción a la mitad del error al duplicar n en esta tasa lineal. Render final de 48.33 segundos y video completo de 137.87 segundos. Revisados fotogramas de las cuatro partes y las fórmulas finales; revisión independiente de código sin problemas importantes. `git diff --check` correcto. No hacer commits: corresponden al usuario.
