import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


sesiones = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
defectos = np.array([1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0])


def modelo_logaritmico(x, lambda0, mu0):
    return lambda0 - mu0 * np.log(x + 1)


popt, pcov = curve_fit(modelo_logaritmico, sesiones, defectos)
lambda0, mu0 = popt


sesiones_proyectadas = np.linspace(1, 20, 100)
proyeccion_defectos = modelo_logaritmico(sesiones_proyectadas, *popt)


plt.scatter(sesiones, defectos, color='red', label='Defectos observados')
plt.plot(sesiones_proyectadas, proyeccion_defectos, color='blue', label='Proyección de defectos')
plt.title('Proyección de defectos por sesiones de prueba')
plt.xlabel('Sesiones de prueba')
plt.ylabel('Número de defectos')
plt.legend()
plt.grid(True)
plt.show()


print(f'Lambda0 (λ₀): {lambda0}')
print(f'Mu0 (μ₀): {mu0}')
