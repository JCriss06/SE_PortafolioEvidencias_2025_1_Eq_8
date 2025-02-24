int sensores[] = {A0, A1, A2, A3};
int actuadores[] = {8, 9, 10, 11};
int i;

void setup() {//configurados como salida
  Serial.begin(9600); // enviar y recibir datos por el serial
  Serial.setTimeout(100); // tiempo de espera para las lecturas de arduino
  for (i = 0; i < 4; i++) {
    pinMode(actuadores[i], OUTPUT);
  }
}

int valor;
void loop() { //lee y guarda los valores
  for (i = 0; i < 4; i++) {
    valor = analogRead(sensores[i]);

    valor = int(valor / 512);
    Serial.print(valor);

    digitalWrite(actuadores[i], valor);
  }
}