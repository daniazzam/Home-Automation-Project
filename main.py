import Feature1,Feature2,Feature3,Feature4
from tkinter import *
from tkinter.ttk import *
import time


#Gui Component
MyGui=Tk()
MyGui.title('Home Automation Dashboard')

Description=Label(MyGui,text='This dashboard is the user\'s interface to turn on and off any of the features.')
Description.grid(row=1,column=1)

text=Label(MyGui,text='Enter the path file in the box below')
text.grid(row=2,column=1)

path=Entry(MyGui,width=50)
path.grid(row=3,column=1)

path_condition=Label(MyGui,text='-')
path_condition.grid(row=4,column=1)

def get_path():
    
    entered_path=path.get()

    if entered_path=="":
        path_condition.config(text='You have to specify the path first')
        return False
    else:
        path_condition.config(text='Path is added correctly')
        print(entered_path)
        return True

################################################
#main code
def run_features():
    F1=Feature1.Feature1()
    F2=Feature2.Feature2()
    F3=Feature3.Feature3(path.get())
    F4=Feature4.Feature4()
    
    while True:
        F1.run_Feature1()
        F2.run_Feature2()
        F3.run_Feature3()
        F4.run_Feature4()
###############################################        
        
text_run=Label(MyGui,text='-')
text_run.grid(row=7,column=1)

def start():
    condition=get_path()
    if condition:
        text_run.config(text="The features are running")
        print('running '+path.get())
        time.sleep(0.5)
        run_features()

    else:
        text_run.config(text='Please make sure to add the path')

pb1=Button(MyGui,text='Run Features',command=start)
pb1.grid(row=6,column=1)


MyGui.mainloop()