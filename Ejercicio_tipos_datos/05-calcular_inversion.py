"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión.
"""

# Se solicitan los datos del usuario

cantidad_invertir = float(input("Ingrese la cantidad que desea invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
numero_anios = float(input("Ingrese el numero de años: "))

# Se define la funcion que calculara el capital obtenido


def calcular_inversion(cantidad_inversion, interes_por_anio, anios_inversion):
    """Funcion que realiza el calculo de inversion

    Args:
        cantidad_inversion (float): cantidad de inversion.
        interes_por_anio (float): interes pór año.
        anios_inversion (float): años invertidos.
    """
    subtotal = cantidad_inversion * interes_por_anio
    capital = subtotal * anios_inversion
    print(f"El Capital total es de: {capital}")


if cantidad_invertir < 0 or interes_anual < 0 or numero_anios < 0:
    print("Favor de validar que los datos ingresados sean positivos.")
else:
    calcular_inversion(cantidad_invertir, interes_anual, numero_anios)
