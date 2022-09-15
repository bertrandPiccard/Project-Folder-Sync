import os 
import shutil

#Function to delete extra files or directories in the replica folder (the ones no present in the source folder)
def delete(list,logger,repF):
    for i in list:
        fullPath = os.path.abspath(repF + "/"+i)
        if os.path.isfile(fullPath):
            os.remove(fullPath)
        elif os.path.isdir(fullPath):
            shutil.rmtree(fullPath)
          
        logger.info("[DELETED] " + "'"+ i +"'"+ " was removed from " + os.path.abspath(repF))


# When a file or directory is not existing in the replica, but in the source folder. A copy will be done added in replica folder
def create(list,logger,srcF,repF):
    for i in list:
        fullPathS = os.path.abspath(srcF + "/" +i)
        fullPathR = os.path.abspath(repF + "/" + i)
        if os.path.isfile(fullPathS):
            shutil.copy(fullPathS, fullPathR)
        elif os.path.isdir(fullPathS):
            shutil.copytree(fullPathS, fullPathR)
            
        logger.info("[CREATED] " + "'"+ i +"'"+ " was created in " + os.path.abspath(repF))  


# Update function will remove files from replica folder and copy the version from the source folder
def updateFile(list,logger,srcF,repF):
    for i in list:
        fullPathS = os.path.abspath(srcF + "/" +i)
        fullPathR = os.path.abspath(repF + "/" + i)

        os.remove(fullPathR)
        shutil.copy(fullPathS, fullPathR)
       
        logger.info("[UPDATED] " + "'"+ i +"'"+ " was updated in " + os.path.abspath(repF))    
       
