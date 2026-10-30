#Ejercicio 11: Buscar un número específico
numeros = [3, 1, 4, 9, 7, 2, 8]
for num in numeros:
    if num == 7:
        print("¡Número 7 encontrado! Deteniendo la búsqueda.")
        break
    print(f"Buscando... número actual: {num}")