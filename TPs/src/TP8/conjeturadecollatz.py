
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


def main():
    while True: 
        entrada = input("Ingrese un número entero positivo: ")
        try:
            num = int(entrada) 
            print("El número de iteraciones para %d es %d\n" % (num, collatz(num)))
            break  
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero positivo entre 1 y 1999.")
        except TypeError as e:
            print(e)


if __name__ == "__main__":
    main()
