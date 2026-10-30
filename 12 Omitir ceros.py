#Ejercicio 12: Omitir ceros
datos = [5, 0, 12, 0, 8, 0, 3]
for valor in datos:
    if valor == 0:
        continue
    print(f"Valor: {valor}")