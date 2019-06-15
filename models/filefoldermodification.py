'''
Created on Feb 15, 2019

@author: binakarir
'''


import shutil
import pathlib
import os

class ModifFile():
    
    
    def __init__(self,parent):
        self.parent = parent
        pass
    def copy(self,src,dst):
        self.pathsrc = src
        self.pathdst = dst
        return self.parent.copy(self.pathsrc,self.pathdst)

# shutil.copy(src,dst)

if __name__ == '__main__':
    os.chdir("..")
    pathsrc = pathlib.Path.cwd()/"models/ist-master"
    pathdst = pathlib.Path.cwd()/"models/ist"

    runshutil = ModifFile(shutil)
    runshutil.copy(pathsrc,pathdst)