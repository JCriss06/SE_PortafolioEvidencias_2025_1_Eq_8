/*
  Practica Unidad 2
*/
int obtener_Menor(int valor[]) {
  int valorMenor = 1024;
  for (int i = 0; i < 30; i++) {
    if (valor[i] < valorMenor) {
      valorMenor = valor[i];
    }
  }

  return valorMenor;
}

int obtener_Mayor(int valor[]) {
  int valorMayor = -1;
  for (int i = 0; i < 30; i++) {
    if (valor[i] > valorMayor) {
      valorMayor = valor[i];
    }
  }

  return valorMayor;
}

int obtener_Mediana(int v[]) {
  for (int i = 0; i < 30; i++) { // Bubble Sort
    for (int j = i + 1; j < 30 - 1; j++) {
      if (v[j] < v[i]) {
        int temp = v[i];
        v[i] = v[j];
        v[j] = temp;
      }
    }
  }
  
  return v[30 / 2];
}

int obtener_Media(int valor[]) {
  int avg = 0;
  for (int i = 0; i < 30; i++) {
    avg += valor[i];
  }
  
  avg /= 30;

  return avg;
}
/////////////////////////////////////////////////
int obtener_Moda(int valor[]){
  int maxrepe = 0;
  int moda = 0;
  for (int i = 0; i < 30; i++){
    int repeticiones = 0;
    for (int j = 0; j < 30; j++){
      if(valor[i] == valor[j])
          repeticiones++;
      if(repeticiones > maxrepe){
        moda = valor[i];
        maxrepe = repeticiones;
      }
    }
  }
  return moda;
}

int sensor[] = { A0, A1, A2, A3 }; //agregar los otros pines 6 en total
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;
int sensorMedia[30];//vector
int sensorMediana[30];
int sensorMenor[30];
int sensorMayor[30];
int sensorModa[30];

void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    sensorMedia[i] = analogRead(sensor[0]);
    sensorMediana[i] = analogRead(sensor[1]);
    sensorMenor[i] = analogRead(sensor[2]);
    sensorMayor[i] = analogRead(sensor[3]);
    delayMicroseconds(100);
  }

  int a = obtener_Media(sensorMedia);
  int b = obtener_Mediana(sensorMediana);
  int c = obtener_Mayor(sensorMayor);
  int d = obtener_Menor(sensorMenor);

  Serial.println(String(a) + ',' + String(b) + ',' + String(c) + ',' + String(d));
  
  delay(1000);
}