
from genericpath import isfile
import logging
import sys
import os 
import shutil
import sys



#Function to delete extra files in Replica folder (the ones no present in the source folder)
def deleteFiles(list,logger,repF):
    for i in list:
        fullPath = repF + "/"+i
        if os.path.isfile(fullPath):
            os.remove(fullPath)
        elif os.path.isdir(fullPath):
            shutil.rmtree(fullPath)
          
        logger.info("[DELETED] " + "'"+ i +"'"+ " was removed from " + fullPath)


# When a file or folder is not existing in replica, but in the source folder. A copy will be done added in replica folder
def createFiles(list,logger,srcF,repF):
    print(list)
    print(srcF)
    print(repF)
    for i in list:
        fullPathS = os.path.abspath(srcF + "/" +i)
        fullPathR = os.path.abspath(repF + "/" + i)
        if os.path.isfile(fullPathS):
            shutil.copy(fullPathS, fullPathR)
        elif os.path.isdir(fullPathS):
            shutil.copytree(fullPathS, fullPathR)
        logger.info("[CREATED] " + "'"+ i +"'"+ " was created in " + fullPathR)  


# Update function will remove the folder or file from replica folder and copy the version from the source folder
def updateFiles(list,logger,srcF,repF):
    for i in list:
        if os.path.isfile(srcF + i):
            os.remove(repF + i)
            shutil.copy(srcF + i, repF + i)
        elif os.path.isdir(srcF + i):
            shutil.rmtree(repF + i)
            shutil.copytree(srcF + i, repF + i)

      
    
        logger.info("[UPDATED] " + "'"+ i +"'"+ " was updated in replica folder")    
       
