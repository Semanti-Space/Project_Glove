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