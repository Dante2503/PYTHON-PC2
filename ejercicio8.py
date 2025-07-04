#Ejercicio 8
"""Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento."""

#Solución:
def funcion_factorial(n):
    if n < 0:
        return "Número no válido"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
num = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {num} es {funcion_factorial(num)}")
    