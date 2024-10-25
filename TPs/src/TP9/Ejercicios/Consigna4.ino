// the setup function runs once when you press reset or power the board 
void setup() { 
  // initialize digital pin LED_BUILTIN as an output. 
  pinMode(LED_BUILTIN, OUTPUT); 
} 
 
// the loop function runs over and over again forever 
void loop() { 
  // Secuencia 1: Encender 200 ms y apagar 200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(200);                       // wait for 200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(200);                       // wait for 200 ms 
  } 
  // Mantener el LED apagado por 600 ms 
  delay(600); 

  // Secuencia 2: Encender 600 ms y apagar 600 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(600);                       // wait for 600 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(600);                       // wait for 600 ms 
  } 
  // Mantener el LED apagado por 600 ms 
  delay(600); 

  // Secuencia 3: Encender 200 ms y apagar 200 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(200);                       // wait for 200 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(200);                       // wait for 200 ms 
  } 
  // Mantener el LED apagado por 1800 ms 
  delay(1800); 
  // Volver a repetir el ciclo 
} 