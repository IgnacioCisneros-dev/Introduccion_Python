
# Ejemplo de la funcion del while

numero = 0
while numero < 10:
    print(numero)
    numero += 1

print("-----------------------------")

# Ejemplo con el uso de la palabra break
# para detener la ejecucion del while

a = 0
while a < 10:
    print(a)
    a += 1
    if a == 5:
        break


# Iterando una lista con un loop for

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    print(f"Numero {numero}")


# Uso del break para interrumpir la iteracion

for numero in lista_numeros:
    if numero == 5:
        break  # Con esta palabra se detiene la iteracion
    print(f"Ejemplo con break: {numero}")


# Uso de la palabra continue para omitir algo y continuar con la iteracion

for numero in lista_numeros:
    if numero == 5:  # Con esta validacion se omite el numero 5 y no se imprime en consolda.
        continue
    print(f"Ejemplo con la palabra continue: {numero}")


# ----Funcion del Range----#

for x in range(5):  # Itera del 0 al 5
    print(f"Ejemplo con Range: {x}")

for x in range(5, 10):  # Itera del 5 al 10
    print(f"Ejemplo del Ragna con inicio y fin: {x}")


for x in range(0, 30, 10):  # Itera del 0 al 30 incrementando de 10 en 10
    print(f"Ejemplo con 3 parametros: {x}")


# Ejemplo del for else

for x in range(4):
    print(x)
else:
    print("Se ha terminado de iterar el for!!!")
