import Feature1,Feature2,Feature3,Feature4

F1=Feature1.Feature1()
F2=Feature2.Feature2()
F3=Feature3.Feature3(r'/home/pi/Desktop/GateInfo.txt')
F4=Feature4.Feature4()

while True:
    F1.run_Feature1()
    F2.run_Feature2()
    F3.run_Feature3()
    F4.run_Feature4()