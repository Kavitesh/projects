// ESP32 LED Blink with Serial Logging

#define LED_PIN 2  // Most ESP32 boards have an onboard LED on GPIO2

void setup() {
    Serial.begin(9600);  // Initialize Serial Monitor
    pinMode(LED_PIN, OUTPUT);  // Set LED pin as output
    Serial.println("ESP32 LED Blink Program Started");
}

void loop() {
    Serial.println("LED ON");
    digitalWrite(LED_PIN, HIGH);  // Turn LED on
    delay(1000);  // Wait 1 second

    Serial.println("LED OFF");
    digitalWrite(LED_PIN, LOW);   // Turn LED off
    delay(1000);  // Wait 1 second
}
