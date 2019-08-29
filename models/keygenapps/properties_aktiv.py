import wx
import pathlib
import cekfile
import random


class PropertiesActiv():

    def __init__(self, parent):
        self.parent = parent
        pathlogos = pathlib.Path.cwd() / "logos/binakarir.png"
        
        self.image = wx.Image(str(pathlogos))
        self.re_image = self.image.Rescale(75, 75)
        self.parent.m_bitmap1.SetBitmap(wx.Bitmap(self.re_image))

        # self.cekFile = cekfile.loc()
        # print (self.cekFile)
        self.__method_checkFile()

    def __method_checkFile(self):
        if cekfile.loc() == False :
            self.rand = random.randint()
            print ("okay this is true")
