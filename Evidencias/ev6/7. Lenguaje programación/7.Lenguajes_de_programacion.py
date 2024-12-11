# -*- coding: utf-8 -*-
"""Copia de Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JrHcoRmpAq1IsmbZQfJPf0nf_JCrUNTb
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos desde un archivo CSV
archivo_csv = 'Lenguajes_uso_frecuencia.csv'  # Asegúrate de tener el archivo con este nombre
df = pd.read_csv(archivo_csv)

# Calcular el porcentaje de uso aproximado basado en la frecuencia "Siempre"
df["Total"] = df[["Siempre", "Frecuentemente", "Algunas veces", "Rara vez", "Nunca"]].sum(axis=1)
df["Porcentaje de Uso"] = (df["Siempre"] / df["Total"]) * 100

# Crear un índice ficticio como variable independiente
df = df.sort_values(by="Porcentaje de Uso", ascending=False).reset_index(drop=True)
df["Ranking"] = np.arange(1, len(df) + 1)

# Separar las variables independiente (Ranking) y dependiente (Uso)
X = df[["Ranking"]].values  # Variable independiente
y = df["Porcentaje de Uso"].values  # Variable dependiente

# Crear y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Generar predicciones
y_pred = model.predict(X)

# Mostrar los coeficientes del modelo
print("Pendiente (coeficiente):", model.coef_[0])
print("Intercepto:", model.intercept_)

# Graficar los datos reales y la regresión lineal
plt.figure(figsize=(12, 6))
plt.scatter(df["Ranking"], df["Porcentaje de Uso"], color="blue", label="Datos reales")
plt.plot(df["Ranking"], y_pred, color="red", label="Regresión Lineal")

# Etiquetas y título
plt.xlabel("Ranking de Lenguajes de Programación")
plt.ylabel("Porcentaje de Uso (%)")
plt.title("Regresión Lineal sobre Popularidad de Lenguajes de Programación")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar el gráfico
plt.show()