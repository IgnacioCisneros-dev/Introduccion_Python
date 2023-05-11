
# Ordenando los elementos de las listas
numeros = [4, 3, 2, 1, 5, 6, 10, 9, 8, 7]

numeros.sort()
print(f"Los numeros de la lista ordenados son: {numeros}")

# Ordenando en descendente

numeros.sort(reverse=True)

print(f"Los numeros de la lista ordenados descendente son: {numeros}")

# Esta es otra forma de ordenar una lista, la diferencia que con esta opcion,
# se crea una nueva lista, no se ve afectada la lista original
numeros2 = sorted(numeros)
print(f"Ordenando la lista: {numeros2}")
