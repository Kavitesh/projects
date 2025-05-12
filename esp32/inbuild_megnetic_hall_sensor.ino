#define LED1 2  // Built-in LED on GPIO2
#define LED2 4
#define LED3 5

void setup() {
    Serial.begin(19600);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    Serial.println("ESP32 Hall Sensor LED Control Started");
}

void loop() {
    int hallValue = hallRead();  // Read Hall sensor
    Serial.print("Hall Sensor Value: ");
    Serial.println(hallValue);

    // Control LEDs based on Hall sensor reading
    if (hallValue > 50) {
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
    } else if (hallValue < -50) {
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, HIGH);
        digitalWrite(LED3, LOW);
    } else {
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, HIGH);
    }

    delay(500);
}
