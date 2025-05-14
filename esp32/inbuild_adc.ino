#define ANALOG_PIN 34  // Any ADC1 pin (34, 35, 36, 39)

void setup() {
    Serial.begin(19600);
    Serial.println("ESP32 ADC Started");
}

void loop() {
    int sensorValue = analogRead(ANALOG_PIN);
    Serial.print("Analog Value: ");
    Serial.println(sensorValue);
    delay(500);
}
