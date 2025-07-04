#Ejercicio 7
"""Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no."""

#Solución
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Ingrese un número para verificar si es primo: "))
print(f"{num} es primo." if es_primo(num) else f"{num} no es primo.")