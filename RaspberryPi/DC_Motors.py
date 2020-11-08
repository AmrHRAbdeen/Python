# import Modules
import RPi.GPIO as GPIO
import time
import sys
# Define Motor_A Variables
MotorA_EnablePin = 13
MotorA_Input1 = 19
MotorA_Input2 = 26
# Define Motor_B Variables
MotorB_EnablePin = 12
MotorB_Input3 = 16
MotorB_Input4 = 20
# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)
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

# Print a Message to the user
printf("Please , Enter Motor Move:  F for Forward \n B for Backward \n R for Right \n L for left \n S for Stop") 
# Super loop
while TRUE:
	User_Input =input()
    if(User_Input =='f' or User_Input == 'F'):
        print(" Robot is moving Forward ...")
        Motors_Forward()
    elif(User_Input =='b' or User_Input == 'B'):
        print(" Robot is moving Backward ...")
        Motors_Backward()
    elif(User_Input =='r' or User_Input == 'R'):
        print(" Robot is moving to the Right ...")
        Motors_Right()
    elif(User_Input =='l' or User_Input == 'L'):
        print(" Robot is moving to the Left ...")					
        Motors_Left()
    elif(User_Input =='s' or User_Input == 'S'):
        print(" Robot Stopped...")
        Motors_Stop()
    elif(User_Input =='e' or User_Input == 'E'):
        GPIO.cleanup()
        sys.exit()
    else:
        printf("Please, Enter a valid Operation")
