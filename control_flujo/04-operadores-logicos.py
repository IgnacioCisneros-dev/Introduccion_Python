# and, or , not

gas = False
encendido = False
edad = 20

# if gas and encendido:
#     print("Tienes lo necesario para andar en automovil.")
# else:
#     print("No puedes avanzar.")

if not gas or (encendido and edad > 18):
    print("Tienes lo necesario para andar en automovil.")
else:
    print("No puedes avanzar.")
