import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('datos.csv')

# Calcular media, mediana y desviación estándar
for columna in df.columns:
    print(f"--- {columna} ---")
    print(f"Media: {df[columna].mean()}")
    print(f"Mediana: {df[columna].median()}")
    print(f"Desviación estándar: {df[columna].std()}")
    print()

# Crear scatter plot
plt.scatter(df['Columna1'], df['Columna2'])
plt.xlabel('Columna1')
plt.ylabel('Columna2')
plt.title('Dispersión Columna1 vs Columna2')
# Calcular regresión lineal
import numpy as np

x = df['Columna1'].values
y = df['Columna2'].values
coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)

# Dibujar línea de tendencia
plt.plot(x, poly1d_fn(x), color='red', linestyle='--', label='Tendencia lineal')

plt.legend()
plt.show()

# Guardar estadísticas en 'reporte.txt'
with open('reporte.txt', 'w') as f:
    for columna in df.columns:
        f.write(f"--- {columna} ---\n")
        f.write(f"Media: {df[columna].mean()}\n")
        f.write(f"Mediana: {df[columna].median()}\n")
        f.write(f"Desviación estándar: {df[columna].std()}\n\n")
    f.write("Regresión lineal (Columna1 -> Columna2):\n")
    f.write(f"y = {coef[0]:.4f}x + {coef[1]:.4f}\n")