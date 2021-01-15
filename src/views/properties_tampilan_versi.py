'''
Created on Feb 7, 2019

@author: binakarir
'''
import wx
import pathlib


class PropertiesTampilanVersi():
    
    def __init__(self, parent):
        self.parent = parent
        
        self.pathlocicon = pathlib.Path.cwd() / "icons/icon.ico"
       
        self.iconapplication = wx.Icon(str(self.pathlocicon))
  
        self.parent.SetTitle("Binakarir")
        
        self.pathloc = pathlib.Path.cwd() / "logos/binakarir.png"
        
        self.image = wx.Image(str(self.pathloc))
        
        self.re_image = self.image.Rescale(300, 75)
        
        self.parent.m_bitmapLogoBinakarir.SetBitmap(wx.Bitmap(self.re_image))

        pass
