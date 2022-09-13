
import filecmp
import operation


def getFileToDelete(srcF,repF) :
    #Compare Source and Replica folder and get the files only available in the Replica folder. Return a list of files
    return filecmp.dircmp(srcF,repF).right_only

def getFileToCreate(srcF,repF):
    #Compare Source and Replica folder and get the files only available in the Source folder. Return a list of files
    return filecmp.dircmp(srcF,repF).left_only
 

def getMismatchFiles(srcF,repF):

    filecmp.clear_cache()
    
    #Compare Source and Replica folder and get a list of common files (not identical). 
    dcCommon = filecmp.dircmp(srcF,repF).common_files
    
    subDir = filecmp.dircmp(srcF,repF).common_dirs
    print(filecmp.cmpfiles(srcF,repF,common=subDir,shallow=True))

    #Compare the list of common file to check if there are identical or not. Re
    #The first position of the tab represent the match, second position the mismatch and third position the errors
    return filecmp.cmpfiles(srcF,repF,common=dcCommon,shallow=True)[1] 


def synchroniseFolder(srcF,repF,logger):
    #Check if there are file to delete in Replica folder
    deleteList = getFileToDelete(srcF,repF)
    if len(deleteList) == 0 :
        logger.warning("Zero file to delete...")
    else:
        operation.deleteFiles(deleteList,logger,repF)

    #Check files to update
    updateList = getMismatchFiles(srcF,repF)
    
    if len(updateList) == 0 :
        logger.warning("Zero file to update...")
    else:
        operation.updateFiles(updateList,logger,srcF,repF)

     #Check if new files need to be created
    createList = getFileToCreate(srcF,repF)
    if len(createList) == 0 :
        logger.warning("Zero file to create...")
    else:
        operation.createFiles(createList, logger,srcF,repF)





