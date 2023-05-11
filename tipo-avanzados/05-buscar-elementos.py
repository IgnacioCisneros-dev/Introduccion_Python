lista_mascotas = ["Pelusa", "Ignacio", "Estiben", "Roky", 1, 2, 3, "Ignacio"]

# Buscar un elemento en la lista y saber el indice en donde se encuentra

if "Roky" in lista_mascotas:
    print(lista_mascotas.index("Roky"))


# Contarndo cuantas elementos hay en la lista
veces = lista_mascotas.count("Ignacio")
print(f"La palabra Ignacio se encuentra {veces} en la lista")
