"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
 todos los años que ha cumplido (desde 1 hasta su edad).
"""

# Se piden los datos al cliente

anios_cumplidos = int(input("Ingrese su edad: "))
print("Se muestran los años complidos: ")
for i in range(anios_cumplidos + 1):
    print(i)
