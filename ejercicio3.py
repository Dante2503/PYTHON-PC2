#Ejercicio 3
"""Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
"""

#Solución
numeros = []
while True:
    desea = input("¿Desea ingresar un número?: ").strip().upper()
    if desea != "SI":
        break
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares
print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print()