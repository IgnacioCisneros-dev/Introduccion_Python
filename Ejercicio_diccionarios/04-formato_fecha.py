meses = {1: 'enero',
         2: 'febrero',
         3: 'marzo',
            4: 'abril',
         5: 'mayo',
         6: 'junio',
         7: 'julio',
         8: 'agosto',
         9: 'septiembre',
         10: 'octubre',
         11: 'noviembre',
         12: 'diciembre'}

fecha = input("Ingrese una fecha en el formato dd/mm/yyyy: ")
fecha = fecha.split('/')
print(f"{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}")
