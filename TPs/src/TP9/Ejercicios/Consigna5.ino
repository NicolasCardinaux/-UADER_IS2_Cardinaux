// the setup function runs once when you press reset or power the board 
void setup() { 
  // initialize digital pin LED_BUILTIN as an output. 
  pinMode(LED_BUILTIN, OUTPUT); 
} 

void loop() { 
  // Secuencia 1: Encender 800 ms y apagar 800 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(800);                       // wait for 800 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(800);                       // wait for 800 ms 
  } 
  // Mantener el LED apagado por 2400 ms 
  delay(2400); 

  // Secuencia 2: Encender 2400 ms y apagar 2400 ms, repetir tres veces 
  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(2400);                      // wait for 2400 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(2400);                      // wait for 2400 ms 
  } 
  // Mantener el LED apagado por 2400 ms 
  delay(2400); 
  // Secuencia 3: Encender 800 ms y apagar 800 ms, repetir tres veces 

  for (int i = 0; i < 3; i++) { 
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on 
    delay(800);                       // wait for 800 ms 
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off 
    delay(800);                       // wait for 800 ms 
  } 
  // Mantener el LED apagado por 7200 ms 
  delay(7200); 
} 