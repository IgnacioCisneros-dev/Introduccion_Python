def mostrar_productos(**datos):
    print(datos["id"], datos["nombre"], datos["descripcion"])
    print(f"Tambien se puede imprimir todo como un diccionario {datos}")


# Se manda a llamar a la funcion
# Con kwargs se le pueden pasar los parametros que sean
mostrar_productos(id="1",
                  nombre="Iphone",
                  descripcion="Esto es una descripcion")
