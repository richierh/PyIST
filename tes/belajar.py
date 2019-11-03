# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct  1 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu4 = wx.Menu()
		self.m_menu3 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem6.SetBitmap( wx.Bitmap( u"/home/cireng/Projects/pyist/tes/man.png", wx.BITMAP_TYPE_ANY ) )

		self.m_menu3.Append( self.m_menuItem6 )

		self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem8 )

		self.m_menu4.AppendSubMenu( self.m_menu3, u"MyMenu" )

		self.m_menubar2.Append( self.m_menu4, u"MyMenu" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


