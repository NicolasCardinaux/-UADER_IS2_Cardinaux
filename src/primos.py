# Python program to display all the prime numbers within an interval

# Definir los límites inferior y superior del intervalo
lower = 1
upper = 100
# Imprimir una declaración indicando el rango que estamos comprobando para los números primos
print("Prime numbers between", lower, "and", upper, "are:")

# Iterar sobre cada número en el rango desde 'lower' hasta 'upper + 1'
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
  if num > 1:
       # Comprobar si 'num' es divisible por cualquier número hasta 'num'
       for i in range(2, num):
           # Si 'num' es divisible por 'i', entonces no es primo, por lo que rompemos el bucle
           if (num % i) == 0:
               break
       else:
           # Si 'num' no es divisible por ningún número hasta 'num', entonces es primo, por lo que lo imprimimos
           print(num)