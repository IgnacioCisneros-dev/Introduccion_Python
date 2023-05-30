"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

# Se le piden los datos al usuario

edad_usuario = int(input("Ingrese su edad : "))
sueldo_mensual = float(input("Ingrese su sueldo mensual: "))


# Validacion que determinara si el usuario debe de pagar impuestos

if edad_usuario > 0 and sueldo_mensual > 0:
    if edad_usuario > 18 and sueldo_mensual > 10000:
        print("Eres mayor de edad y tu sueldo es considerable, por lo que debes de pagar impuestos.")
    else:
        print("No has pasado la validacion para pagar impuestos.")
else:
    print("Favor de validar que los datos ingresados sean valores positivos.")
