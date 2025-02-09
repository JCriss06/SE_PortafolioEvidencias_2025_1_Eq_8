import csv
def leer_datos():
    import serial as conn
    arduino = conn.Serial(port="COM6", baudrate=9600, timeout=1)
    cadena = []
    while len(cadena) < 8: #ajustable
        cadena.append(arduino.readline().decode().strip())
    return cadena

def valida1v2(cadena):
    new_items = [i for i in cadena if i != '']
    print("sin vacios:",new_items)
    validos = []
    for i in new_items:
        items = list(i)
        #print("con IF",items)
        if items[0] == "I" and items[-1] == "F":
            del items[0]
            del items[-1]
        #print(items)
            limpio = ''.join(items)
            #print("sin -:",limpio)
            if limpio.count(' - ') == 3:
                partes = limpio.split(' - ') #retorna una lista
                int_partes = [int(i) for i in partes]
                validos.append(int_partes)
            #print("elementos validos:", int_partes)
    return validos

def vo(vector):
    valobj = sum([i ** 2 for i in vector])
    return valobj

def procesa(cadena):
    resultados = []
    validos = valida1v2(cadena)
    for i in validos:
        objetivo = vo(i)
        resultados.append(i + [objetivo])
        #print(resultados)
    return resultados

def escritura(vector):
    with open("resulverif.csv", mode="w", newline="") as archivo:
        escritura = csv.writer(archivo)
        for fila in vector:
            escritura.writerow(fila)

if __name__ == "__main__":
    pa = leer_datos()
    print("original:",pa)

    pb = procesa(pa)

    for res in pb:
        print(res)

    escritura(pb)


