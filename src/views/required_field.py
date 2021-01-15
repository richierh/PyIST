# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov  2 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class RequiredField(wx.Frame):

    def __init__( self, parent ):
        self.parent = parent
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 301,125 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL|wx.STAY_ON_TOP )
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )


        bSizer2.Add( ( 0, 10), 0, 0, 5 )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"No Tes wajib diisi", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableRow( 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Baik", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


        bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_button1OnButtonClick( self, event ):
        try:
            self.parent.m_selanjutnya.Enable()
        except:
            self.parent.m_lanjut.Enable()
        # if self.parent.m_selanjutnya.
        self.Close()
        event.Skip()





if __name__=="__main__":
    root = wx.App()
    run = RequiredField(None).Show()
    root.MainLoop()