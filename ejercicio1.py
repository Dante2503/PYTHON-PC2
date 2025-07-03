#Ejercicio 1
"""Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""

#Solución
print('Los divisores de 7 son: ')
for num in range(1500, 2701):
    if num % 7 == 0:
        print(num, end=' ')
print("\n")

print('Los múltiplos de 5 son: ')
for num in range(1500, 2701):
    if num % 5 == 0:
        print(num, end=' ')
print("\n")
