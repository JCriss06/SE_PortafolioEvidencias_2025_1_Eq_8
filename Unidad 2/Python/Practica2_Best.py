from datetime import datetime
import time as tm
import serial as conn
import os

intervalo = 5 * 60   # minutos a segundos
maxlecturas = 144
estado_archivo = "s2.txt"
csv_archivo = "lecturaFotoS2.csv"
puerto = "COM3"
baudrate = 9600

def cargar_estado():
    if os.path.exists(estado_archivo):
        with open(estado_archivo, "r") as f:
            return int(f.read().strip()) + 1
    return 1

def guardar_estado(nolectura):
    with open(estado_archivo, "w") as f:
        f.write(str(nolectura))

def registrar_lectura(nolectura, valor):
    fecha = datetime.today().strftime("%Y-%m-%d")
    hora = datetime.today().strftime("%H:%M:%S")

    if not os.path.exists(csv_archivo):
        with open(csv_archivo, "w") as archivo:
            archivo.write("No.Lectura,Valor,Fecha,Hora\n")

    with open(csv_archivo, "a") as archivo:
        archivo.write(f"{nolectura},{valor},{fecha},{hora}\n")

    print(f"Lectura: {nolectura}, Valor: {valor}, Fecha: {fecha}, Hora: {hora}")

def main():
    nolectura = cargar_estado()
    arduino = conn.Serial(port=puerto, baudrate=baudrate, timeout=1)

    while nolectura <= maxlecturas:
        tm.sleep(intervalo)
        arduino.reset_input_buffer()  # Limpiar el buffer de entrada y solo se lea el dato mas reciente enviado por el arduino
        valor = arduino.readline().decode().strip()

        registrar_lectura(nolectura, valor)
        guardar_estado(nolectura)
        nolectura += 1

    arduino.close()

if __name__ == "__main__":
    main()