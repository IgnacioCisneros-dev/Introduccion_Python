animal = "perro"
objeto = "carro rojo"
espacios = " carro verder  "
# UPPER() es un metodo que sirve para poner un string o una palabra en MAYUSCULAS
print(animal.upper())
print(animal.lower())  # Metodo que sirve para colocar un string en minusculas
# Metodo que sirve para poner solo la primer letra del string en MAYUSCULAS
print(animal.capitalize())

"""
    El metodo title() sirve para colocar la primer letra de cada palabra en mayusculas
    """


print(objeto.title())

"""
    El metodo strip sirve para poder eliminar
    los espacion en blanco de una cadena al inicio
    """

print(espacios.strip())

print(espacios.lstrip())  # Elimina los espacios de la izquierda
print(espacios.rstrip())  # Elimina los espacios en blanco de la derecha

# Devuelva el indice donde se encuentra la palabra que recibe como argumento
print(animal.find("r"))

# Metodo que remplaza los caracteres de un string
print(animal.replace("perro", "gato"))

"""
    Los siguientes 2 metodos regresan un booleano si es
    que la palabra ingresada existe en la variable
    """

# Aqui estoy buscando si es que rr existe en el string "animal"
print("rr" in animal)
# Aqui los que estoy buscando es si aa no existe en la variable animal, ambos regresaran true
print("aa" not in animal)
