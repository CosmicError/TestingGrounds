
#TODO: Make the motor pwm actually update when changed, LINE 182

#TODO: create both the modular servo creation and battery creation

# ================= IMPORTS =================

# imported as our main GUI library
import tkinter as tk
# imported so we can pull images from cameras
import cv2
# so we can run the video streaming and the program itself without any noticable lag
import threading
# imported to handle images
from PIL import ImageTk, Image
# imported to handle the config file
import json
# imported for the orin ssh connection
import fabric



# ================= CONFIG =================
PARENT_PATH = __file__.split("GCS.py")[0]

f = open(PARENT_PATH+'config.json')
config = json.load(f)

BATTERY_COUNT = config["ROBOT"]["BATTERY_COUNT"] or 4
MOTOR_COUNT = config["ROBOT"]["MOTOR_COUNT"] or 8
SERVO_COUNT = config["ROBOT"]["SERVO_COUNT"] or 2
ICON_PATH = config["GCS"]["ICON_PATH"] or ""

f.close()

# ================= VARIABLES =================

# VARIABLE SETTINGS
training_sim = False
training_real_world = False
manual_control = False
autonomous_control = False

#INPUTS
web_camera_input = cv2.VideoCapture(0)
depth_camera_input = ...
button_input = ...
controller_input = ...
sonar_input = ...

# CONSTANTS
WINDOW: object = tk.Tk()
PPI: int = WINDOW.winfo_pixels("1i")

# SUB ENVIORMENT STATS
depth: int = tk.IntVar()
humidity: int = tk.IntVar()
tube_temp: int = tk.IntVar()
orin_temp: int = tk.IntVar()

# ORIN
orin_ip: str = tk.StringVar()
orin_port: int = tk.IntVar()
orin_user: str = tk.StringVar()
orin_pass: str = tk.StringVar()
orin_connected: bool = False


# ================= SUB PART CLASSES =================

class Battery():
    def __init__(self, label_object, value_object):
        self.label_object = label_object 
        self.value_object = value_object
        self.voltage = tk.IntVar()
        self.amps = tk.IntVar()
    
    def update_value(self):
        self.value_object.text = str(self.voltage)+" / "+str(self.amps)
    

class Motor():
    def __init__(self, label_object, value_object):
        self.label_object = label_object # object that displays the name of the motor, ex "Motor 1"
        self.value_object = value_object # object that displays the pwm of the motor
        self.pwm = tk.IntVar()
    
    def update_value(self):
        self.pwm.set(3)
        self.value_object.text = "3"

class Servo():
    def __init__(self, label_object, value_object):
        self.label_object = label_object 
        self.value_object = value_object
        self.pwm = tk.IntVar()
    
    def update_value(self):
        self.value_object.text = self.pwm


# ================= SUB COMMANDS =================

def connect_orin(username, password, ip, port):
    orin_connected = True

def disconnect_orin():
    if orin_connected:
        orin_connected = False
    
#Start the subs program for the competition
def start_sub_program():
    return

#Stop the subs program for the competition
def stop_sub_program():
    return

#Turn the Sub On
def power_sub_on():
    return

#Turn the sub Off
def power_sub_off():
    return

#display the speed to the GUI
def get_speed(speed):
    return

def read_config():
    return

def write_config():
    return


# ================= WINDOW =================

# WINDOW SETTINGS
WINDOW.title("Ground Control Station")
#WINDOW.iconphoto(True, tk.PhotoImage(file=ICON_PATH))

WINDOW.columnconfigure(1, weight=1, minsize=250)
WINDOW.rowconfigure(0, weight=1, minsize=100)
WINDOW.rowconfigure(1, weight=1, minsize=100)
WINDOW.rowconfigure(2, weight=1, minsize=100)

# MAIN FRAME CREATION
orin_frame = tk.Frame(master=WINDOW, relief=tk.RAISED, bg="red")
orin_frame.grid(row = 0, column = 2, rowspan = 2, sticky = "nsew", padx=2, pady=2)

video_frame = tk.Frame(WINDOW, bg="limegreen")
video_frame.grid(row = 0, column = 1, rowspan=2, sticky = "nsew", padx=2, pady=2)

radar_frame = tk.Frame(WINDOW, bg="yellow")
radar_frame.grid(row = 0, column = 0, sticky="nsew", padx=2, pady=2)

data_display_frame = tk.Frame(WINDOW, bg = "dodgerblue")
data_display_frame.grid(row = 1, column = 0, rowspan = 2, sticky = "nsew", padx=2, pady=2)

button_frame = tk.Frame(WINDOW, bg="orange")
button_frame.grid(row = 2, column = 1, columnspan=2, sticky="nsew", padx=2, pady=2)


# ORIN FRAME WIDGETS
orin_label = tk.Label(orin_frame, text="ORIN CONNECTION")
orin_user_label = tk.Label(orin_frame, text="User:")
orin_user_input = tk.Entry(orin_frame, textvariable=orin_user)
orin_pass_label = tk.Label(orin_frame, text="Pass:")
orin_pass_input = tk.Entry(orin_frame, width=30, show="*", textvariable=orin_pass)
orin_ip_label = tk.Label(orin_frame, text="IP:")
orin_ip_input = tk.Entry(orin_frame, width=30, textvariable=orin_ip)
orin_port_label = tk.Label(orin_frame, text="Port:")
orin_port_input = tk.Entry(orin_frame, width=30, textvariable=orin_port)
connect_button = tk.Button(orin_frame, text="Connect", command=connect_orin)

orin_label.grid(row = 0, column=0, sticky = "nsew", rowspan = 1, columnspan = 2, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_user_label.grid(row = 1, column=0, sticky = "e", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_user_input.grid(row = 1, column=1, sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_pass_label.grid(row = 2, column=0, sticky = "e", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_pass_input.grid(row = 2, column=1, sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_ip_label.grid(row = 3, column=0, sticky = "e", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_ip_input.grid(row = 3, column=1, sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_port_label.grid(row = 4, column=0, sticky = "e", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
orin_port_input.grid(row = 4, column=1, sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
connect_button.grid(row = 5, column=0, sticky = "nsew", rowspan = 1, columnspan = 2, padx = 5, pady = 5, ipadx = 3, ipady = 3)

# VIDEO FRAME WIDGETS
video_display = tk.Label(video_frame)
video_display.grid(sticky = "nsew", rowspan = 1, columnspan = 2)

# RADAR FRAME WIDGETS
radar_display = tk.Label(radar_frame)
radar_display.grid(sticky = "nsew", rowspan = 1, columnspan = 1)
radar_display.config(width=50, height=21, bg="yellow")


# DATA DISPLAY
batteries = []
motors = []
servos = []

for i in range(BATTERY_COUNT):
    batteries.append(Battery(label_object=tk.Label(data_display_frame, text="Battery "+str(i)+":"), value_object=tk.Label(data_display_frame, text="0")))
    batteries[i].label_object.grid(row = i-(i%2), column=1+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    batteries[i].value_object.grid(row = i-(i%2), column=2+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    #batteries[i].update_value()

for i in range(BATTERY_COUNT, BATTERY_COUNT+MOTOR_COUNT):
    count = i-BATTERY_COUNT
    motors.append(Motor(label_object=tk.Label(data_display_frame, text="Motor "+str(count)+":"), value_object=tk.Label(data_display_frame, text="0")))
    motors[count].label_object.grid(row = i-(i%2), column=1+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    motors[count].value_object.grid(row = i-(i%2), column=2+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    #motors[i].update_value()
    
print(3*"=")
for i in range(BATTERY_COUNT+MOTOR_COUNT, BATTERY_COUNT+MOTOR_COUNT+SERVO_COUNT):
    count = i-(BATTERY_COUNT+MOTOR_COUNT)
    servos.append(Servo(label_object=tk.Label(data_display_frame, text="Servo "+str(count)+":"), value_object=tk.Label(data_display_frame, text="0")))
    servos[count].label_object.grid(row = i-(i%2), column=1+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    servos[count].value_object.grid(row = i-(i%2), column=2+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    #servos[i].update_value()
    
# BUTTON FRAME
button_frame = tk.Label(button_frame)

button_frame.grid(sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)

#  ===== POST CREATION FUNCTIONS / VARS / CONST ======

def stream_video():
    #read the data and seperate it into its index, and frame (we don't need the index so its just an _)
    _, frame = web_camera_input.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #turn it into an image :O
    img = Image.fromarray(cv2image)
    #make the image compatible with TK and allow it to achieve live feed
    imgtk = ImageTk.PhotoImage(image=img)
    #Display the image
    video_display.imgtk = imgtk
    video_display.configure(image=imgtk)
    #after displaying the image, run the function again, to achieve a live video effect
    video_display.after(1, stream_video) 
    #still need to test if this will effect the workability of the program

# Constant used to hold the thread
VIDEO_THREAD = threading.Thread(target=stream_video)

#create a function that will be called when trying to close the application, 
# this is made so we can log out of and power down / record anything that should be, before we close
def close_application():
    #close the started thread
    VIDEO_THREAD.join()
    #make sure the orin is logged out of
    #disconnect_orin()
    #destroy the window, since we are overriding the origional functionality
    WINDOW.destroy()


# ======== CLOSING THE APPLICATION =========

WINDOW.protocol("WM_DELETE_WINDOW", close_application)


# ================= RUN =================

#activate the video streaming
VIDEO_THREAD.start()

#run the tk program
WINDOW.mainloop()
