// La función setup se ejecuta una vez cuando presionas reset o enciendes la placa
void setup() { 
  // Inicializa el pin digital LED_BUILTIN como una salida
  pinMode(LED_BUILTIN, OUTPUT); 
} 

// La función loop se ejecuta repetidamente para siempre
void loop() { 
  // Secuencia 1: Encender 400 ms y apagar 400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // Enciende el LED
    delay(400);                       // Espera 400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // Apaga el LED
    delay(400);                       // Espera 400 ms 
  } 

  // Mantener el LED apagado por 1200 ms 
  delay(1200); 

  // Secuencia 2: Encender 1200 ms y apagar 1200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // Enciende el LED
    delay(1200);                      // Espera 1200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // Apaga el LED
    delay(1200);                      // Espera 1200 ms 
  } 

  // Mantener el LED apagado por 1200 ms 
  delay(1200); 

  // Secuencia 3: Encender 400 ms y apagar 400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // Enciende el LED
    delay(400);                       // Espera 400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // Apaga el LED
    delay(400);                       // Espera 400 ms 
  } 

  // Mantener el LED apagado por 3600 ms 
  delay(3600); 

  // Volver a repetir el ciclo 
}
