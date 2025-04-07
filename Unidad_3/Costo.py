def calcular_ss(valor, min_val, max_val, s4=False):
    if s4:
        #maximizacion
        return (1 - ((max_val - valor) / (max_val - min_val)))
    else:
        #minimizacion
        return ((max_val - valor) / (max_val - min_val))

def calcular_Gsat(valconfi, datos):
    gsatisfaccion = 0
    for i in range(len(valconfi)):
        v_analizar = datos[i]
        vmin = valconfi[i][0]
        vmax = valconfi[i][1]
        preferencia  = i == 3
        wservicio = valconfi[i][2]
        ssl = calcular_ss(v_analizar, vmin, vmax, preferencia)
        gsatisfaccion += ssl * wservicio
    return gsatisfaccion
#########################################
def mininizar(va, vo, vmin, vmax, c):
    if va >= vo:
        e0 = c + c *(va - vo)
    else:
        e0 = 0
    if va >= vmax:
        emin = c + c *(va - vmax)
    else:
        emin = 0
    if va >= vmin:
        emax = c + c *(va -vmin)
    else:
        emax = 0
    return e0, emin, emax

def maximizar(va, vo, vmin, vmax, c):
    if va <= vo:
        e0 = c + c *(vo - va)
    else:
        e0 = 0
    if va <= vmin:
        emin = c + c *(vmin - va)
    else:
        emin = 0
    if va <= vmax:
        emax = c + c *(vmax - va)
    else:
        emax = 0
    return e0, emin, emax

def normalizacion(e0, emin, emax):
    return (1 - (e0 - emin) / (emax - emin))

def obtener_e(valconfi, datos, va):
    normaliza = []
    #nor = 0
    for i in range(len(valconfi)):
        temp = -1#
        if 0 <= i <= 2:
            vact, vo, vmin, vmax, wser, c = va[i], datos[i], valconfi[i][0], valconfi[i][1], valconfi[i][2], valconfi[i][3]
            if vact>= vmin:# todo abajo
                e0, emin, emax = mininizar(vact, vo, vmin, vmax, c)
                nor = normalizacion(e0, emin, emax)
            else:
                nor = 1 * wser
            #print(f"e0: {e0}, emin: {emin}, emax: {emax}")
        elif i == 3:
            vact, vo, vmin, vmax, c = va[i], datos[i], valconfi[i][0], valconfi[i][1], valconfi[i][3]
            e0, emin, emax = maximizar(vact, vo, vmin, vmax, c)
            #print(f"e0: {e0}, emin: {emin}, emax: {emax}")
        '''
        nor = normalizacnoion(e0, emin, emax)
        normaliza.append(nor)
        #print(f"Normalizacion: {nor}")
        
        energia = 0
        for i in range(len(normaliza)):
            wservicio = valconfi[i][2]
            energia += normaliza[i] * wservicio
        #print(f"Energia: {ganancia}")
        '''
        e = normaliza.append(nor)####
        energia = sum(e)


    return energia

def fo(Gs, a, G, b):
    return Gs * a + G * b


if __name__ == "__main__":
    a = 0.8
    b = 0.2
    # min, max, weight, cost
    valconfi = [[20, 28, 0.4, 8],#20 28 0.4 40
                [40, 80, 0.3, 3],# 40 80 0.2 25
                [60, 120, 0.1, 1],# 60 120 0.1 12
                [400, 900, 0.2, 5]]#400 900 0.3 3 maximization

    #individual
    datos = [20,70,95,600] #vo
    va = [18, 60, 90, 300] #va 24, 46, 85, 700
    Gs = calcular_Gsat(valconfi, datos) #Ganancia de Satisfaccion
    print(f"GSatisfactorio: {Gs}")
    Eng = obtener_e(valconfi, datos, va) #Energia
    print(f"Energia: {Eng}")
    Fo = fo(Gs, a, Eng, b)
    print(f"Funcion Objetivo: {Fo}")


    ''' 
    #multiple
    datos_sensores = [
        [21, 41, 76, 666],
        [23, 42, 78, 797],
        [20, 60, 90, 777]
    ]
    for i, valores in enumerate(datos_sensores):
        gsatisfactorio = calcular_Gsat(valconfi, valores)
        print(f"fila {i + 1}: {gsatisfactorio}")
        '''