import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
tiempo = np.arange(0, 20, 1)
costo_proyecto = -np.minimum(tiempo, 12)  # Inversiones hasta el mes 12
plan_ingresos = np.maximum(0, tiempo - 12) * 2  # Ingresos planificados después del mes 12
ingresos_reales = plan_ingresos * 0.8  # Ingresos reales (80% del plan)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos
ax.fill_between(tiempo, costo_proyecto, color="blue", alpha=0.3, label="Plan")  # Área de costos
ax.plot(tiempo, plan_ingresos, label="Plan Income", color="yellow", linewidth=2)
ax.plot(tiempo, ingresos_reales, label="Real Income", color="magenta", linestyle="--", marker="o")

# Configurar etiquetas y leyenda
ax.set_xlabel("Tiempo")
ax.set_ylabel("Costo / Ingreso")
ax.set_title("Costo de Proyecto")
ax.legend()

# Mostrar la gráfica
plt.show()