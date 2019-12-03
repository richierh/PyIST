# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Jun 15 2019)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# # Class DialogSavePDF
###########################################################################


class DialogSavePDF (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(400, 185), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetTitle("Simpan File PDF")

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Direktori", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        fgSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_direktori_pdf = wx.DirPickerCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        fgSizer1.Add(self.m_direktori_pdf, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Nama File", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_filepdf = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_filepdf, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(fgSizer1)
        self.m_panel1.Layout()
        fgSizer1.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_simpanPDF = wx.Button(self.m_panel2, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_simpanPDF, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_batal_simpan = wx.Button(self.m_panel2, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_batal_simpan, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel2.SetSizer(bSizer4)
        self.m_panel2.Layout()
        bSizer4.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_simpanPDF.Bind(wx.EVT_BUTTON, self.m_button_simpanPDFFile)
        self.m_batal_simpan.Bind(wx.EVT_BUTTON, self.m_button_batal_simpanPDF)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_button_simpanPDFFile(self, event):
        event.Skip()

    def m_button_batal_simpanPDF(self, event):
        event.Skip()

