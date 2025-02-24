//Programa 12
int sensor = A0;

void setup() {
  Serial.begin(9600);
}

int v;

void loop() {
   v = analogRead(sensor);
  Serial.println("Valor: " + String(v));
  delay(100);
}
