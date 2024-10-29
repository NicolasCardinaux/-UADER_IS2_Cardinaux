// La función setup se ejecuta una vez cuando presionas reset o enciendes la placa
void setup() { 
  // Inicializa el pin digital LED_BUILTIN como una salida 
  pinMode(LED_BUILTIN, OUTPUT); 
} 

void loop() { 
  // Secuencia 1: Encender 800 ms y apagar 800 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(800);                       // espera 800 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(800);                       // espera 800 ms 
  } 
  // Mantener el LED apagado por 2400 ms 
  delay(2400); 

  // Secuencia 2: Encender 2400 ms y apagar 2400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(2400);                      // espera 2400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(2400);                      // espera 2400 ms 
  } 
  // Mantener el LED apagado por 2400 ms 
  delay(2400); 
  
  // Secuencia 3: Encender 800 ms y apagar 800 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(800);                       // espera 800 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(800);                       // espera 800 ms 
  } 
  // Mantener el LED apagado por 7200 ms 
  delay(7200); 
} 
