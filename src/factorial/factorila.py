def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("El Factorial de 10 es:")
print(factorial(10))
