import csv
import matplotlib.pyplot as plt
import math
import numpy as np
import random as rnd

from Unidad_2.SuavizamientoExponencial import MetricasDeError as errores
from Unidad_2.SuavizamientoExponencial import SuavizamientoSimple_SensibilidadDeParametros as ssp

def lecturaArchivo(archivo): #sabemos que puede haber valores nulos
    with open(archivo, "r") as file:
        reader = csv.reader(file)
        next(reader)
        datos = [list(map(str,linea[:2]))for linea in reader]
        print("Original:",datos)
        return datos

def interpolacionLineal(datos):
    for i in range(len(datos)):
        x, y = datos[i]
        if y == "":
            for j in range(i-1, -1, -1):
                if datos[j][1] != "":
                    x1, y1 = int(datos[j][0]), int(datos[j][1])
                    break
            for j in range(i+1, len(datos)):
                if datos[j][1] != "":
                    x2, y2 = int(datos[j][0]), int(datos[j][1])
                    break

            datos[i][1] = int(y1 + (((y2) - (y1))/((x2) - (x1))) * (int(x) - (x1)))
    d = [[int(valor) for valor in fila] for fila in datos]
    print("Interpolation:",d)
    return d

def identificaOutliers(matriz):
    val = [fila[1] for fila in matriz]
    plt.boxplot(val)
    plt.title("Boxplot Basico")
    plt.show()

def trataOutliers(matriz):
    matriz.sort(key=lambda x: x[1])
    print("Sort Dataset: ", matriz)

    posQ1 = 1*(len(matriz)-1)/4 + 1
    posQ3 = 3*(len(matriz)-1)/4 + 1

    p_decimal, p_entera = math.modf(posQ1)
    p_entera = int(p_entera)
    Q1 = matriz[p_entera-1][1] + p_decimal*(matriz[p_entera][1]-matriz[p_entera-1][1])

    p_decimal, p_entera = math.modf(posQ3)
    p_entera = int(p_entera)
    Q3 = matriz[p_entera-1][1] + p_decimal*(matriz[p_entera][1]-matriz[p_entera-1][1])

    print("Q1-Position: ", posQ1, " Q1 Value: ", Q1)
    print("Q3-Position: ", posQ3, " Q3 Value: ", Q3)

    IQR = Q3-Q1
    print("IQR: ", IQR)

    whiskers = 1.5

    lower_limit = Q1 - whiskers*IQR
    upper_limit = Q3 + whiskers*IQR
    print("LOWER LIMIT: ", lower_limit, " UPPER LIMIT: ", upper_limit)

    auxiliar = []
    for fila in matriz:
        if fila[1] < lower_limit or fila[1] > upper_limit:
            print("Outlier: ", fila)
        else:
            auxiliar.append(fila)
    dataset = auxiliar.copy()
    print("Without outliers:",dataset)

    rnd.shuffle(dataset)
    print("Shuffle Dataset: ", dataset)
    return dataset

def findAlfa(matriz):
    datos = np.array([fila[1] for fila in matriz])

    alfas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    minErorr = 1000
    best_alfa = -1
    for alfa in alfas:
        serie_suavizada = ssp.calc_suavizado_exponencial(datos, alfa)

        #errorMAE = errores.calcMAE(datos, serie_suavizada)
        #errorMSE = errores.calcMSE(datos, serie_suavizada)
        errorRMSE = errores.calcRMSE(datos, serie_suavizada)
        #errorMAPE = errores.calcMAPE(datos, serie_suavizada)

        if minErorr>errorRMSE:
            minErorr  = errorRMSE
            best_alfa = alfa
    print("Best alfa: ", best_alfa)

    x = []
    for i in range(1, len(serie_suavizada) + 1):  # generar el total de valores que se usaran para tabular y graficar las series
        x.append(i)
    plt.figure(figsize=(12, 6))
    plt.plot(x, datos, label='REAL', color='blue')
    plt.plot(x, serie_suavizada, label='SUAVIZADA', color='green')
    plt.title('Comparación de Series')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    lecturas = ["lecturaFoto.csv", "lecturaFotoS2.csv"]
    for lectura in lecturas:
        print("Lectura: ", lectura)
        file = lecturaArchivo(lectura)
        ipl = interpolacionLineal(file) #matriz
        identificaOutliers(ipl) #represemtacion visual
        outgood = trataOutliers(ipl) #outliers
        findAlfa(outgood) #alfa y visualizacion
        print("\n")
    ''' 
    file = lecturaArchivo("lecturaFoto.csv")
    ipl = interpolacionLineal(file) #matriz
    identificaOutliers(ipl) #represemtacion visual
    outgood = trataOutliers(ipl) #outliers
    findAlfa(outgood) #alfa y visualizacion
    '''