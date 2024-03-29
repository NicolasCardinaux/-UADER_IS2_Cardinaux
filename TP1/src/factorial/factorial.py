#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

# Programa en Python para calcular el factorial de un número

import sys

def factorial(num): 
    # Función para calcular el factorial de un número dado
    if num < 0: 
        print("El factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Comprueba si se pasó un argumento al script
if len(sys.argv) == 1:
   # Si no se proporciona ningún argumento, solicita al usuario que ingrese un número o un rango de números
   print("Debe informar un número o un rango de números")
   entrada = input("Por favor, ingrese un número o un rango de números (ej. 5, 4-8, -10, o 4-): ")
else:
   # Toma el primer argumento pasado al script como entrada
   entrada = sys.argv[1]

# Verifica si la entrada es un solo número
if entrada.isdigit():
    # Si la entrada es un solo número, calcula su factorial
    num = int(entrada)
    print("El factorial de",num,"es", factorial(num))
else:
    # Verifica si la entrada es un rango sin límite inferior
    if entrada.startswith('-'):
        inicio = 1
        fin = int(entrada[1:])
    # Verifica si la entrada es un rango sin límite superior
    elif entrada.endswith('-'):
        inicio = int(entrada[:-1])
        fin = 60
    else:
        # Divide la entrada en los números de inicio y fin del rango
        inicio, fin = map(int, entrada.split('-'))

    # Calcula el factorial para cada número en el rango especificado
    for num in range(inicio, fin + 1):
        print("El factorial de",num,"es", factorial(num))
