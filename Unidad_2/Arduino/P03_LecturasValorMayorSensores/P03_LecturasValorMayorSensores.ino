//VALOR MAYOR
int sensor = A0;
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30]; //vector
int valorMayor = -1; 

void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }
  valorMayor = -1; //valor mas chico que el que se puede leer
  for (int i = 0; i < totalLecturas; i++) {
    if(valor[i] > valorMayor){
      valorMayor = valor[i];
    }
  }
  Serial.println(valorMayor);
  delay(10);
}