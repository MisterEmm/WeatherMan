from time import sleep
import RPi.GPIO as GPIO
import requests
import subprocess

prev = 0
prevcond = "Snow"

sleep(5)
subprocess.Popen(["python", "/home/pi/weather/icon.py", "OTNS.png"])
sleep(12)

while True:
        print ("Dark Sky Current Conditions")
        r = requests.get("https://api.darksky.net/forecast/YOUR_API_KEY/YOUR_LAT_LONG?units=uk2&exclude=hourly,flags,daily,alerts")
        
        data = r.json()
        
        print(data['currently']['icon'])
        print(data['currently']['temperature'])
        print(data['currently']['summary'])
        print(data['currently']['precipProbability'])
        
        icon = data['currently']['icon'] + ".png"
        temp = str(int(data['currently']['temperature'])) + "c"
        precip = data['currently']['precipProbability']*100
        prob = str(int((precip * 2.56) / 16))
        check = int(data['currently']['temperature'])
        checkcond = data['currently']['icon']
        
        if check != prev:
            print("Different Temperature")
            subprocess.Popen(["python", "/home/pi/weather/phones.py", icon]) 
        elif checkcond != prevcond:
            print("Different Conditions")
            subprocess.Popen(["python", "/home/pi/weather/phones.py", icon]) 
        else:
            print("Same")
                
        print(checkcond)
        print(temp)
        print(precip)
        #print(prob)
        subprocess.Popen(["python", "/home/pi/weather/icon.py", icon]) 
        sleep(12)
        subprocess.Popen(["python", "/home/pi/weather/temp.py", temp])
        sleep(12)
        subprocess.Popen(["python", "/home/pi/weather/precip.py", prob]) 
        sleep(10)
        print("And that's the weather.")
        sleep(150)
        prev = check
        prevcond = checkcond

else:
        print ("Something Else") 
