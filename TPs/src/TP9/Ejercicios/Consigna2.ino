// La función setup se ejecuta una vez cuando presionas reset o enciendes la placa
void setup() { 
  // Inicializa el pin digital LED_BUILTIN como una salida
  pinMode(LED_BUILTIN, OUTPUT); 
} 

// La función loop se ejecuta repetidamente para siempre
void loop() { 
  digitalWrite(LED_BUILTIN, HIGH);  // Enciende el LED (HIGH es el nivel de voltaje) 
  delay(1000);                      // Espera un segundo 
  digitalWrite(LED_BUILTIN, LOW);   // Apaga el LED (poniendo el voltaje en LOW)
  delay(5000);                      // Espera cinco segundos 
}
