"""
Programa para calcular el área de un círculo y un rectángulo.
Este programa utiliza diferentes tipos de datos y demuestra el uso de identificadores descriptivos.
"""

# Importar la librería math para usar el valor de pi
import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: El radio del círculo (float).
    :return: El área del círculo (float).
    """
    return math.pi * radio**2

def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo dado su ancho y alto.
    :param ancho: El ancho del rectángulo (float).
    :param alto: La altura del rectángulo (float).
    :return: El área del rectángulo (float).
    """
    return ancho * alto

# Variables para almacenar las dimensiones
radio_circulo = 5.5  # float
ancho_rectangulo = 10  # integer
alto_rectangulo = 7.5  # float

# Cálculos de las áreas
area_circulo = calcular_area_circulo(radio_circulo)
area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)

# Mostrar resultados
print(f"El área del círculo con radio {radio_circulo} es: {area_circulo:.2f}")
print(f"El área del rectángulo de {ancho_rectangulo}x{alto_rectangulo} es: {area_rectangulo:.2f}")
