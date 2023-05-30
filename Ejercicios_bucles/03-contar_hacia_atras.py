"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

# Se le pide el numero al usuario
numero = int(input("Ingresar el numero: "))

if numero < 0:
    print("Favor de ingresar un numero valido.")
else:
    for i in range(0, -numero, -1):
        print(i, end=", ")
