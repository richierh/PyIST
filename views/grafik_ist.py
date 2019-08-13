from numpy import arange, sin, pi
import numpy as np
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

class GrafikLayout():


    def __init__(self, parent):
        # super().__init__(parent)
        self.parent = parent
        self.figure = Figure()
        self.axes = self.figure.add_subplot(121)
        self.axes2 = self.figure.add_subplot(122)
        self.canvas = FigureCanvas(self.parent.m_panel61, -1, self.figure)
        # self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 3, wx.LEFT | wx.TOP | wx.GROW)


        self.parent.m_panel61.SetSizer(self.sizer)
        self.parent.m_panel61.Layout()
        self.parent.m_panel18.Layout()
        # self.SetSizer(self.sizer)
        # self.Fit()

    def draw(self,rw=None,sw=None):
        self.rw = rw
        self.sw = sw
        # print (t)
        x = ["SE","WA","AN","GE","RA","ZR","FA","WU","ME"]
        self.x = arange(len(x))
        
        self.rw = [1,5,7,5,2,6,8,2,1]
        self.axes.plot(x,self.rw)
        self.axes.set_xticks(self.x)
        self.axes.set_ylim(bottom=0,top=20)
        
        self.axes.set_title("Rw Score")

        self.sw = [100,75,87,95,92,96,98,82,91]

        self.axes2.plot(x,self.sw)
        self.axes2.set_xticks(self.x)
        self.axes2.set_ylim(bottom=0,top=150)

        self.axes2.set_title("Sw Score")


class GrafikHasil():


    def __init__(self,parent):
        self.parent = parent
        # self.figure = Figure(figsize=(3,5))
        self.figure = Figure(figsize=(5,5))
        # self.figure.subplots_adjust(left=0.2)

        self.axes = self.figure.add_subplot(111)


        self.canvas = FigureCanvas(self.parent.m_panel22, -1, self.figure)
        # self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 0, wx.CENTER | wx.TOP | wx.GROW)

        self.parent.m_panel22.SetSizer(self.sizer)

        self.parent.m_panel22.Layout()

        self.parent.m_panel7.Layout()
        # self.Fit()

        # self.parent.m_panel18.Layout()
        # self.SetSizer(self.sizer)
        # self.Fit()

    def draw(self):
        # print (t)
        y = ["Kemampuan\nberhitung","Daya ingat\ndan konsentrasi","Kreatifitas",
            "Ketelitian","Judgement", "Daya\nanalisis", "Pengembalian\nkeputusan"]
        self.y = arange(len(y))
        x = [130,136,79,125,128,146,128]
        self.rects = self.axes.barh(y,x,color='green')
        self.axes.set_xlim(left=50,right=150)
        self.axes.set_yticks(self.y)
        self.axes.set_title("PROFIL KEUNGGULAN")
        self.autolabel()



    def autolabel(self):

        """
        Attach a text label above each bar displaying its height
        """
        print ("kesini nggak")
        for rect in self.rects:
            width = rect.get_width()
            frac_height = width/5
            if frac_height > 0.95 :
                label_position = width - (0.07 * width)
            else :
                label_position = width + (0.01 * width)
            self.axes.text(label_position,rect.get_y() + rect.get_height()/2.,
                    '{}' .format(round(width,2)),color = "black",fontweight='bold',
                    ha='left', va='center')


if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = GrafikLayout(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()