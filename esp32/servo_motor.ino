#include <Servo.h>

Servo myServo;
#define SERVO_PIN 18

void setup() {
    Serial.begin(19600);
    myServo.attach(SERVO_PIN);
    Serial.println("Servo Initialized");
}

void loop() {
    for (int angle = 0; angle <= 180; angle += 10) {
        myServo.write(angle);
        Serial.print("Servo Angle: ");
        Serial.println(angle);
        delay(500);
    }
    
    for (int angle = 180; angle >= 0; angle -= 10) {
        myServo.write(angle);
        Serial.print("Servo Angle: ");
        Serial.println(angle);
        delay(500);
    }
}
