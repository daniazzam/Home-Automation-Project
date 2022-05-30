############################################################
#Feature #1: Controlling the lights of some rooms using LDRs
############################################################

from gpiozero import LightSensor, Button, PWMLED
from time import sleep



def lights(led, pwmVal):
    led.value=pwmVal


class Feature1:
    def __init__(self):
        #we will be using 3 LDRs 
        #in order to get an average between the 3 LDR values in case any failure happens
        self.ldr1=LightSensor(25)
        self.ldr2=LightSensor(8)
        self.ldr3=LightSensor(7)

        #we will be using 4 LED lights for 4 different rooms
        self.led1=PWMLED(14)
        self.led2=PWMLED(15) 
        self.led3=PWMLED(18)
        self.led4=PWMLED(23)

        #we will be using 5 override switches for the user to decide if he wants to solely rely on the LDRs or turn the lights on or off manually
        #The first button is to check if he wants LDR or manual
        self.buttonLDR =Button(5)   #if pressed, lights are controlled by the LDRs
        self.buttonM1 =Button(6)    #manual switch for room 1
        self.buttonM2 =Button(13)
        self.buttonM3 =Button(19)
        self.buttonM4 =Button(26)

    def getLDRvalue(self):
        valueAdded=self.ldr1.value+self.ldr2.value+self.ldr3.value
        return valueAdded/3

    def checkButtons (self,led):
        if self.buttonLDR.is_pressed:
            #we check the value of LDR
            val=self.getLDRvalue(self)
            if val>0.8:
                #there is light outside, so turn LEDs OFF
                lights(led, 0)
            elif val>0.5:
                lights(led,0.33)
            elif val>0.2:
                lights(led,0.66)
            else:
                #there is DARK outside, so turn LEDs ON
                lights(led,1)
        else:
            if self.buttonM.is_pressed:
                lights(led,1)
            else:
                lights(led,0)

    def run_Feature1(self):
        self.checkButtons(self.led1)
        self.checkButtons(self.led2)  
        self.checkButtons(self.led3)  
        self.checkButtons(self.led4)

if __name__=='__main__':
    F1=Feature1()
    F1.run_Feature1()

