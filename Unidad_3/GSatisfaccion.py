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

if __name__ == "__main__":
    # min, max, weight
    valconfi = [[20, 28, 0.4],
                [40, 80, 0.2],
                [60, 120, 0.1],
                [400, 900, 0.3]]

    #valores optimizados
    datos = [20,70,95,600]
    gsatisfaccion = calcular_Gsat(valconfi, datos)
    print(f"Ganancia Satisfaccion: {gsatisfaccion}")

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