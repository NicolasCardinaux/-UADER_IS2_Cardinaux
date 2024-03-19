import sys

class Factorial:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def factorial(self, num):
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

    def run(self):
        for num in range(self.min, self.max + 1):
            print("El factorial de",num,"es", self.factorial(num))

# Comprueba si se pasó un argumento al script
if len(sys.argv) == 1:
   print("¡Debe informar un número o un rango de números!")
   entrada = input("Por favor, ingrese un número o un rango de números (ej. 5, 4-8, -10, o 4-): ")
else:
   # Toma el argumento como un número o un rango de números
   entrada = sys.argv[1]

# Verifica si la entrada es un solo número
if entrada.isdigit():
    num = int(entrada)
    print("El factorial de",num,"es", Factorial(num, num).run())
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
        # Divide la entrada en los números de inicio y fin
        inicio, fin = map(int, entrada.split('-'))

    # Calcula el factorial de cada número en el rango
    Factorial(inicio, fin).run()
