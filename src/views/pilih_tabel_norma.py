# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 12 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class PilihTabel ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer5 = wx.FlexGridSizer( 2, 0, 0, 0 )
        fgSizer5.AddGrowableCol( 0 )
        fgSizer5.AddGrowableRow( 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer1 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Norma Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.normapendidikan = wx.Button( self.m_panel2, wx.ID_ANY, u"Klik", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.normapendidikan, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Norma Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.normapekerjaan = wx.Button( self.m_panel2, wx.ID_ANY, u"Klik", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.normapekerjaan, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Norma Sendiri", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.normasendiri = wx.Button( self.m_panel2, wx.ID_ANY, u"Klik", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.normasendiri, 0, wx.ALL, 5 )
        
        fgSizer2 = wx.FlexGridSizer( 0, 0, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.buttonclose = wx.Button( self.m_panel1, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.buttonclose, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( fgSizer1 )

        self.m_panel2.Layout()

  

        fgSizer1.Fit( self.m_panel2 )


        fgSizer5.Add( self.m_panel2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        fgSizer5.Add(fgSizer2 ,1, wx.ALIGN_RIGHT,5 )
        # self.m_panel1.SetSizer( fgSizer2 )
        # fgSizer2.Fit( self.m_panel1 )


        self.m_panel1.SetSizer( fgSizer5 )
        self.m_panel1.Layout()

        fgSizer5.Fit( self.m_panel1 )

        bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.normapendidikan.Bind( wx.EVT_BUTTON, self.normapendidikanOnButtonClick )
        self.normapekerjaan.Bind( wx.EVT_BUTTON, self.normapekerjaanOnButtonClick )
        self.normasendiri.Bind( wx.EVT_BUTTON, self.normasendiriOnButtonClick )
        self.buttonclose.Bind( wx.EVT_BUTTON, self.normatabelclose)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def normapendidikanOnButtonClick( self, event ):
        event.Skip()

    def normapekerjaanOnButtonClick( self, event ):
        event.Skip()

    def normasendiriOnButtonClick( self, event ):
        event.Skip()

    def normatabelclose( self, event ):
        event.Skip()