import random as rnd
import csv
import numpy as np

def generaVa():
    externa = []
    for i in range(30):  # filas
        interna = []
        for j in range(100):  # columnas
            # Valores de configuracion maximos y minimos con respecto a la temperatura, humedad, ruido y luminosidad
            tem = rnd.randint(18, 40)
            hum = rnd.randint(35, 160)
            rui = rnd.randint(50, 240)
            lum = rnd.randint(400, 1200)
            interna.append([tem, hum, rui, lum])
        externa.append(interna)
    print(externa)
    return externa

Vas = generaVa()

#data = np.array([item for sublist in Vas for item in sublist])
#iqr_values = np.percentile(data, 75, axis=0) - np.percentile(data, 25, axis=0)
#print("IQR por columna:", iqr_values)

with open('Practica_1/va_generados.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    num_columns = len(Vas[0])
    headers = [f"Va_{i + 1}" for i in range(num_columns)]
    writer.writerow(headers)

    for fila in Vas:
        writer.writerow(fila)  # Guardar cada fila como lista

    #writer.writerow(list(iqr_values))

print("Valores guardados")