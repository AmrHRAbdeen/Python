###############################################
# Author : Amr Abdeen
# Python Version: 3.8.3
###############################################

### Import Needed Packages ###
import os
from tkinter import Tk
from tkinter import END
from tkinter import INSERT
from tkinter import W
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Text
from tkinter import ttk

############### START: Global Variables ###############################
fileName=""
################## END: Global Variables ###############################

################## START: Define mFileOpen #############################
def mFileOpen():
    global fileName
    fileName = filedialog.askopenfilename(initialdir="C:",title="Locate Compiler",filetypes=(("Compilers","*.exe"),("all files","*.*")))
    browseLocation.config(state="normal")
    browseLocation.delete("1.0",END)
    browseLocation.insert(INSERT,fileName)
    browseLocation.config(state="disable")
    print(fileName)
###################### END: Define mFileOpen #############################
def IDE_selectPath():
    Compiler_Path=filedialog.askdirectory(parent=root, initialdir='C:', title='Please select a directory')
    browseLocation.config(state="normal")
    browseLocation.delete("1.0",END)
    browseLocation.insert(INSERT,Compiler_Path)
    browseLocation.config(state="disable")
    #### List all the Compilers ###
    filesList=[fname for fname in os.listdir(Compiler_Path) if fname.endswith('.exe')]
    optMenu=ttk.Combobox(root,values=filesList,state='readonly')
    print(filesList)
    optMenu.grid(row=2,column=0)


###################### START: Define GenerationEngine #####################
def IDE_Engine():
    ### Define Generation Logic ###
    os.startfile(fileName)

###################### END: Define GenerationEngine ######################


####################### START: Building GUI ############################
root = Tk()
root.wm_iconbitmap(bitmap="IDE_Icon.ico")
root.title(" Th3Abdeen | Embedded IDE ")
root.minsize(700, 100)
root.maxsize(1000,500)
####################### END: Building GUI ##############################



################ START: Create Browse Button #############################
browseButton = Button(root, text="Compiler Path ", command=IDE_selectPath,width = 20)
browseButton.grid(row=0,column=0,padx=10,pady=5)
### Display File Location ###
browseLocation=Text(root,height=1,width=50)
browseLocation.grid(row=0,column=1,padx=10,pady=10,sticky=W)
################### END: Create Browse Button #############################

################ START: Create Generate Button #############################
generateButton = Button(root, text="Compile", command=IDE_Engine,width = 10)
generateButton.grid(row=2,column=4,padx=0,pady=0)
################ END: Create Generate Button   #############################

############################## START: Main #################################
if __name__ == '__main__':
    print("**** Start Application... ***** ")
    root.mainloop(0)

############################# END: Main ####################################




