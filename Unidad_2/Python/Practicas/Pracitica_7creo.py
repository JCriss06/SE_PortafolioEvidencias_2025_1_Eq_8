import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def findStacionarity(datos):
    # Prueba de ADF en la serie original
    resultado = adfuller(datos)
    print(f"p-valor serie original: {resultado[1]}")  # Si p > 0.05, diferenciamos
    if resultado[1] > 0.05:
        print("direrenciamos")
        return 0

    # Primera diferenciación (d = 1)
    datos_d1 = np.diff(datos)
    resultado_d1 = adfuller(datos_d1)
    print(f"p-valor con d=1: {resultado_d1[1]}")  # Si sigue p > 0.05, diferenciamos otra vez
    if resultado_d1[1] > 0.05:
        print("diferenciamos de nuevo")
        return 1

    # Segunda diferenciación (d = 2)
    datos_d2 = np.diff(datos_d1)
    resultado_d2 = adfuller(datos_d2)
    print(f"p-valor con d=2: {resultado_d2[1]}")  # Si p < 0.05, la serie ya es estacionaria
    if resultado_d2[1] < 0.05:
        print("La serie es estacionaria")
        return 2

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

import Practica_4 as p4
if __name__ == "__main__":
    file = p4.lecturaArchivo("lecturaFoto.csv")
    ipl = p4.interpolacionLineal(file)
    #checar si detecta los outliers o no
    datos = [i[1]for i in p4.trataOutliers(ipl)] #outgood (los que no tienen outliers)

    print("Solo valores de shuffler: ", datos)

    #d = findStacionarity(datos)
    #print("Valor de (d):",d)

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

