#include <Wire.h>
#include <MPU6050.h>

MPU6050 imu;

void setup() {
    Serial.begin(115200);
    Wire.begin();
    imu.initialize();
    
    if (imu.testConnection()) {
        Serial.println("MPU6050 connected!");
    } else {
        Serial.println("MPU6050 connection FAILED");
    }
}

void loop() {
    int16_t ax, ay, az, gx, gy, gz;
    imu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    
    Serial.print("ax:"); Serial.print(ax);
    Serial.print(" ay:"); Serial.print(ay);
    Serial.print(" az:"); Serial.println(az);
    
    delay(100);
}
