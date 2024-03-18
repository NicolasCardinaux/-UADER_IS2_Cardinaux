# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:  # Si el número es 1 o menor, no es primo 
        return False

    elif numero <= 3:  # Si el número es 2 o 3, es primo 
        return True
    elif numero % 2 == 0 or numero % 3 == 0:  # Si es divisible por 2 o 3, no es primo
        return False
    
    # Comenzamos a verificar divisibilidad desde 5
    i = 5
    while i * i <= numero:  # Mientras el cuadrado de i sea menor o igual al número
        if numero % i == 0 or numero % (i + 2) == 0:  # Si es divisible por i o i+2, no es primo
            return False
        i += 6  # Incrementamos i en 6 para verificar los próximos números
    return True  # Si no se encontró ningún divisor, el número es primo

# Solicitar al usuario dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si ambos números son primos utilizando la función es_primo
if es_primo(numero1) and es_primo(numero2):
    print(numero1, "y", numero2, "son ambos números primos.")
else:
    print(numero1, "y", numero2, "no son ambos números primos.")
