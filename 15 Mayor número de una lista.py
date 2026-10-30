#Ejercicio 15: Mayor número de una lista
valores = [14, 52, 8, 91, 33, 47]
mayor = valores[0]

for val in valores:
    if val > mayor:
        mayor = val

print("El número mayor de la lista es:", mayor)