class Factorial:
    def __init__(self):
        pass

    def factorial(self, x):
        """Esta es una función recursiva para encontrar el factorial de un entero"""
        if x == 1:
            return 1
        else:
            return x * self.factorial(x - 1)

    def run(self, min, max):
        """Calcula el factorial para cada número en el rango min-max"""
        for num in range(min, max + 1):
            resultado = self.factorial(num)
            print("El factorial de", num, "es", resultado)


if __name__ == "__main__":
    while True:
        try:
            # Solicitar al usuario el rango en formato correcto
            rango = input("Ingresa el rango en formato desde-hasta (ej. 4-8, o -10 o 50-) para calcular los factoriales: ")

            # Obtener los extremos del rango
            extremos = rango.split('-')
            desde = extremos[0]
            hasta = extremos[1]

            # Si no se especifica el límite inferior, se asume 1
            desde = int(desde) if desde != "" else 1

            # Si no se especifica el límite superior, se asume 60
            hasta = int(hasta) if hasta != "" else 60

            # Crear una instancia de la clase Factorial y ejecutar el método run
            factorial = Factorial()
            factorial.run(desde, hasta)

            break  # Salir del bucle si no hay errores
        except (ValueError, IndexError):
            print("Error: Ingresa el rango en el formato correcto (desde-hasta), por ejemplo, 4-8 o -10 o 50-.")
