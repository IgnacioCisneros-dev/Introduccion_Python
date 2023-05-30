"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
# Se consulta la informacion del empleado


nombre_empleado = input("Ingrese su nombre: ")
horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
sueldo_hora = int(input("Ingrese el sueldo por hora: "))

# Se crea una funcion que calculara el pago del empleado


def calcular_sueldo(numero_horas_trabajadas, sueldo_por_hora):
    """Funcion que realiza el calculo del sueldo total de los trabajadores

    Args:
        numero_horas_trabajadas (int): Son el numero de horas que el empleado trabaja a la semana
        sueldo_por_hora (int): El el sueldo que se le paga al trabajador por hora

    Returns:
        int: Sueldo final que recibe el empleado
    """
    sueldo_final = numero_horas_trabajadas * sueldo_por_hora
    return sueldo_final


# Llamamos a la funcion pasandole los parametros necesarios


sueldo_total = calcular_sueldo(horas_trabajadas, sueldo_hora)
print(f"El sueldo total del empleado {nombre_empleado} , es: {sueldo_total} ")
