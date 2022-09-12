
import threading
import os
from datetime import datetime
import filecmp


def printit():
  threading.Timer(3.0, printit).start()
  print("Hello, World!" + str(datetime.now()))

path="C:/Users/Bertrand/Desktop/"

src="C:/Users/Bertrand/Desktop/Source/Option 3.pdf"
rep="C:/Users/Bertrand/Desktop/Replicat/Option 3.pdf"

srcF="C:/Users/Bertrand/Desktop/Source/"
repF="C:/Users/Bertrand/Desktop/Replicat/"


def getFileToDelete() :
    #Compare Source and Replica folder and get the files only available in the Replica folder. Return a list of files
    return filecmp.dircmp(srcF,repF).right_only

def getFileToCreate():
    #Compare Source and Replica folder and get the files only available in the Source folder. Return a list of files
    return filecmp.dircmp(srcF,repF).left_only
 

def getMismatchFiles():
    #Compare Source and Replica folder and get a list of common files (not identical). 
    dcCommon = filecmp.dircmp(srcF,repF).common
    #Compare the list of common file to check if there are identical or not. Re
    #The first position of the tab represent the match, second position the mismatch and third position the errors
    return filecmp.cmpfiles(srcF,repF,common=dcCommon,shallow=True)[1] 


def synchroniseFolder():
    #Check if there are file to delete in Replica folder
    deleteList = getFileToDelete()
    if len(deleteList) == 0 :
        print("Zero file to delete")
    else:
        print("Remove files:" + str(deleteList) )

    #Check if new files need to be created
    createList = getFileToCreate()
    if len(createList) == 0 :
        print("Zero file to create")
    else:
        print("Create files:" + str(createList) )

    #Check files to update
    updateList = getMismatchFiles()
    if len(updateList) == 0 :
        print("Zero file to update")
    else:
        print("Update files:" + str(updateList) )




synchroniseFolder()