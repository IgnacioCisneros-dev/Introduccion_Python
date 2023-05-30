"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y 
elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir.
"""

lista_asignaturas = ["Matemáticas",
                     "Física",
                     "Química",
                     "Historia",
                     "Lengua"]

# Se crea una lista vacia

lista_asignaturas_aprobadas = []
lista_asignaturas_reprobadas = []


for i in lista_asignaturas:
    calificacion = float(input(f"¿Cual es tu calificacion en {i} ?"))
    if calificacion >= 6:
        lista_asignaturas_aprobadas.append(i)
    else:
        lista_asignaturas_reprobadas.append(i)

print("Las asignaturas aprobadas son: ", lista_asignaturas_aprobadas)
print("Las asignaturas que debes de repetir son: ", lista_asignaturas_reprobadas)
