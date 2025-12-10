"""
Módulo: ejemplo.py
Descripción: Plantilla base para scripts en Python con buenas prácticas,
             clean code, docstrings y doctests.
"""

# ==========================
# Constantes globales
# ==========================
CONSTANTE_EJEMPLO = 42.0  # Explicación breve de la constante


# ==========================
# Funciones
# ==========================
def funcion_simple(x: float) -> float:
    """
    Ejemplo de función que multiplica un número por la constante.

    Args:
        x (float): Número de entrada.

    Returns:
        float: Resultado de la operación.

    Ejemplos:
        >>> funcion_simple(2)
        84.0
        >>> funcion_simple(0)
        0.0
    """
    return x * CONSTANTE_EJEMPLO


def validar_valores(valor: float):
    """
    Valida que el valor esté dentro de un rango permitido.

    Args:
        valor (float): Número a validar.

    Returns:
        bool: True si el valor es válido.

    Raises:
        ValueError: Si el valor está fuera de rango.

    Ejemplos:
        >>> validar_valores(10)
        True
        >>> validar_valores(-5)
        Traceback (most recent call last):
            ...
        ValueError: Valor fuera de rango
    """
    if not (0 <= valor <= 100):
        raise ValueError("Valor fuera de rango")
    return True


# ==========================
# Función principal
# ==========================
def main():
    """Ejecuta pruebas rápidas del script."""
    print("Prueba rápida:")
    print(f"funcion_simple(2) = {funcion_simple(2)}")
    print(f"validar_valores(10) = {validar_valores(10)}")


# ==========================
# Bloque de ejecución directa
# ==========================
if __name__ == "__main__":
    main()