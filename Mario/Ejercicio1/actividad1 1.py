#Ejercicio 1 by Jose Acosta 
"""
Dada la siguiente lista de estudiantes, cree un script usando ciclos, condiciones, variables y si quiere, funciones, que almacene los valores en las siguientes variables:

 promedio_edad -> el promedio de las edades de los estudiantes.
 num_menores_edad -> el numero de estudiantes menores de edad.
 num_mayores_edad -> el numero de estudiantes mayores de edad.
 porcentaje_mujeres -> el porcentaje de mujeres en el grupo.
 porcentaje_hombres -> el porcentaje de hombres en el grupo.
 estudiantes_activos -> numero de estudiantes activos.
"""

my_students = [
    {
        "nombre": "Juan",
        "edad": 23,
        "genero": "M",
        "activo": False
    },
    {
        "nombre": "Maria",
        "edad": 25,
        "genero": "F",
        "activo": True
    },
    {
        "nombre": "Lucia",
        "edad": 35,
        "genero": "F",
        "activo": False
    },
    {
        "nombre": "Pedro",
        "edad": 30,
        "genero": "M",
        "activo": True
    },
    {
        "nombre": "Luis",
        "edad": 15,
        "genero": "M",
        "activo": True
    }
]

def promedio():
    sumatoria = 0
    counter = 0
    for temp in my_students:
        sumatoria = sumatoria + temp["edad"]
        counter = counter + 1
    return sumatoria/counter

def edad(mode):
    counter = 0
    total = 0
    for temp in my_students:
        if 18 > temp["edad"]:
            counter = counter + 1
        total = total + 1
    if mode == 1:
        return total - counter
    return counter

def porcentaje_genero(mode):
    counter = 0
    total = 0
    for temp in my_students:
        total = total + 1
        if temp["genero"] == "M":
            counter = counter + 1
    if mode == 1:
        return (1 - counter/total)*100
    return (counter/total)*100

def estudiantes_activos():
    counter = 0
    for temp in my_students:
        if temp["activo"] == True:
            counter = counter + 1
    return counter

def primer_ejercicio():
    print(f'El promedio de edades de los alumnos es: {promedio()}')
    print(f'El numero de alumnos menores de edad es: {edad(0)}')
    print(f'El numero de alumnos mayores de edad es: {edad(1)}')
    print(f'El porcentaje de alumnos hombres es: {porcentaje_genero(0)}%')
    print(f'El porcentaje de alumnos mujeres es: {porcentaje_genero(1)}%')
    print(f'El numero de alumnos activos es: {estudiantes_activos()}')



if __name__ == "__main__":
    primer_ejercicio()
