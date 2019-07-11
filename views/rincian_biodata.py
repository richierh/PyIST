import wx


class RincianBiodata ( wx.Frame ):

    def __init__( self, parent,parent2 ):
        self.parent = parent
        self.parent2 = parent2
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Biodata", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.parent.m_panel15.Show()
        bSizer29 = wx.BoxSizer( wx.VERTICAL )
        self.m_panel19 = wx.Panel( self.parent2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        
        bSizer29.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( bSizer29 )
        self.parent.m_panel15.Layout()
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
