import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
dias = np.array([0, 1, 2, 3, 4, 5, 6])
defectos = np.array([9, 18, 5, 7, 23, 2, 8])

# Aplicamos una regresión logarítmica
defectos_log = np.log(defectos)
m, b = np.polyfit(dias, defectos_log, 1)

# Calculamos los coeficientes lambda0 y mu0
lambda0 = np.exp(b)
mu0 = -lambda0 / m

# Proyección para los próximos días
dias_proyeccion = np.arange(0, 10)
defectos_proyectados = lambda0 * np.exp(-dias_proyeccion / mu0)

# Visualización
plt.figure(figsize=(10,6))
plt.scatter(dias, defectos, label='Datos de defectos observados', color='red')
plt.plot(dias_proyeccion, defectos_proyectados, label='Proyección de defectos', color='blue')
plt.xlabel('Días de prueba')
plt.ylabel('Número de defectos')
plt.title('Proyección de defectos en el tiempo')
plt.legend()
plt.grid(True)
plt.show()
