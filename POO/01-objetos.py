# Ejemplo de como se crea una clase

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Se crea un metodo dentro de la clase
    def saludo(self):
        print("Hola, mi nombre es: ", self.nombre, self.apellido)


# Ejemplo de herencia

class Admin(Usuario):
    def super_saludo(self):
        print("Hola, me llamo ", self.nombre,
              self.apellido, " y son un Administrador.")


# Se crea la instancia de la clase Usuario


usuario = Usuario("Ignacio", "Cisneros")

usuario.saludo()

# Se crea la instancia de la clase Admin.

admin = Admin("Super", "Feliz")
admin.saludo()
admin.super_saludo()
