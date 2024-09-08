import numpy as np
import matplotlib.pyplot as plt

# Relaciones dadas
def calcular_esfuerzo(S):
    return 8 * S ** 0.95

def calcular_tiempo_calendario(E):
    return 2.4 * E ** 0.33

# Valores de S y E
tamanos_S = np.linspace(0, 10000, 100)
esfuerzos_E = calcular_esfuerzo(tamanos_S)

# Tiempo calendario para valores de esfuerzo
tiempos_calendario = calcular_tiempo_calendario(esfuerzos_E)

# Graficar E en función de S
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(tamanos_S, esfuerzos_E, label="Esfuerzo (E) vs Tamaño (S)")
plt.xlabel("Tamaño del proyecto (S)")
plt.ylabel("Esfuerzo (E)")
plt.title("Esfuerzo en función del tamaño del proyecto")
plt.legend()

# Graficar td en función de E
plt.subplot(1, 2, 2)
esfuerzos_para_td = np.linspace(1, 500, 100)
tiempos_calendario_para_td = calcular_tiempo_calendario(esfuerzos_para_td)
plt.plot(esfuerzos_para_td, tiempos_calendario_para_td, label="Tiempo calendario (td) vs Esfuerzo (E)")
plt.xlabel("Esfuerzo (E)")
plt.ylabel("Tiempo calendario (td)")
plt.title("Tiempo calendario en función del esfuerzo")
plt.legend()

plt.tight_layout()
plt.show()
