import filecmp
import operations
import os

def getAllSubDir(src):
    # Will retrieve a list of all subdirectories from the directories provided in the parameter
    listSubDir = []
    for root, dirs,files in os.walk(os.path.abspath(src)):
        for dir in dirs:
            listSubDir.append(os.path.join(root, dir))

    return listSubDir

def getToDelete(srcF,repF) :
    #Compare Source and Replica folder and get the files and directories only available in the Replica folder. Return a list of files and directory names
    return filecmp.dircmp(srcF,repF).right_only

def getToCreate(srcF,repF):
    #Compare Source and Replica folder and get the files and directories only available in the Source folder. Return a list of file and directory names
    return filecmp.dircmp(srcF,repF).left_only
 

def getMismatchFiles(srcF,repF):

    filecmp.clear_cache()
    
    #Compare Source and Replica folder and get a list of common files (name matching, not necessarily identical). 
    listFiles = filecmp.dircmp(srcF,repF).common_files
 
    #Compare the list of common file to check if there are identical or not. 
    #The first position of the tab represent the match, second position the mismatch and third position the errors. Here we return the mismatch
    return filecmp.cmpfiles(srcF,repF,common=listFiles,shallow=True)[1] 


def synchroniseFolder(srcF,repF,logger):
    
    #Check if there are files or directories to delete in Replica folder
    deleteList = getToDelete(srcF,repF)
    if len(deleteList) > 0 :
        operations.delete(deleteList,logger,repF)

    #Get and check if files to update in the current folder
    updateList = getMismatchFiles(srcF,repF)
    
    if len(updateList) > 0 :
        operations.updateFile(updateList,logger,srcF,repF)

    #Check if new files or directories in source folder
    createList = getToCreate(srcF,repF)
    if len(createList) > 0 :
        operations.create(createList, logger,srcF,repF)
    
    #Check for subdirectories and will synchronise them as well if needed
    listSubDir = getAllSubDir(srcF)
    if len(listSubDir) > 0:
        for s in listSubDir:
            r = s.removeprefix(srcF)
            r =  os.path.abspath(repF + r)
            synchroniseFolder(s,r,logger)





