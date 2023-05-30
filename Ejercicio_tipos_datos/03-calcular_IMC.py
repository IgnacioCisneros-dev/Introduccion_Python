"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
es el índice de masa corporal calculado redondeado con dos decimales.
"""

# Se piden los datos al usuario

peso = float(input("Ingrese su peso en KG: "))
estatura = float(input("Ingrese su estatura en METROS: "))

# Se define una funcion para calcular el IMC


def calcular_imc(peso_usuario, altura_usuario):
    """Funcion que calcula el Indice de masa corporal.

    Args:
        peso_usuario (kilogramos): Peso que el usuario ingresa.
        altura_usuario (metros): Altura que el usuario ingresa.

    Returns:
        decimal: Indice de masa corporal calculado con los datos
        que el usuario ingresa.
    """
    masa_corporal = peso_usuario / (altura_usuario * altura_usuario)
    return masa_corporal


# Se imprime los resultados in IMC

print(f"El IMC es de: {calcular_imc(peso, estatura)}")
