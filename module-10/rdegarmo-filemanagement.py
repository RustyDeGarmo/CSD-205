'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
7 May 2021
'''

#The purpose of this program is to utilize file management techniques
#import the OS library
import os

#Ask the user for their desired directory with a prompt variable
promptDir = "\nWhat is the path of the directory that you want to go to? "
userDir = input(promptDir)

#create space
print()


#check to see if the directory exists
if os.path.isdir(userDir):

    #Ask the user for the name of the file with a prompt variable and 
    #add the user's directory and file to work with the file in the 
    #correct directory
    promptFile = "\nWhat is the name of the file you want to write to? "
    userFile = f"{userDir}/{input(promptFile)}"

    promptName = "\nWhat is your name? "
    userName = input(promptName)

    promptAddress = "\nWhat is your address? "
    userAddress = input(promptAddress)

    promptPhone = "\nWhat is your phone number? "
    userPhone = input(promptPhone)
    
    #create space
    print()
    #I got an error that access was denied because I had the file open.
    #Check to see if the file is open. Is there another reason that I 
    #would get an access denied error? This only seemed to happen when I
    #had the file open in Word. When I opened the file in Notepad I didn't 
    #seem to get this error. Can you explain that?
    try:
        #open the file to write to it
        with open(userFile, 'w') as fileHandle:
            fileHandle.write(f"{userName}, {userAddress}, {userPhone}")
        #open the file again to read it and print the contents
        with open(userFile) as fileHandle:
            userData = fileHandle.read()
            print("Verify that the information you entered is all correct: ")
            print(userData)
            print()

    except:
        print("Make sure that you don't have the file open!\n")

    
else:
    print("That is not a valid directory")








# py rdegarmo-filemanagement.py