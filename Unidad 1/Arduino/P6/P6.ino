//Programa 6
//muestra el timepo en milisegundos desde que comenzo el programa
long v;

void setup() {
  Serial.begin(9600);
}

void loop() {
  v = millis();
  Serial.println(v);
  delay(100);
}
