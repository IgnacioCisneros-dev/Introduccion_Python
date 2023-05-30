"""
Escribir un programa que pida al usuario dos números y muestre por pantalla
su división. Si el divisor es cero el programa debe mostrar un error.
"""

# Se le piden los datos al usuario

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


# Funcion que realizara la division

def calcular_division(numero_dividendo, numero_divisor):
    """Funcion que calcula una division

    Args:
        numero_dividendo (int): Numero dividendo
        numero_divisor (int): Numero divisor

    Returns:
        int : Regresa el resultado de la division
    """
    resultado = numero_dividendo / numero_divisor
    return resultado


# Se realizan validaciones

if numero1 < 0:
    print("El primer numero debe de ser un numero positivo.")
elif numero2 < 0:
    print("El segundo numero debe de ser un numero positivo.")
else:
    resultado_division = calcular_division(numero1, numero2)
    if resultado_division == 0:
        print("ERROR: El resultado de la division no debe de ser 0")
    else:
        print("Operacion exitosa, el resultado de la division es de: ",
              resultado_division)
