from datetime import datetime
import time as tm
import serial as conn
# con el modulo serial se puede leer el puerto serial de la computadora
intervalo = 5 * 60# minutos
nolectura = 1 # lectura en la que va
maxecturas = 144 # hasta donde llega

estado_archivo = "estado_lectura.txt"

arduino = conn.Serial(port="COM3", baudrate=9600, timeout=1)

with open("lecturaFoto.csv", "w") as archivo:
    archivo.write("No.Lectura,Valor,Fecha,Hora\n")

    while nolectura <= maxecturas:
        tm.sleep(intervalo)
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode().strip()

            fecha = datetime.today().strftime("%Y-%m-%d")
            hora = datetime.today().strftime("%H:%M:%S")

            archivo.write(f"{nolectura},{linea},{fecha},{hora}\n")
            print(f"Lectura: {nolectura}, Valor:{linea}, Fecha: {fecha}, Hora:{hora}\n")
            nolectura += 1

arduino.close()