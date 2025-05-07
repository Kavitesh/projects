#define TOUCH_PIN T0  // GPIO4 (Can be changed to T1, T2, etc.)

void setup() {
    Serial.begin(19600);
    Serial.println("ESP32 Touch Sensor Started");
}

void loop() {
    int touchValue = touchRead(TOUCH_PIN);
    Serial.print("Touch Value: ");
    Serial.println(touchValue);
    delay(500);
}
