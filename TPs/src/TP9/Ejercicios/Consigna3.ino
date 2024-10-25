// the setup function runs once when you press reset or power the board 
void setup() { 
  // initialize digital pin LED_BUILTIN as an output. 
  pinMode(LED_BUILTIN, OUTPUT); 
} 

// the loop function runs over and over again forever 
void loop() { 
  // Secuencia 1: Encender 400 ms y apagar 400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(400);                       // wait for 400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(400);                       // wait for 400 ms 
  } 

  // Mantener el LED apagado por 1200 ms 
  delay(1200); 
  // Secuencia 2: Encender 1200 ms y apagar 1200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(1200);                      // wait for 1200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(1200);                      // wait for 1200 ms 
  } 

  // Mantener el LED apagado por 1200 ms 
  delay(1200); 

  // Secuencia 3: Encender 400 ms y apagar 400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(400);                       // wait for 400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(400);                       // wait for 400 ms 
  } 
  // Mantener el LED apagado por 3600 ms 
  delay(3600); 
  // Volver a repetir el ciclo 
} 