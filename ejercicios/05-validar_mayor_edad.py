# Crear una funcion que valide si el usuario es mayor de edad

# Se crea la funcion

def validar_edad(edad_usuario):
    """Funcion que valida si el usuario es mayor
        de edad

    Args:
        edad_usuario (String): Edad del usuario
    """

    EDAD_MAYOR = 18
    mensaje = ""

    if edad_usuario > EDAD_MAYOR:
        mensaje = "Si es mayor de edad."
    else:
        mensaje = "No  es mayor de edad."

    return mensaje


# Se llama a la funcion

print(validar_edad(3))
