nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese du direccion: ")
telefono = input("Ingrese su telefono: ")

# Se guardan los datos ingresados en el diccionario

diccionario = {'nombre': nombre,
               'edad': edad,
               'direccion': direccion,
               'telefono': telefono}

print(diccionario['nombre'], 'tiene ',
      diccionario['edad'], 'años, vive en ',
      diccionario['direccion'], ' y su numero de telefono es: ',
      diccionario['telefono'])
