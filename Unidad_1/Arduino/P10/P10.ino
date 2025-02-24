//Programa 10
int actuadores[4] = {8,9,10,11};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++){
    pinMode(actuadores[i], OUTPUT);
  }
  //Serial.setTimeout(100);//no va porque el readstrig espera un caracter
}

int v;
void loop() {
  if(Serial.available() > 0){
    v = Serial.readString().toInt();
    digitalWrite(actuadores[v],1);//v
    delay(100);
    digitalWrite(actuadores[v],0);
    delay(100);
  }
}
