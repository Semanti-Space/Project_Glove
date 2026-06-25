#include <Wire.h>
#include <MPU6050.h>

MPU6050 imu;


float filtered_angle_x = 0;
float filtered_angle_y = 0;
float filtered_angle_z = 0;
unsigned long last_time = 0;
//note to self unsigned means it will not take negative numbers.

void setup() {
    Serial.begin(115200);
    Wire.begin();
    imu.initialize();
    int16_t ax, ay, az, gx, gy, gz;
    imu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    

    float ax_g = ax / 16384.0;
    float ay_g = ay / 16384.0;
    float az_g = az / 16384.0;

    float angle_x = atan2(ax_g, sqrt(ay_g*ay_g + az_g*az_g)) * 180.0 / PI;
    float angle_y = atan2(ay_g, sqrt(ax_g*ax_g + az_g*az_g)) * 180.0 / PI;
    float angle_z = atan2(az_g, sqrt(ax_g*ax_g + ay_g*ay_g)) * 180.0 / PI;

    Serial.print("Angle X:"); Serial.print(angle_x);
    Serial.print("Angle Y:"); Serial.println(angle_y);
    Serial.print("Angle Z:"); Serial.print(angle_z);

    filtered_angle_x = angle_x;
    filtered_angle_y = angle_y;
    filtered_angle_z = angle_z;
    
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
    

    unsigned long current_time = millis();
    float dt = (current_time - last_time) / 1000.0;
    last_time = current_time;
    float gyro_rate_x = gx / 131.0;
    float gyro_rate_y = gy / 131.0;
    float gyro_rate_z = gz / 131.0;


    float angle_x = atan2(ax_g, sqrt(ay_g*ay_g + az_g*az_g)) * 180.0 / PI;
    float angle_y = atan2(ay_g, sqrt(ax_g*ax_g + az_g*az_g)) * 180.0 / PI;
    float angle_z = atan2(az_g, sqrt(ax_g*ax_g + ay_g*ay_g)) * 180.0 / PI;

    filtered_angle_x = 0.98 * (filtered_angle_x + gyro_rate_x * dt) + 0.02*angle_x;
    filtered_angle_y = 0.98 * (filtered_angle_y + gyro_rate_y * dt) + 0.02*angle_y;
    filtered_angle_z = 0.98 * (filtered_angle_z + gyro_rate_z * dt) + 0.02*angle_z;


    Serial.print(" Filtered X:"); Serial.println(filtered_angle_x);
    Serial.print(" Filtered Y:"); Serial.println(filtered_angle_y);
    Serial.print(" Filtered Z:"); Serial.println(filtered_angle_z);


    //Serial.print("Angle X:"); Serial.print(angle_x);
    //Serial.print("Angle Y:"); Serial.println(angle_y);
    //Serial.print("Angle Z:"); Serial.print(angle_z);

    
    delay(100);
}
