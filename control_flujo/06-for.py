"""
    Este es un ejemplo del buclo o loop for en python
    """

buscar = 19
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Se encontro el numero buscado." f"{buscar}")
        break
else:
    print("No se encontro el numero " f"{buscar}")
