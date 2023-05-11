

# Validar si una polabra es palindroma


# Funcion que elimina los espacios
def eliminar_espacios(palabra):
    palabra_sin_espacios = ""
    for char in palabra:
        if char != " ":
            palabra_sin_espacios += char
    return palabra_sin_espacios

# Funcion que valida sin una palabra es palindroma


def es_palabra_palindroma(palabra):
    es_palindroma = False
    print(f"Palabra con espacios {palabra}")
    palabra_sin_espacios = eliminar_espacios(palabra)
    texto_al_reves = palabra_al_reves(palabra_sin_espacios)

    if texto_al_reves.lower() == palabra_sin_espacios.lower():
        es_palindroma = True
    return es_palindroma


def palabra_al_reves(palabra):
    texto_al_reves = ""
    for char in palabra:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


palabra_final = eliminar_espacios("amo la paloma")
print(f"La palabra sin espacios es: {palabra_final}")


""" Se manda a llamar la funcion para validar si
la palabra ingresada es palindroma """

print(es_palabra_palindroma("amo la paloma"))
