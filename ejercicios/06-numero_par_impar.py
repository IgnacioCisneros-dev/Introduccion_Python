# Ejercicio: Crear una funcion que diga si un numero es par o impar

# Se crea la funcion

def validar_par_impar(numero):
    """Funcion que recibe un argumento para validar si el numero es par o impar

    Args:
        numero (Numerico): numero el cual se va a validar

    Returns:
        String: Regresa confirmacion si el numero ingresado es PAR o IMPAR
    """

    DIVISOR = 2
    resultado = ""
    if numero % DIVISOR == 0:
        resultado = f"El numero {numero} si es PAR"
    else:
        resultado = f"El numero {numero} es IMPAR"

    return resultado

# Se llama a la funcion


print(validar_par_impar(4))
