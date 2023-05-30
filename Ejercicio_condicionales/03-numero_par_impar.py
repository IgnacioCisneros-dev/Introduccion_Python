"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

# Se pide el numero entero al usuario

numero = int(input("Ingrese un numero entero: "))

if numero > 0:
    resultado = numero % 2
    if resultado == 0:
        # Se trata de un numero PAR
        print(f"El numero ingresado { numero} es un numero PAR.")
    else:
        # Se trata de un numero INPAR
        print(f"El numero ingresado {numero} es un numero IMPAR.")
else:
    print("El numero ingresado debe de ser un entero positivo, favor de intentar de nuevo.")
