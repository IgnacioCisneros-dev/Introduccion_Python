
# Se crea la lista
list_usuarios = [["Ignacio", 1],
                 ["Emir", 2],
                 ["Jaii", 3]]


# De la lista de usuarios, se crea una lista de nombre
list_nombres = []
for usuario in list_usuarios:
    list_nombres.append(usuario[0])
print(list_nombres)

# Lo mismo pero de una forma mas elegante

list_nombres2 = [usuario[0] for usuario in list_usuarios]
print(list_nombres2)

# Filtrado de una lista, se filtran los usuarios
# que tengan el id mayor a 1

list_nombres = [usuario for usuario in list_usuarios if usuario[1] > 1]
print(list_nombres)


# Ejemplo con transaformacion de lista y filtrado.
list_nombres4 = [usuario[1] for usuario in list_usuarios if usuario[1] > 1]
print(list_nombres4)
