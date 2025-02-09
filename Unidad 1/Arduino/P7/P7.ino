//Programa 7
int sensor = A0;
int actuador = 6;

void setup() {
  pinMode(actuador, OUTPUT);//no se si va
  Serial.begin(9600);
}

int v;
void loop() {
  v = analogRead(sensor);
  v = map(v, 0, 1023,0,255);
  analogWrite(actuador,v);
  delay(100);
}
