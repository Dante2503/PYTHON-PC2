#Ejercicio 4
"""Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
"""

#Solución
diccionario_nota_alumno = {
    "Alumno": "Juan",
    "Notas": [15, 16, 17]
}
diccionario_nota_alumno2 = {
    "Alumno": "Jose",
    "Notas": [10, 12, 15]
}
diccionario_nota_alumno3 = {
    "Alumno": "Omar",
    "Notas": [11, 8, 18]
}
listado_alumnos =[
    diccionario_nota_alumno, 
    diccionario_nota_alumno2, 
    diccionario_nota_alumno3
]
print(listado_alumnos)