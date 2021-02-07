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
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Text


############### START: Global Variables ###############################
fileName=""
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
root = Tk()
root.wm_iconbitmap(bitmap="MSexcel.ico")
root.title(" Excel Parser ")
root.minsize(700, 100)
root.maxsize(1000,500)
####################### END: Building GUI ##############################



################ START: Create Browse Button #############################
browseButton = Button(root, text="browse", command=mFileOpen,width = 10)
browseButton.grid(row=0,column=0,padx=10,pady=5)
### Display File Location ###
browseLocation=Text(root,height=1,width=50)
browseLocation.grid(row=0,column=1,padx=10,pady=10,sticky=W)
################### END: Create Browse Button #############################

################ START: Create Generate Button #############################
generateButton = Button(root, text="Generate" , command=GenerationEngine,width = 15)
generateButton.grid(row=2,column=4,padx=0,pady=0)
################ END: Create Generate Button   #############################

############################## START: Main #################################
if __name__ == '__main__':
    print("**** Start Application... ***** ")
    root.mainloop(0)

############################# END: Main ####################################