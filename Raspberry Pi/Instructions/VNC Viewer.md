# Connect Raspberry Pi to Laptop/PC using VNC Viewer

1. Install the Raspberry Pi OS to the SD Card. Preferably using the Raspberry Pi Imager Software for the latest OS. https://www.raspberrypi.org/software/
2. Configure WiFi connection on SD Card. This should be done before inserting the SD card on to the Pi. Create a file `wpa_supplicant.con` on `\boot` in the SD Card. Use the following code to add the details of your WiFi connection and Password. 

    ```
    country=IN
    
    update_config=1
    
    ctrl_interface=/var/run/wpa_supplicant

    network={
      ssid=""
      psk=""
      key_mgmt=WPA-PSK
    }

  Alternatively, use Supplicant Generator in https://codepen.io/LilTrublMakr/full/yRGPrv/ to create the `wpa_supplicant.conf` as it may not run if UNIX style spacing is not adopted. Enter your WiFI connection name and Password within the double quotes. 
  
3. Create a blank text file with the name `ssh` to enable SSH on the Pi. 
4. Put the SD card on the Pi and power on. 
5. Find the IP address of the Pi using terminal by typing `arp -a` or by opening the router page. Connect Pi to laptop/PC through SSH. Type `ssh pi@[IP address of Pi]` in the terminal. **The terminal of the Pi can now be accesed through the terminal of the PC/Laptop**. The password is usually *raspberry*. 
6. Install VNC viewer on the Pi. 
```
sudo apt–get update
sudo apt–get install realvnc–vnc–server realvnc–vnc–viewer
```
7. Navigate to VNC Viewer on the Pi. Type `sudo raspi-config` on terminal. Navigate to `Interfacing Options --> P3 VNC --> Yes`. 
8. Install VNC Viewer on Raspberry Pi. Type the IP address of the Pi. If prompted to login, the username is *pi* and the password is *raspberry*. 
