import decimal
import random as rnd
import math as mt

xmin = -10
xmax = 10

def crea_solucion(n):
    v = [rnd.randint(xmin, xmax) for i in range(n)]
    return v

def solucion_vecina(solucion):
    vector = solucion[:]
    index = rnd.randint(0, len(solucion)-1)
    nuevo_valor = rnd.randint(xmin, xmax)
    vector[index] = nuevo_valor
    return vector

def evaluar(solucion): #funcion objetivo
    vo = sum(i**2 for i in solucion)
    return vo

def proporcion():
    proporcion = [i for i in range(0.8, 0.999, 0.001)]
    return proporcion

def generar_proporciones(start=0.8, end=0.999, step=0.001):
    return [start + i * step for i in range(int((end - start) / step) + 1)]

if __name__ == "__main__":
    T = 1000
    u = 0.05
    e = mt.e

    So = crea_solucion(5)
    SBest = So[:]
    VBest = evaluar(SBest)
    pro = generar_proporciones()
    #pro = proporcion()
    ''' 
    do
        Saux = SBest
        Stemp = SBest #mejor actual
        Votemp = evaluar(Stemp)
        for(k = 0; k < 100; k++ ): # 100 = maxit
            Saux = solucion_vecina(Saux)
            Vo = evaluar(Saux)
            dif = Vo - Votemp
            if (dif < 0):
                Stemp = Saux #[:]
                Votemp = Vo
            else:
                i = rnd.uniform(0,1)
                if(i < e**(dif/T)):
                    Stemp = Saux #[:]
            T = T * proporcion()
        if(Votemp < VBest):
            SBest = Stemp
            VBest = Votemp
    while(T > u):
    '''

    #-------------------
    while True: #while con condicion
        Saux = SBest[:]
        Stemp = SBest[:]
        Votemp = evaluar(Stemp)
        for k in range(100): #while con condicion
            Saux = solucion_vecina(Saux)
            Vo = evaluar(Saux)
            dif = Vo - Votemp
            if dif < 0:
                Stemp = Saux[:]
                Votemp = Vo
            else: # la solicion es mala per hay que darle la oportunidad
                i = rnd.uniform(0, 1) #random

                if i < e ** (dif / T):
                    Stemp = Saux[:]
            for p in pro:
                T = T * p
        if Votemp < VBest:
            SBest = Stemp[:]
            VBest = Votemp
        if T <= u:
            break

    print("Mejor solución:", SBest)
    print("Mejor valor de la función objetivo:", VBest)