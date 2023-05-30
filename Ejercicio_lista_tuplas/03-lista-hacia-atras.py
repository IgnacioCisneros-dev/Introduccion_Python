"""
Escribir un programa que pregunte al usuario los números
ganadores de la lotería primitiva, los almacene en una lista
y los muestre por pantalla ordenados de menor a mayor.
"""

lista_numeros_ganadores = []

for i in range(6):
    lista_numeros_ganadores.append(
        int(input("Ingrese los numeros ganadores de la loteria: ")))

lista_numeros_ganadores.sort()
print(f"Los numeros ganadores son: {lista_numeros_ganadores}")
