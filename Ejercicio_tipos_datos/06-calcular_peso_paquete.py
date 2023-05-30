"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""

# Declaracion de constantes

PESO_PAYASO = 112
PESO_MUNECA = 75

# Se piden los datos al usuario

numero_payasos = int(input("Ingrese el numero de payasos vendidos: "))
numero_munecas = int(input("Ingrese el numero de muñecas vendidas: "))

# Se valida que los datos ingresados sean validos.

if numero_munecas > 0 and numero_payasos > 0:
    peso_total_payasos = PESO_PAYASO * numero_payasos
    peso_total_munecas = PESO_MUNECA * numero_munecas

    peso_total_paquete = peso_total_payasos + peso_total_munecas

    # Se imprime el peso total del paquete

    print("El peso total del paquete que sera enviado es de: ", peso_total_paquete)
else:
    print("Favor de valida que los numeros ingresados sean correcto, deben de ser enteros positivos.")
