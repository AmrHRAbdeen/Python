# import Modules
import keyboard
import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# Define Motor_A Variables
MotorA_EnablePin = 13
MotorA_Input1 = 19
MotorA_Input2 = 26
# Define Motor_B Variables
MotorB_EnablePin = 12
MotorB_Input3 = 16
MotorB_Input4 = 20

# set up the needed GPIO pins to OUTPUT
GPIO.setup( [MotorA_EnablePin,MotorA_Input1 ,MotorA_Input2, MotorB_EnablePin,MotorB_Input3,MotorB_Input4] , GPIO.OUT)
# set Motor A and B Enable to HIGH
GPIO.output( MotorA_EnablePin,GPIO.HIGH)
GPIO.output( MotorB_EnablePin,GPIO.HIGH)

# Define Motors Functions
# Move Motors Forward
def Motors_Forward():
    GPIO.output(MotorA_Input1,GPIO.HIGH)
    GPIO.output(MotorA_Input2,GPIO.LOW)
    GPIO.output(MotorB_Input3,GPIO.HIGH)
    GPIO.output(MotorB_Input4,GPIO.LOW)

# Move motors Backward
def Motors_Backward():
    GPIO.output(MotorA_Input1,GPIO.LOW)
    GPIO.output(MotorA_Input2,GPIO.HIGH)
    GPIO.output(MotorB_Input3,GPIO.LOW)
    GPIO.output(MotorB_Input4,GPIO.HIGH)

# Move Motors to the Right
def Motors_Right():
    GPIO.output(MotorA_Input1,GPIO.HIGH)
    GPIO.output(MotorA_Input2,GPIO.LOW)
    GPIO.output(MotorB_Input3,GPIO.LOW)
    GPIO.output(MotorB_Input4,GPIO.HIGH)

# Move the motors to the Left
def Motors_Left():
    GPIO.output(MotorA_Input1,GPIO.LOW)
    GPIO.output(MotorA_Input2,GPIO.HIGH)
    GPIO.output(MotorB_Input3,GPIO.HIGH)
    GPIO.output(MotorB_Input4,GPIO.LOW)

# Stop the motors
def Motors_Stop():
    GPIO.output(MotorA_Input1,GPIO.LOW)
    GPIO.output(MotorA_Input2,GPIO.LOW)
    GPIO.output(MotorB_Input3,GPIO.LOW)
    GPIO.output(MotorB_Input4,GPIO.LOW)

def KeyboardEventHandler(User_Input):
    if(User_Input.name =='f' or User_Input.name == 'F'):
        print(" Robot is moving Forward ...")
        Motors_Forward()
    elif(User_Input.name =='b' or User_Input.name == 'B'):
        print(" Robot is moving Backward ...")
        Motors_Backward()
    elif(User_Input.name =='r' or User_Input.name == 'R'):
        print(" Robot is moving to the Right ...")
        Motors_Right()
    elif(User_Input.name =='l' or User_Input.name == 'L'):
        print(" Robot is moving to the Left ...")                   
        Motors_Left()
    elif(User_Input.name =='s' or User_Input.name == 'S'):
        print(" Robot Stopped...")
        Motors_Stop()
    elif(User_Input.name =='e' or User_Input.name == 'E'):
        quit()
    else:
        print("Please, Enter a valid Movement")

## Print a message to the user
print("Please , Enter Motor Move:\n F for Forward \n B for Backward \n R for Right \n L for left \n S for Stop \n E to Exit \n")
## Listen to the keyboard
keyboard.on_press(KeyboardEventHandler)

# Super loop to keep the script alive for listening
while True:
    pass

GPIO.cleanup()
