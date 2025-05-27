#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

float accAngle, gyroRate, fusedAngle = 0.0;
float alpha = 0.98;
unsigned long lastTime;

void setup() {
  Serial.begin(19600);
  Wire.begin(21, 22);  // SDA = 21, SCL = 22

  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed");
    while (1);
  }

  Serial.println("MPU6050 initialized!");
  lastTime = millis();
}

void loop() {
  // Read raw data
  int16_t ax, ay, az, gx, gy, gz;
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Convert accelerometer to angle (pitch)
  accAngle = atan2(ay, az) * 180 / PI;

  // Convert gyro x-axis to deg/sec
  gyroRate = gx / 131.0;

  // Time difference
  unsigned long now = millis();
  float dt = (now - lastTime) / 1000.0;
  lastTime = now;

  // Complementary filter fusion
  fusedAngle = alpha * (fusedAngle + gyroRate * dt) + (1 - alpha) * accAngle;

  Serial.print("Pitch Angle (deg): ");
  Serial.println(fusedAngle);

  delay(10);
}
