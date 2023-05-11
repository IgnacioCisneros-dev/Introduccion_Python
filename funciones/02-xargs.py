# Ejemplo de una funcion que recibe multiples parametros
# y dentro de la funcion se maneja como iterable

def sumar(*numeros):
    resultado_suma = 0
    for numero in numeros:
        resultado_suma += numero
    print(f"El resultado de las suma es de: {resultado_suma}")


sumar(5, 5)
sumar(10, 10, 20)
sumar(50, 10, 5, 5, 10, 20)
