#define SENSOR_PIN 18  // HC-SR505 OUT to GPIO18
#define LED_PIN 2      // Onboard LED

void setup() {
    Serial.begin(19600);
    pinMode(SENSOR_PIN, INPUT);
    pinMode(LED_PIN, OUTPUT);
    Serial.println("HC-SR505 PIR Motion Sensor Initialized");
}

void loop() {
    int motionDetected = digitalRead(SENSOR_PIN);
    
    if (motionDetected == HIGH) {
        Serial.println(" Motion Detected!");
        digitalWrite(LED_PIN, HIGH);  // Turn LED ON
    } else {
        Serial.println("No Motion");
        digitalWrite(LED_PIN, LOW);   // Turn LED OFF
    }
    
    delay(500);  // Small delay to avoid excessive readings
}
