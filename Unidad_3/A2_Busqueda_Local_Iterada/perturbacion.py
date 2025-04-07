import random as rnd
xmin = -10
xmax = 10
def perturbacion(solucion): #modificacion brusca de la solucion
    vector = solucion[:]
    print("original",vector)
    index1 = rnd.randint(0, len(solucion) - 1)
    index2 = index1
    while index2 == index1:
        index2 = rnd.randint(0, len(solucion) - 1)

    nuevo_valor1 = rnd.randint(xmin, xmax)
    nuevo_valor2 = rnd.randint(xmin, xmax)

    vector[index1] = nuevo_valor1
    vector[index2] = nuevo_valor2
    print("con perturbacion ",vector)
    return vector

def perturbacion_Range(solucion):
    vector = solucion[:]
    print("original",vector)
    index1 = rnd.randint(0, len(solucion) - 1)
    for i in range(index1, len(solucion)):
        vector[i] = rnd.randint(xmin, xmax) # apartir del index hasta el final
    print("con perturbacion ",vector)
    return vector

def perturbacion_ELevada(So): #nultiplicar la solucion por su index
    vector = So[:]
    idx = rnd.randint(0, len(So) - 1)
    for i in range(idx):
        vector[i] **= i
    return vector

solucion_temporal = [3,1,2,5,4] # Solucion inicial
#perturbacion(solucion_temporal)
perturbacion_Range(solucion_temporal)
#perturbacion2(solucion_temporal)
