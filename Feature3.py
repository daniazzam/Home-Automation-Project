############################################################
#Feature #3: automatic gate using distance sensor+Buzzer+SERVO
############################################################

from gpiozero import DistanceSensor, Buzzer, Servo
import RPi.GPIO as GPIO
from time import sleep
import datetime

with open('readme.txt', 'w') as f:
    f.write('readme')

class Feature3:
    def __init__(self,directory):
        self.distSensor=DistanceSensor(echo=3 ,trigger=2 ,threshold_distance=1)
        self.servo=Servo(24)
        self.gateBuzzer=Buzzer(12)
        self.distance=1
        self.F=open(directory,"w")

    def checkDistance(self):

        #check for distance, if less than 1 meter, open the gate
        if self.distSensor.distance < self.distance:

            #check if servo is closed or in mid position
            #if it is already in mid position, do nothing
            #else, open the gate
            if self.servo.value==0:
                pass
            else:
                #open the gate using servo by setting it to its mid position 90 degrees
                self.F.write("The gate opened at "+str(datetime.datetime.now()))
                self.servo.mid()
                for i in range(4):
                    self.gateBuzzer.on()
                    sleep(0.5)
                    self.gateBuzzer.off()
                    sleep(0.25)
            
        else:
            #close the gate using servo by setting to its min position 0 degrees (closed)
            self.servo.min()

    def run_feature3(self):
        self.checkDistance()

if __name__=='__main__':
    F3=Feature3(r'/home/pi/Desktop/GateInfo.txt')
    F3.run_feature3()