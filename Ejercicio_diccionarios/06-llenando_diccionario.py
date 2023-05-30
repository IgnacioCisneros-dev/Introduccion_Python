informacion_persona = {}

nombre = input("Ingrese su nombre: ")
informacion_persona.update({'nombre': nombre})
print(f'Valor del diccionario: {informacion_persona}')

edad = int(input("Ingrese su edad: "))
informacion_persona.update({'edad': edad})
print(f'Valor del diccionario: {informacion_persona}')

sexo = input("Ingrese su sexo: ")
informacion_persona.update({'sexo': sexo})
print(f'Valor del diccionario: {informacion_persona}')

telefono = input("Ingrese su numero de telefono: ")
informacion_persona.update({'telefono': telefono})
print(f'Valor del diccionario: {informacion_persona}')

correo = input("Ingrese su correo electronico: ")
informacion_persona.update({'correo': correo})
print(f'Valor del diccionario: {informacion_persona}')
