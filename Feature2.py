############################################################
#Feature #2: Motion Sensor + Camera + Entrance Led
############################################################
import Feature1
from gpiozero import PWMLED, MotionSensor
from picamera import PiCamera
from time import sleep

class Feature2:
    def __init__(self):
        F1=Feature1
        self.camera=PiCamera()
        self.ledEntrance=PWMLED(4)
        self.pir = MotionSensor(17)
        self.lightVal=F1.getLDRvalue()
        self.count=1

    def checkMotion(self):
        if self.pir.motion_detected:
            self.camera_light()
        else:
            pass

    def camera_light(self):
        if self.lightVal <0.3:
            self.ledEntrance.on()
            self.camera.start_preview()
            self.camera.exposure_mode='night'
            sleep(2)
            self.camera.capture('/home/pi/Desktop/image%s.jpg' % self.count)
            self.camera.exposure_mode='auto'
            self.camera.stop_preview()
            self.count+=1
            self.ledEntrance.off()
            #Eventhough we are lighting a LED, in case any failure happens for the led, we still need to 
            #take a clear picture of the person causing motion in case of robbery    
        else:
            self.camera.start_preview()
            sleep(2)
            self.camera.capture('/home/pi/Desktop/image%s.jpg' % self.count)
            self.camera.stop_preview()
            self.count+=1
    def run_Feature2(self):
        self.camera_light()

if __name__=='__main__':
    F2=Feature2()
    F2.run_Feature2()
