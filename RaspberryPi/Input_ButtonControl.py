# import Modules
import keyboard
import RPi.GPIO as GPIO
import time
import os

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

# Input Pin
ButtonPress = 4
# set up the needed GPIO pins to OUTPUT
GPIO.setup( [MotorA_EnablePin,MotorA_Input1 ,MotorA_Input2, MotorB_EnablePin,MotorB_Input3,MotorB_Input4] , GPIO.OUT)
GPIO.setup(ButtonPress , GPIO.IN)
# set Motor A and B Enable to HIGH
#GPIO.output( MotorA_EnablePin,GPIO.HIGH)
#GPIO.output( MotorB_EnablePin,GPIO.HIGH)

# Use PWM
MotorA_PWM=GPIO.PWM(MotorA_EnablePin,100)
MotorB_PWM=GPIO.PWM(MotorB_EnablePin,100)
MotorA_PWM.start(100)
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

# Super loop Implementation
while 1:
    #Read Button State
    User_Input =GPIO.input(ButtonPress)
    if(User_Input == True):
        print("Please, Enter a valid Movement")
        GPIO.output(MotorA_Input2,GPIO.HIGH)
    else:
        GPIO.output(MotorA_Input2,GPIO.LOW)

GPIO.cleanup()





