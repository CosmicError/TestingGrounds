
#IMPORTS
import tkinter as tk
from tkinter import *
from tkinter import ttk
from dataclasses import dataclass

#SETTINGS
Training = False
ManualControl = False
AutonomousControl = False

#INPUTS
DualCameraInput = ...
ButtonInput = ...
ControllerInput = ...
SonarInput = ...

#CONSTANTS
window = Tk()
ppi = window.winfo_pixels("1i")

#SUB ENVIORMENT STATS
Depth = 0
Humidity = 0
TubeTemp = 0
OrinTemp = 0

#ORIN
OrinIP = tk.StringVar()
OrinPort = tk.IntVar()
OrinUser = tk.StringVar()
OrinPass = tk.StringVar()

# WINDOW SETTINGS
window.title("Ground Control Station")
window.geometry("600x450")
#window.minsize(100, 100)
#window.maxsize(9999, 9999)
#window.attributes("-fullscreen", 1)

#window.attributes("-alpha", 0.5)

# COMMANDS
def ConnectOrin(username, password, ip, port):
    return

# FRAME SETTINGS
orinframe = ttk.Frame(window, padding="3 3 3 3")
browseframe = ttk.Frame(window, padding="3 3 3 3")

# WIDGET SETTINGS
usernameinput = ttk.Entry(orinframe, width=30, textvariable=userin)
passwordinput = ttk.Entry(orinframe, width=30, show="*", textvariable=passin)
connectbutton = ttk.Button(orinframe, text="Login", command=ConnectOrin)

# WIDGET POSITIONING
usernameinput.place(y=-22, relx=.5, rely=.5, anchor=CENTER)
passwordinput.place(relx=.5, rely=.5, anchor=CENTER)
loginbutton.place(x=5, y=25, relx=.5, rely=.5, anchor=CENTER)

# WIDGET PRESETS
userin.set("Username")
passin.set("Password")

#Created all of these as classes so it is for mechanical / eletrical to add / remove these parts if needed

#using @dataclass to declare that this class is a dataclass and not a normal class
@dataclass
class Battery:
    
    # Attribute Declaratrions using Type Hints
    voltage: int
    amps: int

@dataclass
class Motor:
    pwm: int

@dataclass
class Servo:
    pwm: int
    
#Start the subs program for the competition
def StartSubProgram():
    return

#Stop the subs program for the competition
def StopSubProgram():
    return

#Turn the Sub On
def PowerSubOn():
    return

#Turn the sub Off
def PowerSubOff():
    return

#display the speed to the GUI
def Speed(speed):
    return

def ReadConfig():
    return

def WriteConfig():
    return

# CLOSE
window.protocol("WM_DELETE_WINDOW", logout)

# RUN
window.mainloop()

    
# CUSTOM WIDGETS
'''
class Table:
    def __init__(self, root, columns, rows, data):
        columnwidths = []
        # code for creating table
        for i in range(rows-1):
            for j in range(columns-1):
                self.e = Entry(root, width=15, fg='black', font=('Arial', 14))
                self.e.grid(row=i, column=j)
                print()
                self.e.insert(END, data[i][j])
            '''
