//Programa 8
//convierte el ranfo 0 -1023 a 0 - 255
int sensor = A0;
int actuador = 6;

void setup() {
  pinMode(actuador, OUTPUT);
  Serial.begin(9600);
}

int v;
void loop() {
  v = analogRead(sensor);
  v = v / 4; 
  analogWrite(actuador,v);
  delay(100);
}
