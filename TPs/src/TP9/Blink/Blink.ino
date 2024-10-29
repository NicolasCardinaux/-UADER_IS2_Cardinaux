// La función setup() se ejecuta una vez al iniciar o al resetear la placa
void setup() {
  // Inicializar el pin digital LED_BUILTIN como salida
  pinMode(LED_BUILTIN, OUTPUT);
}

// La función loop() se ejecuta repetidamente
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Encender el LED
  delay(1000);                      // Esperar 1 segundo
  digitalWrite(LED_BUILTIN, LOW);   // Apagar el LED
  delay(5000);                      // Esperar 5 segundos
}
