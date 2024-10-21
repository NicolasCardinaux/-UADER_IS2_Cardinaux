import matplotlib.pyplot as plt

def collatz(n):
    """Calcula la secuencia de Collatz para un número dado y devuelve el número de iteraciones"""
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        iteraciones += 1
    return iteraciones

# Calcular la secuencia de Collatz para los números entre 1 y 10000
nums = list(range(1, 10001))
iteraciones = [collatz(n) for n in nums]

# Imprimir una respuesta
# for i in range(len(nums)):

#      print(f"El número {nums[i]} tardó {iteraciones[i]} iteraciones en converger a una secuencia repetitiva.")


# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(iteraciones, nums, s=1)
plt.title('Secuencia de Collatz para números entre 1 y 10000')
plt.xlabel('Número de iteraciones para converger')
plt.ylabel('Número de inicio de la secuencia')
plt.show()
