import random as rnd
import numpy as np

xmin = -10
xmax = 10

def crea_solucion_vecina(solucion):
    vector = solucion[:]
    index = rnd.randint(0, len(solucion) - 1)
    nuevo_valor = rnd.randint(xmin, xmax)
    vector[index] = nuevo_valor
    return vector

def calcula_fo(solucion):
    vo = sum([i ** 2 for i in solucion])
    return vo

def crea_solucion(n):
    v = [rnd.randint(xmin, xmax) for i in range(n)]
    return v

def busqueda_local(So):
    best_solucion = So[:]
    best_vo = calcula_fo(best_solucion)
    max_it = 10000
    it = 0

    while it < max_it:
        solucion_temporal = crea_solucion_vecina(best_solucion)
        vo_temporal = calcula_fo(solucion_temporal)

        if vo_temporal < best_vo:
            best_vo = vo_temporal
            best_solucion = solucion_temporal[:]
        it += 1

    return best_vo

def genera_matriz():
    matriz = []
    for i in range(5):
        T = rnd.randint(20, 28)
        H = rnd.randint(40, 80)
        R = rnd.randint(60, 120)
        I = rnd.randint(400, 900)
        matriz.append([T, H, R, I])
    return matriz

def calcular_IQR(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    return IQR

if __name__ == "__main__":
    matriz = genera_matriz()
    resultados = []

    for vector in matriz:
        resultados_vector = []
        for _ in range(30):
            resultado = busqueda_local(vector)
            resultados_vector.append(resultado)
        IQR = calcular_IQR(resultados_vector)
        resultados.append(IQR)
        print(f"Vector: {vector}, IQR: {IQR}")

    print("Todos los IQRs calculados:", resultados)