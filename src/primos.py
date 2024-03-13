def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Hola Prueba
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si ambos números son primos
if es_primo(numero1) and es_primo(numero2):
    print(numero1, "y", numero2, "son ambos números primos.")
else:
    print(numero1, "y", numero2, "no son ambos números primos.")
    print(numero1, "y", numero2, "no son ambos números primos.")
   
    
