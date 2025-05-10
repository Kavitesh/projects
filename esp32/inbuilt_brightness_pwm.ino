#define LED_PIN 2
#define PWM_CHANNEL 0

void setup() {
    Serial.begin(19600);
    ledcSetup(PWM_CHANNEL, 5000, 8);  // 5kHz PWM, 8-bit resolution
    ledcAttachPin(LED_PIN, PWM_CHANNEL);
}

void loop() {
    for (int duty = 0; duty <= 255; duty++) {
        ledcWrite(PWM_CHANNEL, duty);
        delay(10);
    }
    for (int duty = 255; duty >= 0; duty--) {
        ledcWrite(PWM_CHANNEL, duty);
        delay(10);
    }
}
