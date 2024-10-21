# Calculando el número de iteraciones del algoritmo de Collatz con validación de entrada
def collatz(num):
    if not isinstance(num, int):
        raise TypeError("Debe ingresar un número entero.")
    
    if num < 1 or num > 1999:
        raise ValueError("El número debe ser un entero positivo entre 1 y 1999")
    
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Función principal para recibir input y ejecutar Collatz
def main():
    while True:  # Bucle para permitir reintentos
        entrada = input("Ingrese un número entero positivo: ")
        try:
            num = int(entrada)  # Convertir entrada a número entero
            print("El número de iteraciones para %d es %d\n" % (num, collatz(num)))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero positivo entre 1 y 1999.")
        except TypeError as e:
            print(e)

# Ejecutar el programa
if __name__ == "__main__":
    main()
