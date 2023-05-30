"""Ejercicio: Crear una funcion que calcule el volumen de una esfera pasandole el radio
    """


# Definicion de la funcion

def calcular_volumen_esfera(radio_espera):
    VALOR_PI = 3.1416
    volumen = (4/3) * VALOR_PI * radio_espera**3

    return volumen


# Se llama a la funcion

radio = 20
print(calcular_volumen_esfera(radio))
