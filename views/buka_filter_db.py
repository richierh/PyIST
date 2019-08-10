#! usr/bin/env python

import wx
import wx.adv

class FrameFilterDatabase ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer50 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer51 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText206 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Filter pilihan anda berdasarkan kriteria berikut ini", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText206.Wrap( -1 )

        self.m_staticText206.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

        bSizer51.Add( self.m_staticText206, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticline2 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer51.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


        bSizer51.Add( ( 0, 20), 0, 0, 5 )

        self.m_staticText207 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText207.Wrap( -1 )

        bSizer51.Add( self.m_staticText207, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        fgSizer39 = wx.FlexGridSizer( 0, 5, 0, 0 )
        fgSizer39.SetFlexibleDirection( wx.BOTH )
        fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText209 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Dari", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText209.Wrap( -1 )

        fgSizer39.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_datePickerdaritgl = wx.adv.DatePickerCtrl( self.m_panel20, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT|wx.TAB_TRAVERSAL )
        fgSizer39.Add( self.m_datePickerdaritgl, 0, wx.ALL, 5 )

        self.m_staticText210 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Sampai", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText210.Wrap( -1 )

        fgSizer39.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePickersampaitgl = wx.adv.DatePickerCtrl( self.m_panel20, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT|wx.TAB_TRAVERSAL )
        fgSizer39.Add( self.m_datePickersampaitgl, 0, wx.ALL, 5 )


        bSizer51.Add( fgSizer39, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_buttonKlikFilterTanggal = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_buttonKlikFilterTanggal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer51.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText208 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nama Orang", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText208.Wrap( -1 )

        bSizer51.Add( self.m_staticText208, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_textCtrlnamaorang = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.TAB_TRAVERSAL )
        bSizer51.Add( self.m_textCtrlnamaorang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_buttonKlikFilterOrang = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_buttonKlikFilterOrang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer51.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText211 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nomor Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText211.Wrap( -1 )

        bSizer51.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlnomortes = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.TAB_TRAVERSAL )
        bSizer51.Add( self.m_textCtrlnomortes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_buttonKlikFilterNoTes = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_buttonKlikFilterNoTes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline4 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer51.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        fgSizer40 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer40.AddGrowableCol( 0,1 )
        fgSizer40.AddGrowableRow( 0,1 )
        fgSizer40.SetFlexibleDirection( wx.BOTH )
        fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

  
        self.m_buttonFilterBatal = wx.Button( self.m_panel20, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer40.Add( self.m_buttonFilterBatal, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


        bSizer51.Add( fgSizer40, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


        self.m_panel20.SetSizer( bSizer51 )
        self.m_panel20.Layout()
        bSizer51.Fit( self.m_panel20 )
        bSizer50.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer50 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_buttonKlikFilterTanggal.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterTanggalOnButtonClick )
        self.m_buttonKlikFilterOrang.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterOrangOnButtonClick )
        self.m_buttonKlikFilterNoTes.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterNoTesOnButtonClick )
        self.m_buttonFilterBatal.Bind( wx.EVT_BUTTON, self.m_buttonFilterBatalOnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_buttonKlikFilterTanggalOnButtonClick( self, event ):
        event.Skip()

    def m_buttonKlikFilterOrangOnButtonClick( self, event ):
        event.Skip()

    def m_buttonKlikFilterNoTesOnButtonClick( self, event ):
        event.Skip()

    def m_buttonFilterBatalOnButtonClick( self, event ):
        event.Skip()