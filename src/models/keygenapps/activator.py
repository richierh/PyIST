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
# # Class FrameActivator
###########################################################################


class FrameActivator (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Silahkan untuk mengaktivasi Aplikasi terlebih dahulu", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		self.m_staticText1.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer1.SetFlexibleDirection(wx.BOTH)
		fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Nomor Lisensi", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)

		self.m_staticText2.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		fgSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

		self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrl1.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		fgSizer1.Add(self.m_textCtrl1, 1, wx.ALL, 5)

		self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Sandi Produk", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		self.m_staticText3.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		fgSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

		self.m_textCtrl2 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
		self.m_textCtrl2.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		fgSizer1.Add(self.m_textCtrl2, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer2.Add(fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		bSizer2.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_bitmap1 = wx.StaticBitmap(self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.m_bitmap1, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button1.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		bSizer3.Add(self.m_button1, 0, wx.ALL, 5)

		self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button2.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		bSizer3.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer2.Add(bSizer3, 0, wx.ALIGN_RIGHT, 5)

		self.m_panel1.SetSizer(bSizer2)
		self.m_panel1.Layout()
		bSizer2.Fit(self.m_panel1)
		bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
		self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick(self, event):
		event.Skip()

	def m_button2OnButtonClick(self, event):
		event.Skip()

