"""
Este ejercicio consiste en tener el nommbre
 y apellido y tener una funcion que imprima el nombre al reves

 Ejemplo: IGNACIO CISNEROS  ---> SORENSIC OICANGI
"""


name = "Ignacio"
apell = "Cisneros"


def voltear_nombre(nombre, apellido):
    """Funcion que recibel un nombre y apellido,
    los concatena y despues retorna el nombre junto con apellido
    a reves

    Args:
        nombre (string): Nombre del usuario
        apellido (string): apellido del usuario

    Returns: Regresa el nombre y apellido a reves
    """

    # Se concatena nombre y apellido

    nombre_completo = ''.join([nombre, apellido])
    nombre_al_reves = ''.join(reversed(nombre_completo))

    return nombre_al_reves


# Se manda a llamar a la funcion

resultado = voltear_nombre(nombre=name, apellido=apell)
print(f"El nombre al reves es: {resultado}")
