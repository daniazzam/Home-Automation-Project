############################################################
#Feature #4: MotionSensor + LED
############################################################

#When night time, if a motion is detected in the hallway, the dim light turns on just
#for the user to see

from gpiozero import PWMLED, MotionSensor
import Feature1

class Feature4():
    def __init__(self):
        F1=Feature1
        self.lightVal=F1.getLDRvalue()
        self.ledHallway=PWMLED(10)
        self.pir = MotionSensor(9)

    def hallwayLight(self,PWM):
        self.ledHallway.value=PWM

    def hallWay(self):
        #check if it is night time to turn light on when motion detected
        if (self.lightVal)<0.3:
            if self.pir.motion_detected:
                self.hallwayLight(0.4)
            else:
                self.hallwayLight(0)

    def run_feature4(self):
        self.hallwayt()

if __name__=='__main__':
    F3=Feature4()
    F3.run_feature4()