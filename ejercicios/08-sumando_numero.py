# Ejercicio:
# Crear una aplicacion que pida numeros infinitos hasta que se ingrese la palabra BASTA

suma_total = 0
lista_numeros = []

while True:
    numero = input("Ingrese numero: ")
    if numero == "BASTA":
        break
    else:
        try:
            # Se parsea a intero
            numero = int(numero)
            lista_numeros.append(numero)
        except:
            print("Favor de solo ingresar numeros.")
            break


# Ahora se iteran los numeros ingresados para sumarlos

for x in lista_numeros:
    suma_total += x


# Se imprime la suma total

print(f"La suma total de los numeros ingresados es: {suma_total}")
