
# Este ejemplo es para ver como funciona el depurador

def contar_palabras(palabra):
    resultado = 0
    for _ in palabra:
        resultado += 1
    return resultado


print("Inicio de la aplicacion")
nombre = "ignacio cisneros juarez"
# aqui se llama a la funcion que cuenta las palabras
resultado = contar_palabras(nombre)
print(f"El numero de palabras que contiene {nombre} es de {resultado}")
print("Termina la aplicacion.")
