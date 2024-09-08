import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Datos históricos
data = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

df = pd.DataFrame(data)

# Modelo Lineal
a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
R = np.corrcoef(df['LOC'], df['Esfuerzo'], 1)
R2_lineal = R**2
r_value_lineal = R2_lineal[1][0]
print("Modelo lineal: E = %.6f + %.6f * LOC" % (b, a))
print("R-squared (lineal) = %.4f" % r_value_lineal)

# Modelo Exponencial
df['logEsfuerzo'] = np.log(df['Esfuerzo'])
df['logLOC'] = np.log(df['LOC'])
X = df['logLOC']
Y = df['logEsfuerzo']
X = sm.add_constant(X)

mx = sm.OLS(Y, X).fit()
k = np.exp(mx.params['const'])
b_exp = mx.params['logLOC']
r_value_exponencial = mx.rsquared
print("Modelo exponencial: E = %.6f * (LOC ^ %.6f)" % (k, b_exp))
print("R-squared (exponencial) = %.4f" % r_value_exponencial)

# Comparar modelos y elegir el mejor
if r_value_lineal > r_value_exponencial:
    mejor_modelo = "lineal"
    print(f"El modelo que mejor representa los datos es el modelo lineal")
else:
    mejor_modelo = "exponencial"
    print(f"El modelo que mejor representa los datos es el modelo exponencial")

# Estimación para LOC = 9100
LOC_estimar_9100 = 9100
if mejor_modelo == "lineal":
    esfuerzo_estimado_9100 = a * LOC_estimar_9100 + b
else:
    esfuerzo_estimado_9100 = k * (LOC_estimar_9100 ** b_exp)

print(f"Esfuerzo estimado para LOC={LOC_estimar_9100} es: {esfuerzo_estimado_9100:.4f} PM")

# Estimación para LOC = 200
LOC_estimar_200 = 200
if mejor_modelo == "lineal":
    esfuerzo_estimado_200 = a * LOC_estimar_200 + b
else:
    esfuerzo_estimado_200 = k * (LOC_estimar_200 ** b_exp)

print(f"Esfuerzo estimado para LOC={LOC_estimar_200} es: {esfuerzo_estimado_200:.4f} PM")

# Graficar los resultados
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')

if mejor_modelo == "lineal":
    plt.plot(df['LOC'], a*df['LOC']+b, label=f'Modelo lineal (R²={r_value_lineal:.2f})', color='red')
else:
    plt.plot(df['LOC'], k*(df['LOC']**b_exp), label=f'Modelo exponencial (R²={r_value_exponencial:.2f})', color='green')

plt.scatter(LOC_estimar_9100, esfuerzo_estimado_9100, color='blue', label=f'Estimación LOC=9100 ({esfuerzo_estimado_9100:.2f} PM)')
plt.scatter(LOC_estimar_200, esfuerzo_estimado_200, color='purple', label=f'Estimación LOC=200 ({esfuerzo_estimado_200:.2f} PM)')

plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()
