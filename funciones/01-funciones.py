# Se define la funcion
def hola():
    print("Hola mundo desde una funcion.")


# De esta manera se manda a llamar a la funcion
hola()


# Parametros y argumentos para las funciones

def saludo(nombre):
    print("Hola mundo")
    print(f"Bienvenido {nombre}")


saludo("Ignacio")
saludo("Emir")

# Ejemplo con multiples parametros y argumentos


def bienvenida(nombre, apellido, edad):
    print(f"Bienvenido {nombre} {apellido}")
    print(f"Es un placer saber que tu edad es: {edad}")


bienvenida("Ignacio", "Cisneros", "25")


"""
Ejemplo con parametro opcionales, se puede declarar en la funcion el 
valor de parametro por defaul en caso de que en la llamada a la funcion
no se le pase ese parametro, en caso contrario, si en la llamada a la 
funcion si se le pasa el parametro, el valor asignado por default en la funcion sera
omitido
"""


def saludar(nombre, apellido="(sin apellido)"):
    print(f"Hola de nuevo {nombre} {apellido} un gusto saludarte de nuevo.")


saludar("Emir")
saludar("Emir", "Ignacio Cisneros")


# Argumentos nombrados

"""
Cuando no sabemos el orden que la funcion recibe los parametros,
podemos especificar el nombre al llamar la funcion de la siguiente manera
"""

saludar(apellido="Cisneros", nombre="Jailene")
