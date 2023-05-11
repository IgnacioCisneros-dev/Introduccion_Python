# Manipulando listas

mascotas = ["Pelusa", "Pulga", "Bicho", "Copito", "Roky"]
print(mascotas[1])  # Accede a un elemento en la lista
# Acede al la listas comenzando desde el elemento 2 hasta el final
print(mascotas[2:])
# Acede a los elementos de la listas desde el inicio de la lista hasta la posicion 3
print(mascotas[:3])


# Ejemplo para imprimir los numeros pares e imperes de una lista

list_numeros = list(range(21))
print(f"Numeros Impares: {list_numeros[1::2]}")  # Numeros Impares
print(f"Numeros Pares: {list_numeros[::2]}")  # Numeros Pares
