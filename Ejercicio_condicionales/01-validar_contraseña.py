"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

CONTRASENA = "CONTRASEÑA"

# Se le pregunta al usuario por la contraseña

contrasena = input("Favor de introducir la contraseña: ")

if contrasena.upper() == CONTRASENA:
    print("En hora buena, la contraseña es: ", contrasena)
else:
    print("La contraseña ingresada no coincide con la del sistema.")
