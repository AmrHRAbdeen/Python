###############################################
# Author : Amr Abdeen
# Python Version: 3.8.3
###############################################

### Import Needed Packages ###
from openpyxl import workbook
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from tkinter import Tk
from tkinter import END
from tkinter import INSERT
from tkinter import W
from tkinter import ttk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Text

############# START: vLookup Example #############
'''
for row in ws['E5:E91']:
    for cell in row:
       cell.value = "=VLOOKUP(D{0}, 'POD data'!C1:D87, 2, FALSE)".format(cell.row)
'''
############# END: vLookup Example #############

############### START: Global Variables ###############################
fileName = ""
################## END: Global Variables ###############################


################## START: Define mFileOpen #############################
def mFileOpen():
    global fileName
    fileName = filedialog.askopenfilename(initialdir="C:",title="Choose Excel File",filetypes=(("Excel files","*.xlsx"),("all files","*.*")))
    browseLocation.config(state="normal")
    browseLocation.delete("1.0",END)
    browseLocation.insert(INSERT,fileName)
    browseLocation.config(state="disable")
    print(fileName)
###################### END: Define mFileOpen #############################


###################### START: Define GenerationEngine #####################
def GenerationEngine():
    ### Define Generation Logic ###
    pass

###################### END: Define GenerationEngine ######################


####################### START: Building GUI ############################
#import os
root = Tk()
#print("CWD={}".format(os.getcwd()))
### For windows display Only
#root.wm_iconbitmap(bitmap='MS_Excel.ico')
root.title(" Excel Parser ")
root.geometry("680x120")
#Don't allow resizing in the x or y direction
root.resizable(0, 0)
#root.minsize(720, 100)
#root.maxsize(1000,500)
####################### END: Building GUI ##############################

###################### START: Create tabs ##############################
myNoteBook = ttk.Notebook(root)
myNoteBook.pack()
### Each tab will be in a frame
GeneratorFrame = Frame(myNoteBook,width=680,height=120)
AboutFrame = Frame(myNoteBook,width=680,height=120)

GeneratorFrame.pack()
AboutFrame.pack()

myNoteBook.add(GeneratorFrame,text="Generator")
myNoteBook.add(AboutFrame,text="About")

################ START: Create Generate Button #############################
generateButton = Button(GeneratorFrame, text="Generate" , command=GenerationEngine,width=8)
generateButton.grid(row=3,column=2,padx=20,pady=10)
################ END: Create Generate Button   #############################

################ START: Create Browse Button #############################
browseButton = Button(GeneratorFrame, text="browse", command=mFileOpen,width=10)
browseButton.grid(row=0,column=0,padx=10,pady=5)
### Display File Location ###
browseLocation = Text(GeneratorFrame,height=1,width=50)
browseLocation.grid(row=0 , column=1,padx=10,pady=10,sticky=W)
################### END: Create Browse Button #############################

############# START: About Info. #####################
About_Lable = Label(AboutFrame,text="GUI Frame for Multi-purposes usage")
About_Lable.pack(pady=5)
About_Lable = Label(AboutFrame,text="Developed By : Amr Abdeen (amr.abdeen2050@gmail.com)")
About_Lable.pack(pady=10)
############# END  : About Info. #####################


###################### END : Create tabs ##############################

############################## START: Main #################################
if __name__ == '__main__':
    print("**** Start Application... ***** ")
    root.mainloop(0)

############################# END: Main ####################################
