
# Clase padre de animal

class Animal:
    def __init__(self, nombre, anomatopeya):
        self.nombre = nombre
        self.anomatopeya = anomatopeya

    def saludar(self):
        print(f"Hola son un animal y mi sonido es : {self.anomatopeya}")


# Clase para Gato

class Gato(Animal):
    tipo = "Gato"


# Clase para perro

class Perro(Animal):
    tipo = "Perro"


# Se crea el objeto de la clase Gato

gato = Gato("Rene", "Maullido")
gato.saludar()

# Se crea el objeto de la clase de perro

perro = Perro("Rocky", "Ladrido")
perro.saludar()
