# EID Grupo 5: descarga de GTA VI y acumulación

## Objetivo

Responder: ¿cómo una tasa que cambia con el tiempo produce una cantidad acumulada?
El video se construirá con Manim Community y explicaciones en español. Mostrará una descarga simulada inspirada en GTA VII, seguida por la interpretación de rectángulos, sumas de Riemann e integral.

## Tamaño hipotético del modelo

Para el ejercicio suponemos una transferencia de 150 GB de GTA VI. Es una elección didáctica, no un dato oficial ni una medición real del juego. La pantalla y la narración deben aclarar: «Tamaño hipotético para el ejercicio; no es un dato oficial».

Se emplean unidades decimales: 1 GB = 1000 MB. MB significa megabytes, no megabits.

## Modelo matemático

Para facilitar el cálculo y mostrar una tasa variable se propone un aumento gradual de velocidad. Es un modelo idealizado, no una medición ni una reproducción de las fluctuaciones de una red real.

- Tiempo t en segundos, entre 0 y T = 30000/7 ≈ 4285.714286.
- Tasa r(t) = 20 + 0.007 t, en MB/s (el coeficiente 0.007 tiene unidades MB/s²).
- Acumulación A(t) = integral desde 0 hasta t de r(u) du = 20t + 0.0035t², en MB.
- Cantidad inicial descargada: 0 MB.
- r(0) = 20 MB/s y r(T) = 50 MB/s.
- A(T) = 150000 MB = 150 GB: descarga completa aproximadamente a los 71 minutos y 26 segundos.

Para la gráfica se conserva el eje temporal en segundos; el panel de descarga puede mostrar el tiempo convertido a minutos. El video representa ese intervalo de forma acelerada.

Cada rectángulo tiene altura r(t_i*) en MB/s y ancho Δt en s. Su área representa una aproximación de los MB descargados durante ese intervalo. La suma aproxima los datos acumulados y la integral expresa el límite al refinar la partición.

Se utilizarán extremos izquierdos para mostrar la mejora de la aproximación: en esta tasa creciente las sumas subestiman el total. Con n = 5, 10 y 20 se obtienen 137.142857, 143.571429 y 146.785714 GB (valores redondeados), respectivamente, acercándose a 150 GB. Evitar usar puntos medios como demostración del error: para esta función lineal dan el resultado exacto desde la primera partición uniforme.

## Estructura visual y del código

Un archivo principal `descarga_gta.py` con escenas independientes para renderizar y revisar cada parte. Constantes compartidas para tamaño, duración y colores. Panel visual propio con título del juego, velocidad, cantidad descargada y barra de progreso; no necesita imágenes del juego ni descargarlo.

1. Introducción: contexto, pregunta central, tamaño de referencia y unidades.
2. Tasa variable: gráfica y panel de descarga sincronizados.
3. Aportes: destacar un intervalo y explicar tasa por duración.
4. Acumulación: sumar rectángulos y refinar la partición.
5. Integral: mostrar el total de 150 GB y responder la pregunta central.

La base incluirá `requirements.txt`, `.gitignore` para entorno y archivos generados, `manim.cfg` y README con instrucciones para macOS. Se usará Manim 0.22.0, ya probado en este equipo, y LaTeX para las fórmulas.

## Entregas pequeñas

0. Este diseño para revisión.
1. Configuración e introducción renderizable.
2. Gráfica de tasa y avance de descarga.
3. Rectángulos, unidades y sumas.
4. Refinamiento, integral y cierre.

Después de cada entrega se detiene el trabajo. El usuario realiza los commits. No se ejecutará git commit ni git push.

## Verificación

Cada escena se renderiza en baja calidad antes de entregarse y se revisa visualmente. Se comprueban los valores matemáticos, la correspondencia entre tiempo, cantidad y porcentaje, y que las unidades estén visibles. No se agregará infraestructura de pruebas innecesaria para las escenas de presentación.

## Ajuste aprobado: plan de internet

El contexto será un plan contratado de 600 Mbps. Como 8 bits equivalen a 1 byte, su máximo teórico equivale a 75 MB/s. En el ejemplo la descarga comienza a 20 MB/s y aumenta hasta 50 MB/s: son velocidades simuladas por debajo de ese máximo, no velocidades garantizadas ni una conversión de 600 Mbps a 20 MB/s. La conexión Wi-Fi, otros dispositivos y el servidor pueden limitar el rendimiento.

Referencia sobre velocidades y limitaciones:
https://www.att.com/blog/download-speed-vs-upload-speed/

Para comparar: 800 Mbps equivalen a un máximo teórico de 100 MB/s. El video usará solo el plan de 600 Mbps para evitar confusión.
