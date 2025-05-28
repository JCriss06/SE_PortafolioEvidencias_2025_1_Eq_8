//Progama 1
int sensor = A0;

void setup() {
  Serial.begin(9600);
}

int v ;

void loop() {
  v = analogRead(sensor);
  Serial.println(v);
  Serial.println("Hola");
  delay(1000);
}
