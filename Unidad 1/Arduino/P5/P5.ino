//Programa 5
//controla la intensidad de una señal PWM
int pinPWM = 6; //modulacion por ancho de pulso 
//obtiene resultados analogicos con medio digitales = ondad cuadrada que se alterna entre endendido y apagado
void setup() { 
  //pinMode(pinPWM, OUTPUT); nose si va
  Serial.begin(9600);
}

void loop() {
  for(int i = 0; i<255; i++){
    analogWrite(pinPWM,i);
    delayMicroseconds(100000);
  }
  delay(10);

  for (int i = 255; i > 0; i--){
    analogWrite(pinPWM,i);
    delayMicroseconds(100000);
  }
  delay(10);
}
