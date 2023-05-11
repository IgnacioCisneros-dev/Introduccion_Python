lista_mascotas = ["Pelusa",
                  "Ignacio",
                  "Estiben",
                  "Roky",
                  1,
                  2,
                  3,
                  "Ignacio"]

# Agregando elementos a la lista

print(lista_mascotas)
lista_mascotas.insert(0, "Nueva mascota")
# Agrega un elemento al final de la lista
lista_mascotas.append("Mascota final")

# Eliminando elementos de un listado

lista_mascotas.remove("Roky")  # Elimina un elemento especifico de la lista

# Eliminando el ultimo elemento de la lista

lista_mascotas.pop()

print(lista_mascotas)
