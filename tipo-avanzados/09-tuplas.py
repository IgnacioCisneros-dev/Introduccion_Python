# Las tuplas son identicas a las listas pero estas no se pueden modificar, no se puedes eliminar ni añadir elementos

numeros = (1, 2, 3, 4, 5)
print(f"Los numeros son: {numeros}")

# De esta forma igual se pueden crear las tuplas

punto = tuple([1, 2, 3])
print(f"Tupla de otra manera: {punto}")


# Si se puede iterar una tupla

for numero in numeros:
    print(numero)


# Creando una lista a partir de una tupla para poder modificarla

nueva_lista = list(numeros)
# Aqui se esta modificando la nueva lista que se creo a partir de la tupla,
#  mas no la tupla, ya que las tuplas no se pueden modificar.
nueva_lista[0] = "Nuevo elemento en la lista"
print(f"Esta es la nueva lista: {nueva_lista}")
