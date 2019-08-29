# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Oct 29 2018)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# # Class FrameWarningKey
###########################################################################


class FrameWarningKey (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Binakarir", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer56 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel27 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel27.SetBackgroundColour(wx.Colour(251, 216, 176))

		bSizer57 = wx.BoxSizer(wx.VERTICAL)

		bSizer57.Add((0, 25), 0, 0, 5)

		self.m_staticText142 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"SILAHKAN MASUKAN SERIAL LISENSI", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText142.Wrap(-1)

		bSizer57.Add(self.m_staticText142, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer57.Add((0, 25), 0, 0, 5)

		fgSizer36 = wx.FlexGridSizer(3, 2, 0, 0)
		fgSizer36.SetFlexibleDirection(wx.BOTH)
		fgSizer36.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText143 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"No Aplikasi Random", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText143.Wrap(-1)

		fgSizer36.Add(self.m_staticText143, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_staticText144 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText144.Wrap(-1)

		fgSizer36.Add(self.m_staticText144, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_staticText145 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"Seri Lisensi", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText145.Wrap(-1)

		fgSizer36.Add(self.m_staticText145, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

		self.m_textCtrl49 = wx.TextCtrl(self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
		fgSizer36.Add(self.m_textCtrl49, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		fgSizer36.Add((0, 0), 1, wx.EXPAND, 5)

		bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText146 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"status validasi :", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText146.Wrap(-1)

		bSizer3.Add(self.m_staticText146, 0, wx.ALL | wx.EXPAND |  wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

		self.m_staticText6 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText6.Wrap(-1)

		bSizer3.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_bitmap1 = wx.StaticBitmap(self.m_panel27, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.m_bitmap1, 0, wx.ALL, 5)

		self.m_staticText146 = wx.StaticText(self.m_panel27, wx.ID_ANY, u"            ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText146.Wrap(-1)

		bSizer3.Add(self.m_staticText146, 0, wx.ALL | wx.EXPAND |  wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

		fgSizer36.Add(bSizer3, 1, wx.ALIGN_RIGHT, 5)

		bSizer57.Add(fgSizer36, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

		fgSizer37 = wx.FlexGridSizer(0, 3, 0, 0)
		fgSizer37.SetFlexibleDirection(wx.BOTH)
		fgSizer37.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_button38 = wx.Button(self.m_panel27, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer37.Add(self.m_button38, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 5)

		self.m_button39 = wx.Button(self.m_panel27, wx.ID_ANY, u"Validasi", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer37.Add(self.m_button39, 0, wx.ALL | wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)
		
		self.m_button40 = wx.Button(self.m_panel27, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer37.Add(self.m_button40,0 , wx.ALL|wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)
		
		bSizer57.Add(fgSizer37, 0, wx.ALIGN_RIGHT, 5)

		self.m_panel27.SetSizer(bSizer57)
		self.m_panel27.Layout()
		bSizer57.Fit(self.m_panel27)
		bSizer56.Add(self.m_panel27, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer56)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_textCtrl49.Bind(wx.EVT_TEXT, self.m_textCtrl49OnText)
		self.m_button38.Bind(wx.EVT_BUTTON, self.m_button38OnButtonClick)
		self.m_button39.Bind(wx.EVT_BUTTON, self.m_button39OnButtonClick)
		self.m_button40.Bind(wx.EVT_BUTTON, self.m_button40OnButtonClick)
	
	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_button40OnButtonClick(self,event):
		event.Skip()
	
	def m_textCtrl49OnText(self, event):
		event.Skip()

	def m_button38OnButtonClick(self, event):
		event.Skip()

	def m_button39OnButtonClick(self, event):
		event.Skip()


