from numpy import arange, sin, pi
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx


class GrafikLayout():

    def __init__(self, parent):
        # super().__init__(parent)
        self.parent = parent
        # self.canvas = FigureCanvas(self, -1, self.figure)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(121)
        self.axes2 = self.figure.add_subplot(122)
        self.canvas = FigureCanvas(self.parent.m_panel61, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 3, wx.LEFT | wx.TOP | wx.GROW)

        self.parent.m_panel61.SetSizer(self.sizer)
        self.parent.m_panel61.Layout()
        self.parent.m_panel18.Layout()
 

        # self.SetSizer(self.sizer)
        # self.Fit()

    def draw(self, nilai_rw_sw, rw=None, sw=None):
        self.rw_sw = nilai_rw_sw
        self.np = np.array(self.rw_sw)
        self.pd = pd.DataFrame(self.np)
        self.rw = self.pd[0].astype(int).tolist()
        self.sw = self.pd[1].astype(int).tolist()
        sumbu_x = ["SE", "WA", "AN", "GE", "RA", "ZR", "FA", "WU", "ME"]
        self.x = arange(len(sumbu_x))
        
        self.axes.plot(sumbu_x, self.rw)
        for x,y in zip(sumbu_x,self.rw):

            label = "{}".format(y)

            self.axes.annotate(label, # this is the text
                        (x,y), # this is the point to label
                        textcoords="offset points", # how to position the text
                        xytext=(0,10), # distance from text to points (x,y)
                        ha='center')


        self.axes.set_xticks(self.x)
        self.axes.set_ylim(bottom=0, top=25)
        
        self.axes.set_title("Rw Score")


        self.axes2.plot(sumbu_x, self.sw)

        for x,y in zip(sumbu_x,self.sw):

            label = "{}".format(y)

            self.axes2.annotate(label, # this is the text
                        (x,y), # this is the point to label
                        textcoords="offset points", # how to position the text
                        xytext=(0,10), # distance from text to points (x,y)
                        ha='center')

        self.axes2.set_xticks(self.x)
        self.axes2.set_ylim(bottom=0, top=175)

        self.axes2.set_title("Sw Score")
        
    

class GrafikHasil():

    def __init__(self, parent):
        self.parent = parent
        # self.figure = Figure(figsize=(3,5))
        self.figure = Figure(figsize=(5, 5))
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

    # def draw(self, nilai_grafik=None):
    #     self.grafik = nilai_grafik
    #     # print (t)
    #     y = ["Kemampuan\nberhitung", "Daya ingat\ndan konsentrasi", "Kreatifitas",
    #         "Ketelitian", "Judgement", "Daya\nanalisis", "Pengembalian\nkeputusan"]
    #     self.y = arange(len(y))
    #     x = [130, 136, 79, 125, 128, 146, 128]
    #     self.rects = self.axes.barh(y, x, color='green')
    #     # self.axes.invert_yaxis()
    #     self.axes.set_xlim(left=50, right=150)
    #     self.axes.set_yticks(self.y)
    #     self.axes.set_title("PROFIL KEUNGGULAN")
    #     self.autolabel()
        

    def autolabel(self):

        """
        Attach a text label above each bar displaying its height
        """
        print ("kesini nggak")
        for rect in self.rects:
            width = rect.get_width()
            frac_height = width / 5
            if frac_height > 0.95 :
                label_position = width - (0.07 * width)
            else :
                label_position = width + (0.01 * width)
            self.axes.text(label_position, rect.get_y() + rect.get_height() / 2.,
                    '{}' .format(round(width, 2)), color="black", fontweight='bold',
                    ha='left', va='center')


class GrafikProfesi():

    def __init__(self, parent):
        self.parent = parent
        # self.figure = Figure(figsize=(3,5))
        self.figure = Figure(figsize=(5, 5))
        # self.figure.subplots_adjust(left=0.2)

        self.axes = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self.parent.m_panel26, -1, self.figure)
        # self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 0, wx.CENTER | wx.TOP | wx.GROW)

        self.parent.m_panel26.SetSizer(self.sizer)

        self.parent.m_panel26.Layout()
        self.parent.m_panel9.Layout()
        # self.Fit()

        # self.parent.m_panel18.Layout()
        # self.SetSizer(self.sizer)
        # self.Fit()

    def draw(self, nilai_grafik=None):
        self.grafik = nilai_grafik
        # print (t)
        x = ["a", "b", "c",
            "d", "e", "f", "g"]
        self.x = arange(len(x))
        y = [130, 136, 79, 125, 128, 146, 128]
        self.rects = self.axes.bar(x, y, color='green')
        # self.axes.invert_yaxis()
        self.axes.set_ylim(bottom=50, top=150)
        self.axes.set_xticks(self.x)
        self.axes.set_title("PROFESI JURUSAN")
        self.autolabel()

    def autolabel(self):

        """
        Attach a text label above each bar displaying its height
        """
        print ("kesini nggak")
        for rect in self.rects:
            print (rect)
            height = rect.get_height()
            frac_height = height / 5
            if frac_height > 0.95 :
                label_position = height - (0.07 * height)
            else :
                label_position = height + (0.01 * height)
            self.axes.text(rect.get_x() + rect.get_width() / 2., label_position,
                    '{}' .format(round(height, 2)), color="black", fontweight='bold',
                    ha='center', va='center')


if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = GrafikLayout(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()
