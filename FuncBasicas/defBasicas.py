# Funciones Básicas

'''
Función que toma dos párametros y retorna la suma de ellos
'''
def suma(a,b):
    return a + b


'''
Función que toma dos párametros y retorna la resta de ellos
'''
def resta(a,b):
    return a - b


'''
Función que toma dos párametros y retorna la división de ellos
'''
def division(a,b):
    if  b == 0:
        raise ValueError("No se puede dividir por 0!!!")
    else:
        return a / b


'''
Función que toma dos párametros y retorna la multiplicación de ellos
'''
def multiplicacion(a,b):
    return a * b

