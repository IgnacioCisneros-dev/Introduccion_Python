"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la
<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

# Se le piden los datos al usuario

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

# Se define la funcion que realizara la division


def calcular_division(numero_uno, numero_dos):
    """Funcion que calcula una division

    Args:
        numero_uno (int): numero dividendo
        numero_dos (int): numero divisor

    Returns:
        int: Resultado de la division de numero_uno / numero_dos
    """
    resultado_division = numero_uno / numero_dos
    return resultado_division


# Se imprime el resultado


print(f"{numero1} entre {numero2} da un coeficiente de {calcular_division(numero1, numero2)}")
