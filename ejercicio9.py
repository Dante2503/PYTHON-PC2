#Ejercicio 9
"""Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?"""

#Solución:
def quitar_vocales(texto):
    vocales = "aeiouAEIOU"
    return ''.join([letra for letra in texto if letra not in vocales])
entrada = input("Ingrese texto (Input): ")
print("Texto sin vocales (Output):", quitar_vocales(entrada))
