#Ejercicio 10: Contador de vocales
frase = "dark souls el lo maximo"
vocales = "aeiouAEIOU"
contador = 0

for caracter in frase:
    if caracter in vocales:
        contador += 1

print(f"La frase contiene {contador} vocales.")