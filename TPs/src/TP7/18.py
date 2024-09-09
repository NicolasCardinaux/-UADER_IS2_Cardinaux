import numpy as np
from scipy.optimize import fsolve

# Datos iniciales
costo_mensual = 1000  # Inversión mensual en dólares
meses_iniciales = 12  # Duración inicial del proyecto en meses
valor_futuro = 18000  # Valor presente de los flujos de caja futuros al finalizar el proyecto
tasa_efectiva_mensual = 0.01  # Tasa efectiva mensual

# a. Cálculo del Valor Presente Neto (VPN) del proyecto si se ejecuta según lo planeado

# Cálculo del Valor Presente de las Inversiones (VPI)
VPI = sum([costo_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_iniciales + 1)])

# Cálculo del Valor Presente de los Flujos de Caja (VPF)
VPF = valor_futuro / (1 + tasa_efectiva_mensual) ** meses_iniciales

# Cálculo del Valor Presente Neto (VPN)
VPN_original = VPF - VPI

print(f"a. El Valor Presente Neto (VPN) del proyecto según los planes originales es: ${VPN_original:.2f}")

# b. Cálculo del Valor Presente Neto (VPN) si el proyecto se extiende por tres meses más

# Nuevos meses de inversión si el proyecto se extiende
meses_extendidos = meses_iniciales + 3

# Cálculo del Valor Presente de las Inversiones (VPI) para 15 meses
VPI_extendido = sum([costo_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_extendidos + 1)])

# Cálculo del Valor Presente de los Flujos de Caja (VPF) para 15 meses
VPF_extendido = valor_futuro / (1 + tasa_efectiva_mensual) ** meses_extendidos

# Cálculo del Valor Presente Neto (VPN) para 15 meses
VPN_extendido = VPF_extendido - VPI_extendido

print(f"b. El Valor Presente Neto (VPN) del proyecto con 3 meses adicionales es: ${VPN_extendido:.2f}")

# c. Cálculo de la Rentabilidad en ambos casos

# Rentabilidad = Valor Presente Neto / Valor Presente de la Inversión
rentabilidad_original = VPN_original / VPI
rentabilidad_extendida = VPN_extendido / VPI_extendido

print(f"c. La rentabilidad del proyecto según los planes originales es: {rentabilidad_original:.2%}")
print(f"c. La rentabilidad del proyecto con 3 meses adicionales es: {rentabilidad_extendida:.2%}")

# d. Impacto del retraso en 6 meses en la entrega del proyecto

# Cálculo del VPN si el retraso es de 6 meses (total de 18 meses)
meses_retraso = meses_iniciales + 6

# Cálculo del Valor Presente de las Inversiones (VPI) para 18 meses
VPI_retraso = sum([costo_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_retraso + 1)])

# Cálculo del Valor Presente de los Flujos de Caja (VPF) para 18 meses
VPF_retraso = valor_futuro / (1 + tasa_efectiva_mensual) ** meses_retraso

# Cálculo del Valor Presente Neto (VPN) para 18 meses
VPN_retraso = VPF_retraso - VPI_retraso

# El impacto del retraso es la diferencia entre el VPN original y el VPN con el retraso
impacto_retraso = VPN_retraso

print(f"d. El impacto del retraso de 6 meses en la entrega del proyecto es: ${impacto_retraso:.2f}")

# e. Análisis de la conveniencia de agregar un costo adicional del 5% para garantizar la ejecución según el calendario original

# Costo mensual adicional del 5% para la gestión profesional del proyecto
costo_adicional_gerencia = 0.05 * costo_mensual
costo_total_mensual_gerencia = costo_mensual + costo_adicional_gerencia

# Cálculo del VPI con costos de gerencia adicionales
VPI_gerencia = sum([costo_total_mensual_gerencia / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_iniciales + 1)])

# Cálculo del VPN con gerencia de proyectos
VPN_con_gerencia = VPF - VPI_gerencia

print(f"e. El Valor Presente Neto (VPN) con gerencia de proyectos es: ${VPN_con_gerencia:.2f}")

# f. Cálculo del costo mensual máximo aceptable si el proyecto se extiende a 15 meses pero el inversor quiere mantener el mismo valor presente de la utilidad que en el caso original

# Función para el cálculo del VPN en función del costo mensual
def calcular_VPN_con_costo_mensual(costo_mensual, meses, tasa, valor_futuro, VPN_deseado):
    VPI = sum([costo_mensual / (1 + tasa) ** t for t in range(1, meses + 1)])
    VPF = valor_futuro / (1 + tasa) ** meses
    return VPF - VPI - VPN_deseado

# Encontrar el costo mensual que hace que el VPN sea igual al VPN original
costo_maximo_mensual = fsolve(calcular_VPN_con_costo_mensual, x0=costo_mensual, args=(meses_extendidos, tasa_efectiva_mensual, valor_futuro, VPN_original))[0]

print(f"f. El costo mensual máximo aceptable si el proyecto se extiende a 15 meses es: ${costo_maximo_mensual:.2f}")
