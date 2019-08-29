import os
import pathlib

pathloc = pathlib.Path.cwd() / "nem.txt"


def loc():
    
    if os.path.isfile(pathloc) == True :
        return True
    else :
        return False


def createfile():
    f = open(pathloc, mode="w+")
    
    f.close()


print (loc())
