// Sensor Ultrasónico y Arduino UNO
// by Daniel Alvarez

// Definir de pines
#define TRIGGER_PIN 7
#define ECHO_PIN 6
#define BUZZER_PIN 8
#define LED_PIN 10

// // // SETUP // // //

void setup() {
  //Comunicación serial a 9600 baudios para la depuración
  Serial.begin(9600);
  
  //  Entradas y salidas
  pinMode(TRIGGER_PIN, OUTPUT);  // Pin sensor ultrasónico (salida)
  pinMode(ECHO_PIN, INPUT);      // Pin eco del sensor ultrasónico (entrada)
  pinMode(BUZZER_PIN, OUTPUT);   // Pin Buzzer (salida)
  pinMode(LED_PIN, OUTPUT);      // Pin del LED (salida)
}

// // // LOOP // // //

void loop() {
  
  long duration, distance;
  
  // Generar un pulso corto para activar el sensor ultrasónico
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  
  // Medir la duración del eco para determinar la distancia
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;  // Calcular la distancia en centímetros
  
  // Imprimir
  Serial.print(""); 
  Serial.println(distance);  
  
  // Verificar si la distancia es menor o igual a 10 centímetros
  if (distance <= 10) {
    // Encender el LED y activar el zumbador durante 300 ms
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    delay(300);
    digitalWrite(BUZZER_PIN, LOW);
    
    // delay antes de realizar la siguiente verificación
    delay(4000);
  } else {
    // Apagar el LED si la distancia es mayor a 10 centímetros
    digitalWrite(LED_PIN, LOW);
  }
  
  // delay antes de realizar la siguiente iteración del bucle principal
  delay(100);
}
