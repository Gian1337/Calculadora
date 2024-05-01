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


'''
Función que toma dos parámetros (a = base y b = exponente) y luego  devuelve el cálculo de la potencia.
'''
def potencia(a,b):
    return a ** b

'''
Función que toma dos parámetros (a = numero y b = raiz) y luego devuelve el cálculo de la raíz.
'''

def raiz(a, b):
    return a ** (1/b)