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
    float ax_g = ax / 16384.0;
    float ay_g = ay / 16384.0;
    float az_g = az / 16384.0;

    //Serial.print("ax_g:"); Serial.print(ax_g);
    //Serial.print(" ay_g:"); Serial.print(ay_g);
    //Serial.print(" az_g:"); Serial.println(az_g);

    float angle_x = atan2(ax_g, sqrt(ay_g*ay_g + az_g*az_g)) * 180.0 / PI;
    float angle_y = atan2(ay_g, sqrt(ax_g*ax_g + az_g*az_g)) * 180.0 / PI;
    float angle_z = atan2(az_g, sqrt(ax_g*ax_g + ay_g*ay_g)) * 180.0 / PI;

    Serial.print("Angle X:"); Serial.print(angle_x);
    Serial.print("Angle Y:"); Serial.println(angle_y);
    Serial.print("Angle Z:"); Serial.print(angle_z);

    
    delay(100);
}
