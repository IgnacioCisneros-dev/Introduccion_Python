"""
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo
o un mensaje de aviso si la divisa no está en el diccionario.
"""

# De esta forma es como de declaran los diccionarios

monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

moneda = input("Favor de introducir una divisa: ")

if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa ingresada no existe en el diccionario.")
