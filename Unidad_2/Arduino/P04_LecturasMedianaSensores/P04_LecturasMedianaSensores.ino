//MEDIANA
int sensor = A0;
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30]; //vector

void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  //Ordenamiento del vector ( Burbuja )
  for(int i = 0; i<totalLecturas; i++){
    for(int j= i+1; j<totalLecturas-1; j++){      
      if(valor[j] < valor[i]){
        //swap
        int temp = valor[i];
        valor[i] = valor[j];
        valor[j] = temp;
      }
    }
  }
  //Ejercicio 1 - Moda
  Serial.println(valor[totalLecturas/2]);
  delay(10);
}