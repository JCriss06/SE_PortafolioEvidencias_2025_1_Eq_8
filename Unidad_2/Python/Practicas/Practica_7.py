import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

#Solo es para encontrar la d (Diferenciacion)
import Practica_4 as p4
if __name__ == "__main__":
    archivo = p4.lecturaArchivo("lecturaFoto.csv")
    ipl = p4.interpolacionLineal(archivo)
    # En esta practica no tratamos los outliers ni hacemos el suavizamiento exponencial
    # Solo nos interesa la diferenciación (d)
    datos = ([fila[1] for fila in ipl])
    print(f"Solo valor: {datos}")

    # Prueba de ADF en la serie original
    resultado = adfuller(datos)
    print(f"p-valor serie original: {resultado[1]}")  # Si p > 0.05, diferenciamos

    # Primera diferenciación (d = 1)
    datos_d1 = np.diff(datos)
    resultado_d1 = adfuller(datos_d1)
    print(f"p-valor con d=1: {resultado_d1[1]}")  # Si sigue p > 0.05, diferenciamos otra vez

    # Segunda diferenciación (d = 2)
    datos_d2 = np.diff(datos_d1)
    resultado_d2 = adfuller(datos_d2)
    print(f"p-valor con d=2: {resultado_d2[1]}")  # Si p < 0.05, la serie ya es estacionaria

    # Graficamos las series
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.plot(datos, marker='o')
    plt.title("Serie original")

    plt.subplot(1, 3, 2)
    plt.plot(datos_d1, marker='o')
    plt.title("Serie diferenciada (d=1)")

    plt.subplot(1, 3, 3)
    plt.plot(datos_d2, marker='o')
    plt.title("Serie diferenciada (d=2)")

    plt.show()
