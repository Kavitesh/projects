#define PULSE_PIN 18  // Pin to receive pulses

void setup() {
    Serial.begin(19600);
    pinMode(PULSE_PIN, INPUT_PULLUP);
    Serial.println("ESP32 Pulse Counter Started");
}

void loop() {
    int pulse = digitalRead(PULSE_PIN);
    Serial.print("Pulse State: ");
    Serial.println(pulse);
    delay(100);
}
