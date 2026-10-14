"""Modelo idealizado: tiempo en segundos y datos en megabytes decimales.

Las funciones se usan en el intervalo 0 <= t <= DURACION_S.
150 GB es un supuesto didáctico, no un tamaño oficial de GTA VI.
"""

PLAN_MBPS = 600
TAMANO_GB = 150
TASA_INICIAL_MB_S = 20
TASA_FINAL_MB_S = 50
DURACION_S = TAMANO_GB * 1000 / ((TASA_INICIAL_MB_S + TASA_FINAL_MB_S) / 2)
PENDIENTE_MB_S2 = (TASA_FINAL_MB_S - TASA_INICIAL_MB_S) / DURACION_S


def tasa_mb_s(t: float) -> float:
    """Velocidad de descarga en MB/s, diferente de los Mbps del plan."""
    return TASA_INICIAL_MB_S + PENDIENTE_MB_S2 * t


def datos_mb(t: float) -> float:
    """Datos acumulados desde t=0, en MB (antiderivada de la tasa)."""
    return TASA_INICIAL_MB_S * t + PENDIENTE_MB_S2 * t**2 / 2


def aportes_izquierdos_mb(n: int) -> list[float]:
    """Aportes en MB usando n intervalos iguales y su extremo izquierdo."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo")
    dt = DURACION_S / n
    return [tasa_mb_s(i * dt) * dt for i in range(n)]
