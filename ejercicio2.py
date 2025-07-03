#Ejercicio 2
"""Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

#Solución
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)
print()