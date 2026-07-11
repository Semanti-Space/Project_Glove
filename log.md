## June 6
- Got MediaPipe working
- Learned about 21 landmarks coordinates
- Noticed index tip y-value decreases when finger curls 
- The base of your index finger (Point 5) is attached to your palm. It barely moves when you curl your finger. So its y value staying around 0.61 is correct — it's just sitting there anchored to your hand.
- The tip (Point 8) is what moves dramatically — from 0.90 (hanging down, extended) to 0.11 (curled up toward your palm). 
- RULE - If tip.y is significantly LESS than base.y → finger is curled (because tip and base are close)
If tip.y is equal to or greater than base.y → finger is extended (because tip and base are far away.)

## June 7 
- Wrote a function using dictionary and the putText function  that tells you whether the index finger is extended or curled, and prints "EXTENDED" or "CURLED" on screen in real time. After the Index finger is succesfull, I did the same for all five fingers simultaneously. 
 Built finger extension/curl detection using y-coordinate differences
- Learned about thresholds, dictionaries, f-strings, cv2.putText
- Using this and the if else, I detected the first mudra 'Pataka' 
- Learnt about the difference between base and tip of a finger and the threshold value for each.

## June 8 and June 9 
- Completed writing the code for all 28 Single Hand Mudras. 
- Added conditions for each one specifically, trying them out in the camera, and writing out their exact problems
- Made an error log in my diary for all the overlapping or glitching Mudras which I will fix tomorrow.

## June 10 and June 11 
- Dedicated to solving logical errors in my code 
- Wrote down each issue which included overlapping of mudras, not working mudras in a physical diary 
- Figured out the code and logic behind the wrong code in the diary by myself
- Main Issue between the 3 - Padmakosha, Samdamsha and Mukula - Due to fingers occluding one another, I could not capture them by the 2D webcam. Led me to use Sensor fusion architecture. 
- Tried to solve major errors that I faced with Alapadma, And Bhramhara and Mrigashirsha.

## June 12 
- Official completion of Phase 1 
- Errors:
- Depth or Puffiness - Padmakosha, Samdamsha and Mukula
- Finger spread occlusion - Alapadma 
- Touch point occlusion - Katakamukhaha 

## Phase 2 - June 20th
- Connected the ESP32 via the USB cable to the laptop.
- Had the MPU soldered and connected it to the breadboard. Used the jumper wires to connect it to the ESP32. 
- Wrote the sketch for ax, ay and az in Arduino IDE and saw the values change as I tilt the breadboard. 
- Flat: z is big positive; Tilted one way: x is big positive; Tilted the other way: x is big negative

## June 21st and June 22nd 
- Found the gravitational force of the raw units of x,y and z.
- Found the observations for ax_g, ay_g and az_g for lying flat, laying to my left, laying to my right. 
- Learned about the vector decomposition in the MPU. 
- Learned about the Inertial Reference Frames in Biomechanics - Using gravity (constant) as a inertial reference 

## June 23rd 
- Finding angles using the gravitational forces of the raw units
- using atan2  to find the angle.
- Took observations of the angle while laying flat (z ~90), to my left (x ~ 90) and to my right 
- Noticed a slight ~2 degree wobble due to the accelerometer. Otherwise Accurate 

## June 24th 
- Learnt about the Complementary filter. 
- Implemented the formula for gyroscopic measurements
- Unpredictable angle values and assymmetry in laying to my left and right 
- Will try to solve the errors tomorrow

## June 25th 
- Solved the errors for Complementary filter by adding the initial values of x into filtered_Angle
- Installed the second MPU to the breadboard
- Connected both MPUs to each other by male to male jumper wires.
- Learnt about 0x68 and 0x69 I2C Address


## June 26th 
- Implemented the code for finding the angles for both MPU1 and MPU2. 
- IMU1: X≈-20, Y≈5.7, Z≈87.5
- IMU2: X≈14, Y≈10.5, Z≈83.6
- Difference between the two to find wrist angle 
- PHASE 2 COMPLETED 


## July 1st to July 5th 
- Understood what flex sensors are and how they work 
- Learnt about resistance changes when flex sensor is bent or straight 
- Got the flex sensors soldered to connecting wires 
- Got the coin vibrator motors soldered to connecting wires 

## July 6th to July 8th
- Learnt about voltage dividers 
- Understoof Pin34 Analog reader of esp32
- Learnt about ADC (Analog to Digital Converter)
- Learnt about the possible values range (0 to 4095) for range of voltage from 0 to 3.3V




