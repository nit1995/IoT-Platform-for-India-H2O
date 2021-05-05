## Connect Raspberry Pi to ThingSpeak for Data Transfer

1. Create a Channel on ThingSpeak
2. Get API Key on ThingSpeak Channel. Copy the *Write API Key*
3. Install the required libraries.
``` 
sudo apt-get install httplib
sudo apt-get install urllib
```
If `httplib` is not installed, try `http.client`. 

4. Create a file with *.py* extension and copy the code in https://bit.ly/3h5QYAG. 
Run the file using 
```
python /path/filename.py
```
You can see CPU Temperature on your terminal 

<img width="567" alt="Screenshot 2021-05-05 at 10 03 30 AM" src="https://user-images.githubusercontent.com/8596851/117097417-2d799680-ad89-11eb-8333-4e6a5998f563.png">

On your ThingSpeak channel, you can see the data visualisation. 

<img width="1299" alt="Screenshot 2021-05-05 at 9 47 52 AM" src="https://user-images.githubusercontent.com/8596851/117097468-4eda8280-ad89-11eb-93d9-8daf43dfcb27.png">


