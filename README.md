# EID de Cálculo · Grupo 5

Animación con Manim sobre acumulación a partir de una tasa variable, usando una descarga simulada de GTA VI.

## Primer bloque: introducción

La escena presenta una transferencia supuesta de **150 GB**, un plan de **600 Mbps** y la diferencia entre megabits y megabytes. 600 Mbps equivalen a un máximo teórico de **75 MB/s**; las velocidades del modelo (20 a 50 MB/s) son simuladas y no garantizadas por el plan.

Los **150 GB son un tamaño hipotético para el ejercicio, no un dato oficial** ni una descarga real medida. La gráfica y el panel de descarga están disponibles en la escena `TasaVariable`. Los rectángulos y sus aportes están disponibles en `AportesDescarga`; el refinamiento y la explicación de la integral se implementarán en el siguiente bloque.

## Instalación en macOS

Requisitos: Python 3.12 o posterior, `uv`, Homebrew y MacTeX (LaTeX y dvisvgm).

Desde la carpeta del repositorio:

```sh
brew install cairo pkg-config
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
```

## Generar el video

```sh
source .venv/bin/activate
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
manim -pql descarga_gta.py IntroduccionDescarga
```

`-p` abre el resultado y `-ql` genera una vista previa a 480p. Para 1080p, reemplaza `-pql` por `-pqh`.

El video de prueba se guarda en `media/videos/descarga_gta/480p15/IntroduccionDescarga.mp4`. La carpeta `media/` y el entorno `.venv/` no se suben a Git.

## Fuentes y diseño

- [AT&T: velocidades y limitaciones de descarga](https://www.att.com/blog/download-speed-vs-upload-speed/).
- [Instalación oficial de Manim](https://docs.manim.community/en/stable/installation/uv.html).
- [Diseño matemático y visual](docs/diseno-manim.md).
- [Plan por bloques](docs/plan-implementacion.md).

## Segundo bloque: tasa variable y descarga

```sh
manim -pql descarga_gta.py TasaVariable
```

Escena de 29 segundos con gráfica, punto móvil, tiempo en minutos, velocidad en MB/s, GB acumulados y porcentaje. El eje horizontal de la gráfica usa segundos. Todo se sincroniza con un único reloj; la simulación comprime unos 71 minutos y 26 segundos en 18 segundos de animación.

El modelo está separado en `modelo_descarga.py`: r(t) = 20 + 0.007t MB/s, A(t) = 20t + 0.0035t² MB. Al finalizar, t = 30000/7 s, r(t) = 50 MB/s y A(t) = 150000 MB. El tiempo mostrado en el panel está redondeado a una décima de minuto.

Pruebas matemáticas (no requieren Manim):

```sh
python -m unittest discover -s tests
```

## Tercer bloque: aportes y suma de rectángulos

```sh
manim -pql descarga_gta.py AportesDescarga
```

Escena de unos 33 segundos. Divide la descarga en cinco intervalos iguales de 6000/7 s (aproximadamente 857.14 s) y usa la tasa al inicio de cada intervalo. Los puntos amarillos identifican las muestras y cada rectángulo representa tasa × duración, en MB.

El primer aporte es aproximadamente 17142.86 MB, o 17.14 GB. La suma de los cinco aportes es aproximadamente 137.14 GB, inferior a los 150 GB del modelo porque la tasa es creciente y usamos extremos izquierdos. La función `aportes_izquierdos_mb(n)` permite calcular otras particiones sin redondear los valores intermedios; solo se redondean las cifras mostradas.

Las seis pruebas verifican el modelo, los cinco aportes, la mejora numérica para 5/10/20 intervalos y el rechazo de cantidades de intervalos inválidas. La animación del refinamiento queda para el bloque 4.
