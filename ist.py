#!usr/bin/env python

'''
Created on Mar 21, 2019

from oscheck import *
import@author: cireng
'''

import gettext
import os
import pathlib
import sys
import platform
from coreapps.views.app import MyApp
from pathlib import Path

pathwd = pathlib.Path.cwd() / "coreapps"
sys.path.append(str(pathwd))
# print (sys.path)
os.chdir(str(pathwd))


class VerifyKey():
    
    
    def __init__(self, parent):
        self.value = parent
        pass
    
    def Verify(self):
        return self.value

    def __repr__(self):
        return str(self.value)


def openWindows():
    gettext.install("myApp")
    run = MyApp(0)
    run.MainLoop()  
    return None

def close():
    from coreapps.views.authenticationFrameWarningKey import authenticationFrameWarningKey
    
    start = authenticationFrameWarningKey(None)
    start.Show()
    return None

if platform.system() == "Windows":
#     print (platform.system())
    my_file = Path("C:\\ProgramData\\3351.txt")
#     print (my_file)
    if my_file.is_file():
        # print ("file ada")
        openWindows()
    else : 
        # print ("file tidak ada")
        KeyVerification = VerifyKey("2")
        # print (KeyVerification.Verify())
        # print (type(KeyVerification))
        if KeyVerification.Verify() == "1":
            openWindows()
        else :
            close()


elif platform.system() == "Linux" :
    print (platform.system())
    my_file = Path.home() / ".3351"
    print (my_file)
    # print (my_file)
    if my_file.is_file():
        print ("file ada")
        openWindows()
        print ("le")
    else : 
        # print ("file tidak ada")
        KeyVerification = VerifyKey("2")
        # print (KeyVerification.Verify())
        # print (type(KeyVerification))
        if KeyVerification.Verify() == "1":
            openWindows()
        else :
            close()