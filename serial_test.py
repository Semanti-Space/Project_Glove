import serial 

ser = serial.Serial('COM3',115200, timeout=1)  
while True:
    line = ser.readline()
    line = line.decode('utf-8').strip()
    print(line)
    for i in line.split(","):
        f = i.split(":")
        f_final = f[1]
        print(f_final)

        
