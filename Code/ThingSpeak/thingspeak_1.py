#Python code to take datastring from Arduino and send to ThingSpeak platform




import httplib
import urllib
import time
key = "R2JGYZW5IMHCGSSA"  # Put your API Key here

import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()


def water_quality():
    while True:
        if ser.in_waiting > 6:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            line = line.split(',')
            cond_1 = line[0]
            cond_2 = line[1]
            cond_3 = line[2]
            ph = line[3]
            cod = line[4]
            bod = line[5]
          params = urllib.urlencode({'field1': cond_1, 'field2': cond_2, 'key':key }) 
          headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
          conn = httplib.HTTPConnection("api.thingspeak.com:80")
          try:
              conn.request("POST", "/update", params, headers)
              response = conn.getresponse()
              print (cond_1)
              print (response.status, response.reason)
              data = response.read()
              conn.close()
          except:
              print ("connection failed")
          break
if __name__ == "__main__":
        while True:
                water_quality()
