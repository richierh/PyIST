from numpy import arange, sin, pi
import numpy as np
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

class GrafikLayout(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        # self.canvas = FigureCanvas(self.parent.m_panel61, -1, self.figure)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)


        # self.parent.m_panel61.SetSizer(self.sizer)
        # self.parent.m_panel61.Layout()
        # self.parent.m_panel18.Layout()
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        # print (t)
        x = ["SE","WA","AN","GE","RA","ZR","FA","WU","ME"]
        self.x = arange(len(x))
        y = [1,5,7,5,2,6,8,2,1]
        self.axes.plot(x,y)
        self.axes.set_xticks(self.x)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = GrafikLayout(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()   