//Sintesis de lo que se debe de agarrar
/*
//MEDIA ARITMETICA O PROMEDIO
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

  int avg = 0;
  for (int i = 0; i < totalLecturas; i++) {
    avg += valor[i];
  }
  
  avg /= totalLecturas;

  Serial.println(avg);

  delay(10);
}
*/

//LECTURA FOTORESISTOR
int sensor = A0;

void setup() {
  Serial.begin(9600);
}

int v;
void loop() {
  v = analogRead(sensor);
  Serial.println(v);
  delay(1000);
  //delayMicroseconds(1000000);
}
