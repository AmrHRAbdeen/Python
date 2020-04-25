import os, sys

'''
Adding a change for Git Tut
1- Create file
2-Content+ = > constant
#include <stdio.h>
#include <string.h>
#include "Std_Types.h"
/*Type defs*/
typedef unsigned char uint8 ;
typedef unsigned short int uint16 ;

int main(void)
{

}
'''
# 1- Create file
# File will be created in the same place from which you run the script
myMainFile = open("Main.c", "w+")
print("File has been created")
# (\n) is interpreted  correctly in Python
# Including the header Files in the Main File
myMainFile.write("#include <stdio.h> \n#include <string.h> \n#include \"Std_Types.h\" \n")
# writing the main function
myMainFile.write("int main(void) \n{\n")
### Writing the repeated code here ###
myMainFile.write("print(\"Hello World \";")
### Writing the End } of Main Function
myMainFile.write("\n}\n")
### Writing the Credentials
myMainFile.write("\\*This file has been created by  Python :D  *\\")
# PS:closing the file is essential for the content to be written
myMainFile.close()
### We need to call gcc.exe to execute this file Main.c
print(r"C:\MinGW\gcc\bin\gcc.exe " + "Main.c")
os.system(r"C:\MinGW\gcc\bin\gcc.exe " + "Main.c")
cwd = os.getcwd()
print(cwd)