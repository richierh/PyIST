import platform
from os.path import isfile
import pathlib
import wx

class Registration(wx.Frame):

    def __init__(self,*args,**kwards):
        super().__init__(*args,**kwards)
        self.SetTitle("Registration Form")
        self.Center()

        
def linux():
    print ("you are entering")
    file_key = "rsun.py"
    print (isfile(file_key))
    # Memilih apakah akan membuka Tampilan Registrasi atau Membuka Tampilan Aplikasi
    if isfile(file_key):
        print ("hell0")

    else:
        print ("the file is not exist")

        # Buka Tampilan Registrasi dan Login 
        root = wx.App()
        WindowsRegister = Registration(None)
        WindowsRegister.Show()
        root.MainLoop()

def windows():
    print ("you are entering windows")


print (platform.system())
platform_dict = {
    "Linux" : linux(),
    "Windows": windows()
}