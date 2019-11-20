from gpiozero import Servo
from time import sleep
from sys import argv, exit
 
myGPIO=17
 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Different Jiggle")

myServo.value= 0.35
sleep(1)
myServo.value= -0.3
sleep(1)
myServo.value= 0.35
sleep(1)
myServo.value= -0.3
sleep(1)
myServo.value= 0
sleep(0.3)


exit()