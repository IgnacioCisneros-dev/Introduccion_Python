# El Set significa conjunto o grupo de datos

# Creando un set

primer_set = {1, 2, 2, 2, 3, 3, 3, 4}
print(primer_set)  # En los set no se admiten valores repetidos

# Creando un set a partir de una lista

lista = [10, 9, 8, 10, 8]
segundo_set = set(lista)
print(f"Este es un set a partir de una lista: {segundo_set}")

# Viendo los operadores de los sets

# Union de SETS

print(primer_set | segundo_set)  # El operador | se le comose como UNION
