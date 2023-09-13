
#TODO: Make the motor pwm actually update when changed, LINE 182

#TODO: Make the motor placement look a bit nicer, maybe not so verticle
#TODO: create both the modular servo creation and battery creation

# ================= IMPORTS =================

# imported as our main GUI library
import tkinter as tk
# imported so we can pull images from cameras
import cv2
# so we can run the video streaming and the program itself without any noticable lag
import threading
# used so we dont hard code sub components in so that if the sub were to ever change, it would not call for a huge code re-write
from dataclasses import dataclass
# imported to handle images
from PIL import ImageTk, Image


# ================= VARIABLES =================

#SETTINGS
training = False
manual_control = False
autonomous_control = False
BATTERY_COUNT = 4
MOTOR_COUNT = 8
SERVO_COUNT = 2

#INPUTS
dual_camera_input = ...
button_input = ...
controller_input = ...
cap = cv2.VideoCapture(0)
sonar_input = ...

#CONSTANTS
WINDOW = tk.Tk()
PPI = WINDOW.winfo_pixels("1i")

#SUB ENVIORMENT STATS
depth = 0
humidity = 0
tube_temp = 0
orin_temp = 0

#ORIN
orin_ip = tk.StringVar()
orin_port = tk.IntVar()
orin_user = tk.StringVar()
orin_pass = tk.StringVar()
orin_connected = False


# ================= WINDOW FUNCTIONS =================

def get_window_size():
    WINDOW.update_idletasks()
    width = WINDOW.winfo_width()
    height = WINDOW.winfo_height()
    print(f"Window size: {width}x{height}")
    
# function for video streaming


# ================= SUB DATACLASSES =================

#Created all of these as classes so it is for mechanical / eletrical to add / remove these parts if needed

#using @dataclass to declare that this class is a dataclass and not a normal class
@dataclass
class Battery:
    
    # Attribute Declaratrions using Type Hints
    label_object: object
    value_object: object
    voltage: int = 0
    amps: int = 0
    
    def update_value(self):
        self.value_object.text = str(self.voltage)+" / "+str(self.amps)
    

@dataclass
class Motor:
    label_object: object # object that displays the name of the motor, ex "Motor 1"
    value_object: object # object that displays the pwm of the motor
    pwm: int = tk.IntVar()
    
    def update_value(self):
        self.pwm.set(3)
        self.value_object.text = "3"

@dataclass
class Servo:
    label_object: object
    value_object: object
    pwm: tk.IntVar() = 0
    
    def update_value(self):
        self.value_object.text = self.pwm


# ================= SUB COMMANDS =================

def connect_orin(username, password, ip, port):
    return

def disconnect_orin():
    if orin_connected:
        return
    
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
WINDOW.geometry("600x450")
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
radar_frame.grid(row = 0, column = 0, sticky="nsew", rowspan=1, padx=2, pady=2)

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
connect_button = tk.Button(orin_frame, text="Connect", command=get_window_size)

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

video_display.grid(sticky = "nsew", rowspan = 1, columnspan = 2, padx = 5, pady = 5, ipadx = 3, ipady = 3)

# RADAR FRAME WIDGETS
radar_display = tk.Label(radar_frame)

radar_display.grid(sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)


# DATA DISPLAY
motors = []

servo_display_widgets = []
battery_display_widgets = []

for i in range(MOTOR_COUNT):
    motors.append(Motor(label_object=tk.Label(data_display_frame, text="Motor: "+str(i)), value_object=tk.Label(data_display_frame, text="0")))#
    motors[i].label_object.grid(row = i-(i%2), column=1+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    motors[i].value_object.grid(row = i-(i%2), column=2+(i%2*2), sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)
    motors[i].update_value()
    
# BUTTON FRAME
button_frame = tk.Label(button_frame)

button_frame.grid(sticky = "nsew", rowspan = 1, columnspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)

#  ===== POST CREATION FUNCTIONS / VARS / CONST ======

def stream_video():
    #read the data and seperate it into its index, and frame (we don't need the index so its just an _)
    _, frame = cap.read()
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
    disconnect_orin()
    #destroy the window, since we are overriding the origional functionality
    WINDOW.destroy()


# ======== CLOSING THE APPLICATION =========

WINDOW.protocol("WM_DELETE_WINDOW", close_application)


# ================= RUN =================

#activate the video streaming
VIDEO_THREAD.start()

#run the tk program
WINDOW.mainloop()
