frutas_y_precio = {'Platano': 1.35,
                   'Manzana': 0.80,
                   'Pera': 0.85,
                   'Naranja': 0.70}

nombre_fruta = input(
    "Ingrese el nombre de la fruta que desea calcular el precio: ")


def calcular_precio_fruta(kilos, precio_kilo):
    precio_total = kilos * precio_kilo
    return precio_total


if nombre_fruta in frutas_y_precio:
    print(f"La fruta {nombre_fruta} si existe en la lista.")
    numero_kilos = float(input("Ingrese el numero de kilos: "))
    precio_final = calcular_precio_fruta(
        numero_kilos,
        frutas_y_precio[nombre_fruta])
    print(f"El precio final es: $ {precio_final}")
else:
    print(f"La fruta {nombre_fruta} no se encontro en la lista.")
