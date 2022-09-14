
import filecmp
import operations
import os

def getAllSubDir(src):
    listSubDir = []
    for root, dirs,files in os.walk(os.path.abspath(src)):
        for dir in dirs:
            listSubDir.append(os.path.join(root, dir))

    return listSubDir

def getFileToDelete(srcF,repF) :
    #Compare Source and Replica folder and get the files only available in the Replica folder. Return a list of files
    return filecmp.dircmp(srcF,repF).right_only

def getFileToCreate(srcF,repF):
    #Compare Source and Replica folder and get the files only available in the Source folder. Return a list of files
    return filecmp.dircmp(srcF,repF).left_only
 

def getMismatchFiles(srcF,repF):

    filecmp.clear_cache()
    
    #Compare Source and Replica folder and get a list of common files (not identical). 
    listFiles = filecmp.dircmp(srcF,repF).common_files
 
    #Compare the list of common file to check if there are identical or not. Re
    #The first position of the tab represent the match, second position the mismatch and third position the errors
    return filecmp.cmpfiles(srcF,repF,common=listFiles,shallow=True)[1] 


def synchroniseFolder(srcF,repF,logger):
    
    #Check if there are file to delete in Replica folder
    deleteList = getFileToDelete(srcF,repF)
    if len(deleteList) > 0 :
        operations.deleteFiles(deleteList,logger,repF)

    #Check files to update
    updateList = getMismatchFiles(srcF,repF)
    
    if len(updateList) > 0 :
        operations.updateFiles(updateList,logger,srcF,repF)

     #Check if new files need to be created
    createList = getFileToCreate(srcF,repF)
    if len(createList) > 0 :
        operations.createFiles(createList, logger,srcF,repF)
    
    #Check the subdirectories and will synchronise them as well
    listSubDir = getAllSubDir(srcF)
    if len(listSubDir) > 0:
        for s in listSubDir:
            r = s.removeprefix(srcF)
            r =  os.path.abspath(repF + r)
            synchroniseFolder(s,r,logger)





