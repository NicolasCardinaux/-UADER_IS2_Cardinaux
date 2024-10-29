// La función setup se ejecuta una vez cuando presionas reset o enciendes la placa
void setup() { 
  // Inicializa el pin digital LED_BUILTIN como una salida
  pinMode(LED_BUILTIN, OUTPUT); 
} 
 
// La función loop se ejecuta una y otra vez indefinidamente
void loop() { 
  // Secuencia 1: Encender 200 ms y apagar 200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(200);                       // espera 200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(200);                       // espera 200 ms 
  } 
  // Mantener el LED apagado por 600 ms 
  delay(600); 

  // Secuencia 2: Encender 600 ms y apagar 600 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(600);                       // espera 600 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(600);                       // espera 600 ms 
  } 
  // Mantener el LED apagado por 600 ms 
  delay(600); 

  // Secuencia 3: Encender 200 ms y apagar 200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // enciende el LED 
    delay(200);                       // espera 200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // apaga el LED 
    delay(200);                       // espera 200 ms 
  } 
  // Mantener el LED apagado por 1800 ms 
  delay(1800); 
  // Volver a repetir el ciclo 
} 
