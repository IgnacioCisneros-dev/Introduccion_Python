# Forma de iterar una listas con un for

lista_mascotas = ["Pelusa", "Ignacio", "Estiben", "Roky", 1, 2, 3]

# Iteracion de una lista normal
for mascota in lista_mascotas:
    print(mascota)


# Trabajando con tuplas para saber el indice donde se encuentra el elemento de la lista, para eso se ocupa ENUMERATE
for indice, mascota in enumerate(lista_mascotas):
    print(indice, mascota)
