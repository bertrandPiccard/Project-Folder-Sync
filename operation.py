
from genericpath import isfile
import logging
import sys
import os 
import shutil
import sys



#Function to delete extra files in Replica folder (the ones no present in the source folder)
def deleteFiles(list,logger,repF):
    for i in list:
        if os.path.isfile(repF + i):
            os.remove(repF+i)
        elif os.path.isdir(repF + i):
            os.removedirs(repF+i)
        logger.info("[DELETED] " + "'"+ i +"'"+ " was removed form Replica folder")


# When a file or folder is not existing in replica, but in the source folder. A copy will be done added in replica folder
def createFiles(list,logger,srcF,repF):
    for i in list:
        if os.path.isfile(srcF + i):
            shutil.copy(srcF + i, repF + i)
            print("I'm a file")
        elif os.path.isdir(srcF + i):
            shutil.copytree(srcF + i, repF + i)
        logger.info("[CREATED] " + "'"+ i +"'"+ " was created in replica folder")  


# Update function will remove the folder or file from replica folder and copy the version from the source folder
def updateFiles(list,logger,srcF,repF):
    for i in list:
        if os.path.isfile(srcF + i):
            os.remove(repF + i)
            shutil.copy(srcF + i, repF + i)
        elif os.path.isdir(srcF + i):
            os.removedirs(repF + i)
            shutil.copytree(srcF + i, repF + i)

      
    
        logger.info("[UPDATED] " + "'"+ i +"'"+ " was updated in replica folder")    
       
