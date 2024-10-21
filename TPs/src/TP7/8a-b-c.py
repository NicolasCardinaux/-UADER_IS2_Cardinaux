import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definición de las funciones
def E_acum(K, a, t):
    return K * (1 - np.exp(-a * t ** 2))

def E(t, K, a):
    return 2 * K * a * t * np.exp(-a * t**2)

# Datos históricos
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])

# Ajuste del modelo a los datos históricos
K_hist = np.sum(E_data)
popt, _ = curve_fit(lambda t, a: E(t, K_hist, a), t_data, E_data, p0=[0.1])
a_estimada = popt[0]

# 8a. Gráfica del dataset histórico y del modelo ajustado
t_fit = np.linspace(min(t_data), max(t_data), 100)
E_fit = E(t_fit, K_hist, a_estimada)

plt.scatter(t_data, E_data, label='Datos históricos')
plt.plot(t_fit, E_fit, label='Modelo ajustado', color='red')

# 8b. Cálculo y gráfica para un nuevo proyecto con K proporcionado (72 PM)
K_nuevo = 72
E_nuevo = E(t_fit, K_nuevo, a_estimada)
plt.plot(t_fit, E_nuevo, label='Nuevo proyecto (72 PM)', color='blue')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.legend()
plt.title('Esfuerzo Instantáneo Comparado')
plt.show()

# Cálculo del esfuerzo acumulado para el nuevo proyecto
E_nuevo_acum = E_acum(K_nuevo, a_estimada, t_fit)

# 8b. Gráfica del esfuerzo acumulado y los puntos de datos históricos
plt.plot(t_fit, E_nuevo_acum, label='Nuevo proyecto (72 PM)', color='blue')
plt.scatter(t_data, np.cumsum(E_data), label='Esfuerzo acumulado histórico', color='green')
plt.plot(t_fit, np.cumsum(E_fit), label='Modelo ajustado', color='red')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo acumulado (personas-mes)')
plt.legend()
plt.title('Esfuerzo Acumulado Comparado')
plt.show()

# 8c. Efecto de utilizar un valor de "a" que es el cuádruple del valor obtenido por calibración
a_cuadruple = 4 * a_estimada

# Cálculo y gráfica para el proyecto con el nuevo valor de 'a'
E_cuadruple = E(t_fit, K_nuevo, a_cuadruple)
plt.plot(t_fit, E_cuadruple, label='Nuevo proyecto con a cuadruple', color='purple')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.legend()
plt.title('Esfuerzo Instantáneo con a Cuádruple')
plt.show()

