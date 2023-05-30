"""
Escribir un programa que pida al usuario un número entero y muestre por 
pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""

# Se le piden los datos al usuario

numero_entero = int(input("Ingrese un numero entero positivo: "))

if numero_entero > 0:
    simbolo = ""
    for i in range(0, numero_entero):
        print(f"*{simbolo}")
        simbolo = simbolo + "*"
else:
    print("Favor de ingresar un numero entero positivo.")
