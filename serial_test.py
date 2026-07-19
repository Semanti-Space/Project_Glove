import serial 

ser = serial.Serial('COM3',115200, timeout=1)  
while True:
    line = ser.readline()
    line = line.decode('utf-8').strip()
    print(line)
    parts = line.split(",")
    if len(parts) < 5:
        continue
    f1 = int(parts[0].split(":")[1])
    f2 = int(parts[1].split(":")[1])
    f3 = int(parts[2].split(":")[1])
    f4 = int(parts[3].split(":")[1])
    f5 = int(parts[4].split(":")[1])
    print(f1, f2, f3, f4, f5)


    def get_finger_state(value, threshold_bent, threshold_straight):
        if value > threshold_bent:
            return "BENT"
        elif value < threshold_straight:
            return "STRAIGHT"
        else:
            return "UNCLEAR"
    
    s1 = get_finger_state(f1, 1000, 700)
    s2 = get_finger_state(f2, 400, 200)
    s3 = get_finger_state(f3, 400, 200)
    s4 = get_finger_state(f4, 1000, 400)
    s5 = get_finger_state(f5, 1500, 1300)
    print (s1, s2, s3, s4, s5)
    
        
