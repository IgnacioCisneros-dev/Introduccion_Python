# Ejercicio:
# Crear una funcion que cuenta cuantas vocales tiene una palabra


def contar_vocales(palabra):
    """Funcion que cuenta cuantas vocales tiene una palabra,
         la palabra la recibe como argumento
    Args:
        palabra (String): Palabra a la cual se contara cuantas vocales tiene
    Returns:
        Int: Retorna el numero de vocales que encontro en la palabra recibida como argumento
    """

    # Se itera la parabra
    contador = 0
    for i in palabra.upper():
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            contador += 1

    return contador


# Se llama a la funcion y se le pasa un parametro

print(contar_vocales("ignacio"))
