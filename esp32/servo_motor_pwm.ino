#include <Arduino.h>

#define SERVO_PIN 18   // GPIO18 controls the servo
#define PWM_CHANNEL 0
#define PWM_FREQ 50    // 50Hz PWM (Standard for servos)
#define PWM_RESOLUTION 16  // 16-bit resolution

void setup() {
    Serial.begin(9600);
    ledcSetup(PWM_CHANNEL, PWM_FREQ, PWM_RESOLUTION);
    ledcAttachPin(SERVO_PIN, PWM_CHANNEL);
    Serial.println("Servo Motor Initialized");
}

void setServoAngle(int angle) {
    int duty = map(angle, 0, 180, 1638, 8192);  // Convert angle to PWM duty cycle
    ledcWrite(PWM_CHANNEL, duty);
    Serial.print("Servo Angle: ");
    Serial.println(angle);
}

void loop() {
    for (int angle = 0; angle <= 180; angle += 10) {
        setServoAngle(angle);
        delay(500);
    }
    
    for (int angle = 180; angle >= 0; angle -= 10) {
        setServoAngle(angle);
        delay(500);
    }
}
