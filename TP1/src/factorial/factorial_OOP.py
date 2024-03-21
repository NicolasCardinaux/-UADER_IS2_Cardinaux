import sys

class Factorial:
    def __init__(self, min, max):
        # Inicializa el objeto Factorial con los valores mínimos y máximos para el cálculo
        self.min = min
        self.max = max

    def factorial(self, num):
        # Método para calcular el factorial de un número dado
        if num < 0:
            # Si el número es negativo, el factorial no está definido
            print("El factorial de un número negativo no existe")
        elif num == 0:
            # El factorial de 0 es 1
            return 1
        else:
            # Calcula el factorial utilizando un bucle while
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self):
        
        # Método para ejecutar el cálculo del factorial para cada número en el rango dado
        for num in range(self.min, self.max + 1):
            print("El factorial de", num, "es", self.factorial(num))

# Comprueba si se pasó un argumento al script
if len(sys.argv) == 1:
    # Si no se proporciona ningún argumento, solicita al usuario que ingrese un número o un rango de números
    print("¡Debe informar un número o un rango de números!")
    entrada = input("Por favor, ingrese un número o un rango de números (ej. 5, 4-8, -10, o 4-): ")
else:
    # Toma el primer argumento pasado al script como entrada
    entrada = sys.argv[1]

# Verifica si la entrada es un solo número
if entrada.isdigit():
    # Si la entrada es un solo número, calcula el factorial para ese número
    num = int(entrada)
    print("El factorial de", num, "es", Factorial(num, num).run())
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
    Factorial(inicio, fin).run()
