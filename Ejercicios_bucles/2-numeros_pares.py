"""
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número 
separados por comas.
"""


# Se le piden los datos al usuario

numero = int(input("Ingrese un numero: "))


def buscar_numeros_impares(numero_entero):
    """Funcion que dado un numero evalua si es un numero entero positivo y 
    calcula sus numeros impares

    Args:
        numero_entero (int): Numero al cual se le calcularan sus numeros impares
    """
    if numero_entero > 0:
        for i in range(1, numero_entero + 1, 2):
            print(i, end=", ")
    else:
        print("Favor de ingresar un numero entero positivo.")


# Se llama a la funcion que calcula los numeros impares

buscar_numeros_impares(numero)
