//MODA
int sensor = A0;

void setup() {
  Serial.begin(9600);
}
int totalLecturas = 30;
int valor[30]; //vector

void loop() {
  for (int i = 0; i < totalLecturas; i++){
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  int maxrepe = 0;
  int moda = 0;
  for (int i = 0; i < totalLecturas; i++){
    repeticiones = 0;
    for (int j = 0; j < totalLecturas; j++){
      if(valor[i] == valor[j])
          repeticiones++;
      if(repeticiones > maxrepe){
        moda = valor[i];
        maxrepe = repeticiones;
      }
    }
  }
  Serial.println(moda);
}