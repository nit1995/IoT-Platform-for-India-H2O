### Connect Arduino to Raspberry Pi
Use a USB cable to connect the Arduino and the Raspberry Pi. Alternatively, use GPIO pins to connect.  However, a voltage shifter is required if the Arduino board operates on 5V. Connect the RX and TX of the Arduino with the TX and RX of the Pi. 

1. Detect Arduino on the Raspberry Pi. Run `ls /dev/tty*`. The Arduino usually appears in the serial port as *dev/ttyACM0*

<img width="572" alt="Screenshot 2021-04-29 at 3 42 53 PM" src="https://user-images.githubusercontent.com/8596851/116535662-9e402f00-a901-11eb-93e4-ab184aef00e0.png">

Enable hardware permission for serial port to enable dialout error using 
```
sudo adduser username dialout
```
Replace *username* with the username of your Pi.

2. Install python serial libraries 
```
sudo apt install python3-pip
python3 -m pip install pyserial
```
3. For simple communication, upload the following code on you Arduino using the Arduino IDE. 
```
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Hello from Arduino!");
  delay(1000);
}
```

Ensure the same baud rate in both Arduino and Raspberry Pi. 

4. Create a file with the extension *.py* in your Pi. Paste the following code in the file. 
```
#!/usr/bin/env python3
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
```

On your terminal, go to the file path, make thepython file executable and run the file. 

```
chmod +x filename.py
./filename.py 



<img width="655" alt="Screenshot 2021-04-29 at 3 47 46 PM" src="https://user-images.githubusercontent.com/8596851/116536241-4a821580-a902-11eb-8022-c540906d9236.png">

<img width="565" alt="Screenshot 2021-04-29 at 3 51 47 PM" src="https://user-images.githubusercontent.com/8596851/116536677-d98f2d80-a902-11eb-9f93-b49c69601435.png">
