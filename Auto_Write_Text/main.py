# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

##### Needed Packages ######################################
## This app is used to autoWrite Text and press keys
## pip install pyautogui
############################################################
import pyautogui
import time

MessageCnt= 5
while MessageCnt > 0:
    ## Type Message
    time.sleep(2)
    pyautogui.typewrite("Hey!")
    time.sleep(1)
    ## Press Enter
    pyautogui.press('enter')
    time.sleep(2)
    MessageCnt = MessageCnt -1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
