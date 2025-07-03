#Ejercicio 5
"""Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count.
"""

#Solución
def contar_digito(numero, digito):
    return str(numero).count(str(digito))

numero = int(input("Ingrese el número: "))
digito = int(input("Ingrese el dígito a buscar: "))
print(f"Cantidad de veces {digito} en el número: {contar_digito(numero, digito)}")
