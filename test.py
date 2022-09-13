import os
import filecmp
src = "C:/Users/Bertrand/Desktop/Source/"
rep = "C:/Users/Bertrand/Desktop/Replica/"




listDir = filecmp.dircmp(src,rep).common_dirs










def getAllSubDir(src):
    listSubDir = []
    for dirpath, dirs,files in os.walk(os.path.abspath(src)):
        for dir in dirs:
            listSubDir.append(os.path.join(dirpath,dir))

    return listSubDir

list =getAllSubDir(src)


for s in list:
    r = s.removeprefix(os.path.abspath(src))
    r = os.path.abspath(rep + r)
    print(r)

