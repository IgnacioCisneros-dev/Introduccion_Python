"""
    Escribir una funcion que encuentre el numero menor de la lista
   """


# Se crea la lista

lista = [4, 3, 65, 235, 23, 54, 23, 5]

menor = "init"

for x in lista:
    if menor == "init":
        menor = x
    else:
        menor = x if x < menor else menor

print(f"Lista: {lista}")
print(f"El numero menor de la lista es: {menor}")
