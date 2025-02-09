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

/*
//SENSOR PIR
int sendord = 7;
void setup(){
  Serial.begin(9600);
  pinMode(sendord, INPUT);
}
int v;
void loop(){
  v = digitalRead(sendord);
  Serial.println(v);
  delay(1000);
}
*/