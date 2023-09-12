#IMPORTS
from dataclasses import dataclass
import PySide6.QtCore

#SETTINGS
Training = False
ManualControl = False
AutonomousControl = False

#INPUTS
DualCameraInput = ...
ButtonInput = ...
ControllerInput = ...
SonarInput = ...

#SUB ENVIORMENT STATS
Depth = 0
Humidity = 0
TubeTemp = 0

OrinTemp = 0

#ORIN
OrinIP = ""
OrinPort = 0
OrinUser = ""
OrinPass = ""

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
