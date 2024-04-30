'''
Proyecto: Calculadora
Alumno: Gianluca Carlini
Fecha límite: 08/05/2024
Problema: Se decidió abordar el problema de una CALCULADORA utilizando programación estructurada y funcional. En un módulo, se codificaran aquellas funciones básicas correspondientes a una calculadora (suma, resta, multiplicación, división). En otro módulo, se obtendrán las entradas que el usuario ingrese y la operación deseada.

'''

import math
#Se importa las funciones básicas de una calculadora
import FuncBasicas.defBasicas as defBasics

#Declaración de lista donde se almacenan los resultados
resultados = [] 

def calculadora(nro1, nro2, operacion):
    
    if operacion == "+":
        rdo = defBasics.suma(nro1, nro2) #Llama a la función suma y se almacena en variable resultado
        print(f"El resultado de la suma es: {rdo}") 
    elif operacion == "-":
        rdo = defBasics.resta(nro1, nro2) #Llama a la función resta y se almacena en variable resultado
        print(f"El resultado de la resta es: {rdo}") 
    elif operacion == "*":
        rdo = defBasics.multiplicacion(nro1,nro2) #Llama a la función multiplicación y se almacena en variable resultado
        print(f"El resultado de la multiplicación es: {rdo}") 
    elif operacion == "/":
        rdo = defBasics.division(nro1,nro2) #Llama a la función división y se almacena en variable resultado
        print(f"El resultado de la división es: {rdo}") 
    else:
        print("Error!!!")
        rdo = None

    resultados.append(rdo)
    return tuple(resultados)


'''
Función que obtiene los inputs(primer número, segundo número y el tipo de operación que desea) del usuario y retorna esos valores.
Además, valida que la operación sea las permitidas por sistemas (suma, resta, multiplicación, división).
'''
def get_inputs():
    while True:
        try:
            print("Bienvenido a la Calculadora")
            while True: #Bloque de validación del primer número para que el usuario ingrese únicamente un número.
                try:
                     var1= float(input("Ingrese el primer número: "))
                     break
                except ValueError:
                    print("Input inválido. Debe ingresar un número!!!")
            
            while True: #Bloque de validación del segundo número para que el usuario ingrese únicamente un número.
                try:
                    var2= float(input("Ingrese el segundo número: "))
                    break
                except ValueError:
                    print("Input inválido. Debe ingresar un número!!!")
            
            #Validación para que el usuario ingrese el carácter correcto de operación
            operacion= input("Ingrese una operación (+, -, *, /): ")
            if operacion not in ['+','-', '*', '/']:
                raise ValueError("Operador inválido. Sólo puede ingresar + , - , * , /")
            
            return var1, var2, operacion
        except ValueError as error:
            print(f"Ingrese los datos nuevamente {error}")

numero1, numero2, operacion = get_inputs()

#Los outputs que genere la calculadora la cual recibe por parametro dos numeros y una operación, se irán agregando a la lista 'resultados'.
resultados = calculadora(numero1,numero2,operacion)

print("Los resultados de las operaciones son: ")
#Finalmente, recorro el arreglo y muestro los resultados guardados.
for rdo in resultados:
    print(f"Resultado: {rdo}")
