"""
Escribir un programa que lea un entero positivo, introducido por el usuario y 
después muestre en pantalla la suma de todos los enteros desde 1 hasta.
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
"""


# Leemos los datos de entrada del usuario

numero_entero_positivo = int(input("Ingrese un numero entero positivo: "))

if numero_entero_positivo < 0:
    print("El numero ingresado no es valido.")
else:
    suma = numero_entero_positivo * (numero_entero_positivo + 1) / 2
    print(
        f"La suma de los numeros enteros desde 1 hasta {numero_entero_positivo} es de : {suma}")
