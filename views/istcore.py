# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  1 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from wx.lib.agw import ultimatelistctrl as ULC

###########################################################################
# Class VersiIST
###########################################################################

class VersiIST ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Silahkan Pilih Versi IST", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmapLogoBinakarir = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmapLogoBinakarir, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBoxVersiISTChoices = [ u"IST Versi Seleksi", u"IST Versi Binakarir" ]
		self.m_radioBoxVersiIST = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"Pilihan Versi IST", wx.DefaultPosition, wx.DefaultSize, m_radioBoxVersiISTChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBoxVersiIST.SetSelection( 0 )
		bSizer2.Add( self.m_radioBoxVersiIST, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_buttonTutupVersiIST = wx.Button( self.m_panel1, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_buttonTutupVersiIST, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonVersiISTLanjut = wx.Button( self.m_panel1, wx.ID_ANY, u"Lanjut", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_buttonVersiISTLanjut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer4, 1, wx.ALIGN_RIGHT, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonTutupVersiIST.Bind( wx.EVT_BUTTON, self.m_buttonTutupVersiISTOnButtonClick )
		self.m_buttonVersiISTLanjut.Bind( wx.EVT_BUTTON, self.m_buttonVersiISTLanjutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonTutupVersiISTOnButtonClick( self, event ):
		event.Skip()

	def m_buttonVersiISTLanjutOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class ISTUtama
###########################################################################

class ISTUtama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 0), 1, 0, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"INTELLIGENCE STRUCTURE TEST", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextNama = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNama.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextNama, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrlNama = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"Ketik Nama Anda", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrlNama, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticTextNomor = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nomor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNomor.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextNomor, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrlNomor = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrlNomor, 0, wx.ALL, 5 )

		self.m_staticTextUsia = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsia.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextUsia, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinCtrl10 = wx.SpinCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 12, 20, 0 )
		bSizer15.Add( self.m_spinCtrl10, 0, wx.ALL, 5 )

		self.m_staticText218 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Thn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		bSizer15.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_staticTextKelas = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextKelas.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextKelas, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.m_choice2 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer2.Add( self.m_choice2, 0, wx.ALL, 5 )

		self.m_staticText2171 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2171.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2171, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = [ u"SD", u"SMP", u"SMA" ]
		self.m_choice1 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 2 )
		fgSizer2.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticTextAsal_Sekolah = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAsal_Sekolah.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextAsal_Sekolah, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrlAsalSekolah = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.m_textCtrlAsalSekolah, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableCol( 2 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonInput_Jawaban = wx.Button( self.m_panel2, wx.ID_ANY, u"Mulai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonInput_Jawaban.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3.Add( self.m_buttonInput_Jawaban, 0, wx.ALL, 5 )


		fgSizer4.Add( fgSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Biodata Peserta", False )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText91 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SE (Sub Tes 1)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer7.Add( self.m_staticText91, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer7.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer7.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer7.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer7.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer7.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer7.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer7.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer7.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer7.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer7.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer7.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		fgSizer7.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		fgSizer7.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		fgSizer7.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		fgSizer7.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		fgSizer7.Add( self.m_staticText47, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		fgSizer7.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer7.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer7.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl25, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer7.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl26, 0, wx.ALL, 5 )

		self.m_staticText72 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		fgSizer7.Add( self.m_staticText72, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl47 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl47, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer7, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText92 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WA (Sub Tes 2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		self.m_staticText92.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer8.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer8.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer8.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl27.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer8.Add( self.m_textCtrl27, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer8.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer8.Add( self.m_textCtrl28, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer8.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl29 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl29, 0, wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		fgSizer8.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl30 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl30, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		fgSizer8.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl31, 0, wx.ALL, 5 )

		self.m_staticText57 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		fgSizer8.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl32, 0, wx.ALL, 5 )

		self.m_staticText58 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		fgSizer8.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl33 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl33, 0, wx.ALL, 5 )

		self.m_staticText59 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizer8.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl34, 0, wx.ALL, 5 )

		self.m_staticText60 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		fgSizer8.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl35, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer8.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl36 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl36, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		fgSizer8.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl37, 0, wx.ALL, 5 )

		self.m_staticText63 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		fgSizer8.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl38 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl38, 0, wx.ALL, 5 )

		self.m_staticText64 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		fgSizer8.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl39 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl39, 0, wx.ALL, 5 )

		self.m_staticText65 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer8.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl40 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl40, 0, wx.ALL, 5 )

		self.m_staticText66 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		fgSizer8.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl41, 0, wx.ALL, 5 )

		self.m_staticText67 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		fgSizer8.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl42 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl42, 0, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer8.Add( self.m_staticText68, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl43 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl43, 0, wx.ALL, 5 )

		self.m_staticText69 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		fgSizer8.Add( self.m_staticText69, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl44 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl44, 0, wx.ALL, 5 )

		self.m_staticText70 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		fgSizer8.Add( self.m_staticText70, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl45, 0, wx.ALL, 5 )

		self.m_staticText73 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		fgSizer8.Add( self.m_staticText73, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl48 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl48, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer8, 1, wx.EXPAND, 5 )

		fgSizer81 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer81.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText921 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AN (Sub Tes 3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText921.Wrap( -1 )

		self.m_staticText921.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer81.Add( self.m_staticText921, 0, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer81.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl71, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		fgSizer81.Add( self.m_staticText521, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl271 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl271.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
	
		fgSizer81.Add( self.m_textCtrl271, 0, wx.ALL, 5 )

		self.m_staticText531 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )

		fgSizer81.Add( self.m_staticText531, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl281 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl281.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer81.Add( self.m_textCtrl281, 0, wx.ALL, 5 )

		self.m_staticText541 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )

		fgSizer81.Add( self.m_staticText541, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl291 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl291, 0, wx.ALL, 5 )

		self.m_staticText551 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText551.Wrap( -1 )

		fgSizer81.Add( self.m_staticText551, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl301 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl301, 0, wx.ALL, 5 )

		self.m_staticText561 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText561.Wrap( -1 )

		fgSizer81.Add( self.m_staticText561, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl311 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl311, 0, wx.ALL, 5 )

		self.m_staticText571 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText571.Wrap( -1 )

		fgSizer81.Add( self.m_staticText571, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl321 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl321, 0, wx.ALL, 5 )

		self.m_staticText581 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )

		fgSizer81.Add( self.m_staticText581, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl331 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl331, 0, wx.ALL, 5 )

		self.m_staticText591 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )

		fgSizer81.Add( self.m_staticText591, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl341 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl341, 0, wx.ALL, 5 )

		self.m_staticText601 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText601.Wrap( -1 )

		fgSizer81.Add( self.m_staticText601, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl351 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl351, 0, wx.ALL, 5 )

		self.m_staticText611 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText611.Wrap( -1 )

		fgSizer81.Add( self.m_staticText611, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl361 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl361, 0, wx.ALL, 5 )

		self.m_staticText621 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText621.Wrap( -1 )

		fgSizer81.Add( self.m_staticText621, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl371 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl371, 0, wx.ALL, 5 )

		self.m_staticText631 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText631.Wrap( -1 )

		fgSizer81.Add( self.m_staticText631, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl381 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl381, 0, wx.ALL, 5 )

		self.m_staticText641 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText641.Wrap( -1 )

		fgSizer81.Add( self.m_staticText641, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl391 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl391, 0, wx.ALL, 5 )

		self.m_staticText651 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText651.Wrap( -1 )

		fgSizer81.Add( self.m_staticText651, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl401 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl401, 0, wx.ALL, 5 )

		self.m_staticText661 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText661.Wrap( -1 )

		fgSizer81.Add( self.m_staticText661, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl411 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl411, 0, wx.ALL, 5 )

		self.m_staticText671 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText671.Wrap( -1 )

		fgSizer81.Add( self.m_staticText671, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl421 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl421, 0, wx.ALL, 5 )

		self.m_staticText681 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText681.Wrap( -1 )

		fgSizer81.Add( self.m_staticText681, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl431 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl431, 0, wx.ALL, 5 )

		self.m_staticText691 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText691.Wrap( -1 )

		fgSizer81.Add( self.m_staticText691, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl441 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl441, 0, wx.ALL, 5 )

		self.m_staticText701 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText701.Wrap( -1 )

		fgSizer81.Add( self.m_staticText701, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl451 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl451, 0, wx.ALL, 5 )

		self.m_staticText731 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText731.Wrap( -1 )

		fgSizer81.Add( self.m_staticText731, 0, wx.ALL, 5 )

		self.m_textCtrl481 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_textCtrl481, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer81, 1, wx.EXPAND, 5 )

		fgSizer83 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer83.SetFlexibleDirection( wx.BOTH )
		fgSizer83.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer83.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText923 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"GE Subtes 4 (0-32)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText923.Wrap( -1 )

		self.m_staticText923.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer83.Add( self.m_staticText923, 0, wx.ALL, 5 )

		self.m_staticText223 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )

		fgSizer83.Add( self.m_staticText223, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl73 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer83.Add( self.m_textCtrl73, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer83, 0, wx.EXPAND, 5 )

		fgSizer82 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer82.SetFlexibleDirection( wx.BOTH )
		fgSizer82.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer82.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText922 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"RA (Sub Tes 5)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText922.Wrap( -1 )

		self.m_staticText922.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer82.Add( self.m_staticText922, 0, wx.ALL, 5 )

		self.m_staticText222 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer82.Add( self.m_staticText222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl303 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl303, 0, wx.ALL, 5 )

		self.m_staticText522 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText522.Wrap( -1 )

		fgSizer82.Add( self.m_staticText522, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl313 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl313, 0, wx.ALL, 5 )

		self.m_staticText532 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText532.Wrap( -1 )

		fgSizer82.Add( self.m_staticText532, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl323 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl323, 0, wx.ALL, 5 )

		self.m_staticText542 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText542.Wrap( -1 )

		fgSizer82.Add( self.m_staticText542, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl333 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl333, 0, wx.ALL, 5 )

		self.m_staticText552 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText552.Wrap( -1 )

		fgSizer82.Add( self.m_staticText552, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl343 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl343, 0, wx.ALL, 5 )

		self.m_staticText562 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText562.Wrap( -1 )

		fgSizer82.Add( self.m_staticText562, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl353 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl353, 0, wx.ALL, 5 )

		self.m_staticText572 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText572.Wrap( -1 )

		fgSizer82.Add( self.m_staticText572, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl363 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl363, 0, wx.ALL, 5 )

		self.m_staticText582 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText582.Wrap( -1 )

		fgSizer82.Add( self.m_staticText582, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl373 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl373, 0, wx.ALL, 5 )

		self.m_staticText592 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText592.Wrap( -1 )

		fgSizer82.Add( self.m_staticText592, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl383 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl383, 0, wx.ALL, 5 )

		self.m_staticText602 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText602.Wrap( -1 )

		fgSizer82.Add( self.m_staticText602, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl393 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl393, 0, wx.ALL, 5 )

		self.m_staticText612 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText612.Wrap( -1 )

		fgSizer82.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl403 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl403, 0, wx.ALL, 5 )

		self.m_staticText622 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText622.Wrap( -1 )

		fgSizer82.Add( self.m_staticText622, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl413 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl413, 0, wx.ALL, 5 )

		self.m_staticText632 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText632.Wrap( -1 )

		fgSizer82.Add( self.m_staticText632, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl423 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl423, 0, wx.ALL, 5 )

		self.m_staticText642 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText642.Wrap( -1 )

		fgSizer82.Add( self.m_staticText642, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl433 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl433, 0, wx.ALL, 5 )

		self.m_staticText652 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText652.Wrap( -1 )

		fgSizer82.Add( self.m_staticText652, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl443 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl443, 0, wx.ALL, 5 )

		self.m_staticText662 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText662.Wrap( -1 )

		fgSizer82.Add( self.m_staticText662, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl453 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl453, 0, wx.ALL, 5 )

		self.m_staticText672 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText672.Wrap( -1 )

		fgSizer82.Add( self.m_staticText672, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl463 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl463, 0, wx.ALL, 5 )

		self.m_staticText682 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText682.Wrap( -1 )

		fgSizer82.Add( self.m_staticText682, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl473 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl473, 0, wx.ALL, 5 )

		self.m_staticText692 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText692.Wrap( -1 )

		fgSizer82.Add( self.m_staticText692, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl483 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl483, 0, wx.ALL, 5 )

		self.m_staticText702 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText702.Wrap( -1 )

		fgSizer82.Add( self.m_staticText702, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl493 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl493, 0, wx.ALL, 5 )

		self.m_staticText732 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText732.Wrap( -1 )

		fgSizer82.Add( self.m_staticText732, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer82.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer82, 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText219 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"ZR (Sub Tes 6)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		self.m_staticText219.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer16.Add( self.m_staticText219, 0, wx.ALL, 5 )

		self.m_staticText220 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer16.Add( self.m_staticText220, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl100 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl100, 0, wx.ALL, 5 )

		self.m_staticText2211 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2211, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl110 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl110, 0, wx.ALL, 5 )

		self.m_staticText2221 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2221.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2221, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl120 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl120, 0, wx.ALL, 5 )

		self.m_staticText2231 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2231.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2231, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl130 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl130, 0, wx.ALL, 5 )

		self.m_staticText2241 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2241.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2241, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl140 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl140, 0, wx.ALL, 5 )

		self.m_staticText2251 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2251.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2251, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl150 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl150, 0, wx.ALL, 5 )

		self.m_staticText2261 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2261.Wrap( -1 )

		fgSizer16.Add( self.m_staticText2261, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl160 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl160, 0, wx.ALL, 5 )

		self.m_staticText227 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText227.Wrap( -1 )

		fgSizer16.Add( self.m_staticText227, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl170 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl170, 0, wx.ALL, 5 )

		self.m_staticText228 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText228.Wrap( -1 )

		fgSizer16.Add( self.m_staticText228, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl180 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl180, 0, wx.ALL, 5 )

		self.m_staticText229 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText229.Wrap( -1 )

		fgSizer16.Add( self.m_staticText229, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl190 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl190, 0, wx.ALL, 5 )

		self.m_staticText230 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText230.Wrap( -1 )

		fgSizer16.Add( self.m_staticText230, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl200 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl200, 0, wx.ALL, 5 )

		self.m_staticText231 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		fgSizer16.Add( self.m_staticText231, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl210 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl210, 0, wx.ALL, 5 )

		self.m_staticText232 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText232.Wrap( -1 )

		fgSizer16.Add( self.m_staticText232, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl220 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl220, 0, wx.ALL, 5 )

		self.m_staticText233 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText233.Wrap( -1 )

		fgSizer16.Add( self.m_staticText233, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl230 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl230, 0, wx.ALL, 5 )

		self.m_staticText234 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText234.Wrap( -1 )

		fgSizer16.Add( self.m_staticText234, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl240 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl240, 0, wx.ALL, 5 )

		self.m_staticText235 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText235.Wrap( -1 )

		fgSizer16.Add( self.m_staticText235, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl250 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl250, 0, wx.ALL, 5 )

		self.m_staticText236 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText236.Wrap( -1 )

		fgSizer16.Add( self.m_staticText236, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl260 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl260, 0, wx.ALL, 5 )

		self.m_staticText238 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText238.Wrap( -1 )

		fgSizer16.Add( self.m_staticText238, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl270 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl270, 0, wx.ALL, 5 )

		self.m_staticText239 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText239.Wrap( -1 )

		fgSizer16.Add( self.m_staticText239, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl280 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl280, 0, wx.ALL, 5 )

		self.m_staticText240 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText240.Wrap( -1 )

		fgSizer16.Add( self.m_staticText240, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl290 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl290, 0, wx.ALL, 5 )

		self.m_staticText241 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )

		fgSizer16.Add( self.m_staticText241, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl196 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl196, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer16, 1, wx.EXPAND, 5 )

		fgSizer84 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer84.SetFlexibleDirection( wx.BOTH )
		fgSizer84.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer84.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText924 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"FA ( Sub Tes 7 )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText924.Wrap( -1 )

		self.m_staticText924.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer84.Add( self.m_staticText924, 0, wx.ALL, 5 )

		self.m_staticText224 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )

		fgSizer84.Add( self.m_staticText224, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl74 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl74, 0, wx.ALL, 5 )

		self.m_staticText524 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText524.Wrap( -1 )

		fgSizer84.Add( self.m_staticText524, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl274 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl274.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer84.Add( self.m_textCtrl274, 0, wx.ALL, 5 )

		self.m_staticText534 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText534.Wrap( -1 )

		fgSizer84.Add( self.m_staticText534, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl284 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl284.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer84.Add( self.m_textCtrl284, 0, wx.ALL, 5 )

		self.m_staticText544 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText544.Wrap( -1 )

		fgSizer84.Add( self.m_staticText544, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl294 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl294, 0, wx.ALL, 5 )

		self.m_staticText554 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText554.Wrap( -1 )

		fgSizer84.Add( self.m_staticText554, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl304 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl304, 0, wx.ALL, 5 )

		self.m_staticText564 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText564.Wrap( -1 )

		fgSizer84.Add( self.m_staticText564, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl314 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl314, 0, wx.ALL, 5 )

		self.m_staticText574 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText574.Wrap( -1 )

		fgSizer84.Add( self.m_staticText574, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl324 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl324, 0, wx.ALL, 5 )

		self.m_staticText584 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText584.Wrap( -1 )

		fgSizer84.Add( self.m_staticText584, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl334 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl334, 0, wx.ALL, 5 )

		self.m_staticText594 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText594.Wrap( -1 )

		fgSizer84.Add( self.m_staticText594, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl344 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl344, 0, wx.ALL, 5 )

		self.m_staticText604 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText604.Wrap( -1 )

		fgSizer84.Add( self.m_staticText604, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl354 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl354, 0, wx.ALL, 5 )

		self.m_staticText614 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText614.Wrap( -1 )

		fgSizer84.Add( self.m_staticText614, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl364 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl364, 0, wx.ALL, 5 )

		self.m_staticText624 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText624.Wrap( -1 )

		fgSizer84.Add( self.m_staticText624, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl374 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl374, 0, wx.ALL, 5 )

		self.m_staticText634 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText634.Wrap( -1 )

		fgSizer84.Add( self.m_staticText634, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl384 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl384, 0, wx.ALL, 5 )

		self.m_staticText644 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText644.Wrap( -1 )

		fgSizer84.Add( self.m_staticText644, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl394 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl394, 0, wx.ALL, 5 )

		self.m_staticText654 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText654.Wrap( -1 )

		fgSizer84.Add( self.m_staticText654, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl404 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl404, 0, wx.ALL, 5 )

		self.m_staticText664 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText664.Wrap( -1 )

		fgSizer84.Add( self.m_staticText664, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl414 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl414, 0, wx.ALL, 5 )

		self.m_staticText674 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText674.Wrap( -1 )

		fgSizer84.Add( self.m_staticText674, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl424 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl424, 0, wx.ALL, 5 )

		self.m_staticText684 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText684.Wrap( -1 )

		fgSizer84.Add( self.m_staticText684, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl434 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl434, 0, wx.ALL, 5 )

		self.m_staticText694 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText694.Wrap( -1 )

		fgSizer84.Add( self.m_staticText694, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl444 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl444, 0, wx.ALL, 5 )

		self.m_staticText704 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText704.Wrap( -1 )

		fgSizer84.Add( self.m_staticText704, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl454 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl454, 0, wx.ALL, 5 )

		self.m_staticText734 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText734.Wrap( -1 )

		fgSizer84.Add( self.m_staticText734, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl484 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer84.Add( self.m_textCtrl484, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer84, 1, wx.EXPAND, 5 )

		fgSizer85 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer85.SetFlexibleDirection( wx.BOTH )
		fgSizer85.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer85.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText925 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WU (Sub Tes 8)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText925.Wrap( -1 )

		self.m_staticText925.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer85.Add( self.m_staticText925, 0, wx.ALL, 5 )

		self.m_staticText225 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText225.Wrap( -1 )

		fgSizer85.Add( self.m_staticText225, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl75 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl75, 0, wx.ALL, 5 )

		self.m_staticText525 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText525.Wrap( -1 )

		fgSizer85.Add( self.m_staticText525, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl275 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl275.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer85.Add( self.m_textCtrl275, 0, wx.ALL, 5 )

		self.m_staticText535 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText535.Wrap( -1 )

		fgSizer85.Add( self.m_staticText535, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl285 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl285.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer85.Add( self.m_textCtrl285, 0, wx.ALL, 5 )

		self.m_staticText545 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText545.Wrap( -1 )

		fgSizer85.Add( self.m_staticText545, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl295 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl295, 0, wx.ALL, 5 )

		self.m_staticText555 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText555.Wrap( -1 )

		fgSizer85.Add( self.m_staticText555, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl305 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl305, 0, wx.ALL, 5 )

		self.m_staticText565 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText565.Wrap( -1 )

		fgSizer85.Add( self.m_staticText565, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl315 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl315, 0, wx.ALL, 5 )

		self.m_staticText575 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText575.Wrap( -1 )

		fgSizer85.Add( self.m_staticText575, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl325 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl325, 0, wx.ALL, 5 )

		self.m_staticText585 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText585.Wrap( -1 )

		fgSizer85.Add( self.m_staticText585, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl335 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl335, 0, wx.ALL, 5 )

		self.m_staticText595 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText595.Wrap( -1 )

		fgSizer85.Add( self.m_staticText595, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl345 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl345, 0, wx.ALL, 5 )

		self.m_staticText605 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText605.Wrap( -1 )

		fgSizer85.Add( self.m_staticText605, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl355 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl355, 0, wx.ALL, 5 )

		self.m_staticText615 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText615.Wrap( -1 )

		fgSizer85.Add( self.m_staticText615, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl365 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl365, 0, wx.ALL, 5 )

		self.m_staticText625 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText625.Wrap( -1 )

		fgSizer85.Add( self.m_staticText625, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl375 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl375, 0, wx.ALL, 5 )

		self.m_staticText635 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText635.Wrap( -1 )

		fgSizer85.Add( self.m_staticText635, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl385 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl385, 0, wx.ALL, 5 )

		self.m_staticText645 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText645.Wrap( -1 )

		fgSizer85.Add( self.m_staticText645, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl395 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl395, 0, wx.ALL, 5 )

		self.m_staticText655 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText655.Wrap( -1 )

		fgSizer85.Add( self.m_staticText655, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl405 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl405, 0, wx.ALL, 5 )

		self.m_staticText665 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText665.Wrap( -1 )

		fgSizer85.Add( self.m_staticText665, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl415 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl415, 0, wx.ALL, 5 )

		self.m_staticText675 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText675.Wrap( -1 )

		fgSizer85.Add( self.m_staticText675, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl425 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl425, 0, wx.ALL, 5 )

		self.m_staticText685 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText685.Wrap( -1 )

		fgSizer85.Add( self.m_staticText685, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl435 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl435, 0, wx.ALL, 5 )

		self.m_staticText695 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText695.Wrap( -1 )

		fgSizer85.Add( self.m_staticText695, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl445 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl445, 0, wx.ALL, 5 )

		self.m_staticText705 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText705.Wrap( -1 )

		fgSizer85.Add( self.m_staticText705, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl455 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl455, 0, wx.ALL, 5 )

		self.m_staticText735 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText735.Wrap( -1 )

		fgSizer85.Add( self.m_staticText735, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl485 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer85.Add( self.m_textCtrl485, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer85, 1, wx.EXPAND, 5 )

		fgSizer86 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer86.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText926 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"ME (Sub Tes 9)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText926.Wrap( -1 )

		self.m_staticText926.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		fgSizer86.Add( self.m_staticText926, 0, wx.ALL, 5 )

		self.m_staticText226 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText226.Wrap( -1 )

		fgSizer86.Add( self.m_staticText226, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl76 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl76, 0, wx.ALL, 5 )

		self.m_staticText526 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText526.Wrap( -1 )

		fgSizer86.Add( self.m_staticText526, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl276 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl276.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer86.Add( self.m_textCtrl276, 0, wx.ALL, 5 )

		self.m_staticText536 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText536.Wrap( -1 )

		fgSizer86.Add( self.m_staticText536, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl286 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl286.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		fgSizer86.Add( self.m_textCtrl286, 0, wx.ALL, 5 )

		self.m_staticText546 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText546.Wrap( -1 )

		fgSizer86.Add( self.m_staticText546, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl296 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl296, 0, wx.ALL, 5 )

		self.m_staticText556 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText556.Wrap( -1 )

		fgSizer86.Add( self.m_staticText556, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl306 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl306, 0, wx.ALL, 5 )

		self.m_staticText566 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText566.Wrap( -1 )

		fgSizer86.Add( self.m_staticText566, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl316 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl316, 0, wx.ALL, 5 )

		self.m_staticText576 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText576.Wrap( -1 )

		fgSizer86.Add( self.m_staticText576, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl326 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl326, 0, wx.ALL, 5 )

		self.m_staticText586 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText586.Wrap( -1 )

		fgSizer86.Add( self.m_staticText586, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl336 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl336, 0, wx.ALL, 5 )

		self.m_staticText596 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText596.Wrap( -1 )

		fgSizer86.Add( self.m_staticText596, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl346 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl346, 0, wx.ALL, 5 )

		self.m_staticText606 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText606.Wrap( -1 )

		fgSizer86.Add( self.m_staticText606, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl356 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl356, 0, wx.ALL, 5 )

		self.m_staticText616 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText616.Wrap( -1 )

		fgSizer86.Add( self.m_staticText616, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl366 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl366, 0, wx.ALL, 5 )

		self.m_staticText626 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText626.Wrap( -1 )

		fgSizer86.Add( self.m_staticText626, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl376 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl376, 0, wx.ALL, 5 )

		self.m_staticText636 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText636.Wrap( -1 )

		fgSizer86.Add( self.m_staticText636, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl386 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl386, 0, wx.ALL, 5 )

		self.m_staticText646 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText646.Wrap( -1 )

		fgSizer86.Add( self.m_staticText646, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl396 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl396, 0, wx.ALL, 5 )

		self.m_staticText656 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText656.Wrap( -1 )

		fgSizer86.Add( self.m_staticText656, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl406 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl406, 0, wx.ALL, 5 )

		self.m_staticText666 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText666.Wrap( -1 )

		fgSizer86.Add( self.m_staticText666, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl416 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl416, 0, wx.ALL, 5 )

		self.m_staticText676 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText676.Wrap( -1 )

		fgSizer86.Add( self.m_staticText676, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl426 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl426, 0, wx.ALL, 5 )

		self.m_staticText686 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText686.Wrap( -1 )

		fgSizer86.Add( self.m_staticText686, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl436 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl436, 0, wx.ALL, 5 )

		self.m_staticText696 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText696.Wrap( -1 )

		fgSizer86.Add( self.m_staticText696, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl446 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl446, 0, wx.ALL, 5 )

		self.m_staticText706 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText706.Wrap( -1 )

		fgSizer86.Add( self.m_staticText706, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl456 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl456, 0, wx.ALL, 5 )

		self.m_staticText736 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText736.Wrap( -1 )

		fgSizer86.Add( self.m_staticText736, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl486 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_textCtrl486, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer86, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer7 )
		self.m_scrolledWindow1.Layout()
		bSizer7.Fit( self.m_scrolledWindow1 )
		bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer131 = wx.BoxSizer( wx.VERTICAL )

		self.m_button6 = wx.Button( self.m_panel4, wx.ID_ANY, u"Hitung", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_button6, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer131, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel4.SetSizer( bSizer6 )
		self.m_panel4.Layout()
		bSizer6.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"Input Jawaban", False )
		self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.Hide()

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText84 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Sub Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer9.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText83 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer9.Add( self.m_staticText83, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText74 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"SE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer9.Add( self.m_staticText74, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl21 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 10 )
		fgSizer9.Add( self.m_spinCtrl21, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"WA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer9.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.m_spinCtrl22 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl22, 0, wx.ALL, 5 )

		self.m_staticText76 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"AN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer9.Add( self.m_staticText76, 0, wx.ALL, 5 )

		self.m_spinCtrl23 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl23, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"GE (0-32)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		fgSizer9.Add( self.m_staticText77, 0, wx.ALL, 5 )

		self.m_spinCtrl24 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl24, 0, wx.ALL, 5 )

		self.m_staticText78 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"RA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		fgSizer9.Add( self.m_staticText78, 0, wx.ALL, 5 )

		self.m_spinCtrl25 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl25, 0, wx.ALL, 5 )

		self.m_staticText79 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"ZR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer9.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.m_spinCtrl26 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl26, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"FA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer9.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.m_spinCtrl27 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl27, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"WU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer9.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_spinCtrl28 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl28, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"ME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer9.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.m_spinCtrl29 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer9.Add( self.m_spinCtrl29, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer11 )
		self.m_panel5.Layout()
		bSizer11.Fit( self.m_panel5 )
		self.m_notebook1.AddPage( self.m_panel5, u"Input Total", False )
		self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		fgSizer161 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer161.SetFlexibleDirection( wx.BOTH )
		fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText199 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText199.Wrap( -1 )

		fgSizer161.Add( self.m_staticText199, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl155 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl155, 0, wx.ALL, 5 )

		self.m_staticText200 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nomor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText200.Wrap( -1 )

		fgSizer161.Add( self.m_staticText200, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl156 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl156, 0, wx.ALL, 5 )

		self.m_staticText201 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		fgSizer161.Add( self.m_staticText201, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl157 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl157, 0, wx.ALL, 5 )

		self.m_staticText202 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Kelas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )

		fgSizer161.Add( self.m_staticText202, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl158 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl158, 0, wx.ALL, 5 )

		self.m_staticText203 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )

		fgSizer161.Add( self.m_staticText203, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl159 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl159, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer161, 0, 0, 5 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel61 = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )

		fgSizer17 = wx.FlexGridSizer( 12, 3, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText204 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"RW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )

		fgSizer17.Add( self.m_staticText204, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText205 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"SW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )

		fgSizer17.Add( self.m_staticText205, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText206 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"SE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText206.Wrap( -1 )

		fgSizer17.Add( self.m_staticText206, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl160 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl160, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl161 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl161, 0, wx.ALL, 5 )

		self.m_staticText207 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"WA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )

		fgSizer17.Add( self.m_staticText207, 0, wx.ALL, 5 )

		self.m_textCtrl162 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl162, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl163 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl163, 0, wx.ALL, 5 )

		self.m_staticText208 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"AN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		fgSizer17.Add( self.m_staticText208, 0, wx.ALL, 5 )

		self.m_textCtrl164 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl164, 0, wx.ALL, 5 )

		self.m_textCtrl165 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl165, 0, wx.ALL, 5 )

		self.m_staticText209 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"GE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		fgSizer17.Add( self.m_staticText209, 0, wx.ALL, 5 )

		self.m_textCtrl166 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl166, 0, wx.ALL, 5 )

		self.m_textCtrl167 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl167, 0, wx.ALL, 5 )

		self.m_staticText210 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"ME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		fgSizer17.Add( self.m_staticText210, 0, wx.ALL, 5 )

		self.m_textCtrl168 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl168, 0, wx.ALL, 5 )

		self.m_textCtrl169 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl169, 0, wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"RA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		fgSizer17.Add( self.m_staticText211, 0, wx.ALL, 5 )

		self.m_textCtrl170 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl170, 0, wx.ALL, 5 )

		self.m_textCtrl171 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl171, 0, wx.ALL, 5 )

		self.m_staticText212 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"ZR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		fgSizer17.Add( self.m_staticText212, 0, wx.ALL, 5 )

		self.m_textCtrl172 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl172, 0, wx.ALL, 5 )

		self.m_textCtrl173 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl173, 0, wx.ALL, 5 )

		self.m_staticText213 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"FA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		fgSizer17.Add( self.m_staticText213, 0, wx.ALL, 5 )

		self.m_textCtrl174 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl174, 0, wx.ALL, 5 )

		self.m_textCtrl175 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl175, 0, wx.ALL, 5 )

		self.m_staticText214 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"WU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		fgSizer17.Add( self.m_staticText214, 0, wx.ALL, 5 )

		self.m_textCtrl176 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl176, 0, wx.ALL, 5 )

		self.m_textCtrl177 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl177, 0, wx.ALL, 5 )

		self.m_staticText215 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		fgSizer17.Add( self.m_staticText215, 0, wx.ALL, 5 )

		self.m_textCtrl178 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl178, 0, wx.ALL, 5 )

		self.m_textCtrl179 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl179, 0, wx.ALL, 5 )


		fgSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText216 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"IQ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		fgSizer17.Add( self.m_staticText216, 0, wx.ALL, 5 )

		self.m_textCtrl180 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl180, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer17, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer10 )
		self.m_scrolledWindow2.Layout()
		bSizer10.Fit( self.m_scrolledWindow2 )
		bSizer9.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer9 )
		self.m_panel6.Layout()
		bSizer9.Fit( self.m_panel6 )
		self.m_notebook1.AddPage( self.m_panel6, u"View", False )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer12.Add( ( 0, 125), 0, wx.EXPAND, 5 )

		self.m_staticText2191 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"HASIL ANALISIS IST", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2191.Wrap( -1 )

		self.m_staticText2191.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		bSizer12.Add( self.m_staticText2191, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer12.Add( ( 0, 25), 0, 0, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,225 ), wx.LC_REPORT )
		bSizer12.Add( self.m_listCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.LC_REPORT )
		bSizer12.Add( self.m_listCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText217 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Keunggulan akan terisi apabila subjek mendapat skor SW lebih dari 100 pada beberapa subtest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		bSizer12.Add( self.m_staticText217, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel7.SetSizer( bSizer12 )
		self.m_panel7.Layout()
		bSizer12.Fit( self.m_panel7 )
		self.m_notebook1.AddPage( self.m_panel7, u"Keunggulan", False )
		self.m_panel9 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer14.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer14 )
		self.m_panel9.Layout()
		bSizer14.Fit( self.m_panel9 )
		self.m_notebook1.AddPage( self.m_panel9, u"Input Total", False )
		self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		fgSizer171 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer171.AddGrowableCol( 1 )
		fgSizer171.AddGrowableCol( 2 )
		fgSizer171.SetFlexibleDirection( wx.BOTH )
		fgSizer171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_hapus = wx.Button( self.m_panel10, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer171.Add( self.m_button_hapus, 0, wx.ALL, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_filter = wx.Button( self.m_panel10, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button_filter, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button_lihat_dari_database = wx.Button( self.m_panel10, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button_lihat_dari_database, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button_reset = wx.Button( self.m_panel10, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button_reset, 0, wx.ALL, 5 )


		fgSizer171.Add( bSizer17, 0, wx.ALIGN_RIGHT, 5 )


		bSizer16.Add( fgSizer171, 0, wx.EXPAND, 5 )

		self.custom_ultimateList =  ULC.UltimateListCtrl(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,agwStyle = wx.LC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT )

		bSizer16.Add( self.custom_ultimateList , 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer16 )
		self.m_panel10.Layout()
		bSizer16.Fit( self.m_panel10 )
		self.m_notebook1.AddPage( self.m_panel10, u"Database", True )

		bSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrlNama.Bind( wx.EVT_LEFT_UP, self.m_textCtrlNamaOnLeftUp )
		self.m_buttonInput_Jawaban.Bind( wx.EVT_BUTTON, self.m_buttonInput_JawabanOnButtonClick )
		self.m_textCtrl6.Bind( wx.EVT_TEXT, self.m_textCtrl6OnText )
		self.m_textCtrl47.Bind( wx.EVT_TEXT, self.m_textCtrl47OnText )
		self.m_textCtrl7.Bind( wx.EVT_TEXT, self.m_textCtrl7OnText )
		self.m_textCtrl48.Bind( wx.EVT_TEXT, self.m_textCtrl48OnText )
		self.m_textCtrl71.Bind( wx.EVT_TEXT, self.m_textCtrl71OnText )
		self.m_textCtrl481.Bind( wx.EVT_TEXT, self.m_textCtrl481OnText )
		self.m_textCtrl303.Bind( wx.EVT_TEXT, self.m_textCtrl303OnText )
		self.m_textCtrl181.Bind( wx.EVT_TEXT, self.m_textCtrl181OnText )
		self.m_textCtrl100.Bind( wx.EVT_TEXT, self.m_textCtrl100OnText )
		self.m_textCtrl196.Bind( wx.EVT_TEXT, self.m_textCtrl196OnText )
		self.m_textCtrl74.Bind( wx.EVT_TEXT, self.m_textCtrl74OnText )
		self.m_textCtrl484.Bind( wx.EVT_TEXT, self.m_textCtrl484OnText )
		self.m_textCtrl75.Bind( wx.EVT_TEXT, self.m_textCtrl75OnText )
		self.m_textCtrl485.Bind( wx.EVT_TEXT, self.m_textCtrl485OnText )
		self.m_textCtrl76.Bind( wx.EVT_TEXT, self.m_textCtrl76OnText )
		self.m_textCtrl486.Bind( wx.EVT_TEXT, self.m_textCtrl486OnText )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button_lihat )
		self.m_button_hapus.Bind( wx.EVT_BUTTON, self.m_button_hapus_onclick )
		self.m_button_filter.Bind( wx.EVT_BUTTON, self.m_button_filter_onclick )
		self.m_button_lihat_dari_database.Bind( wx.EVT_BUTTON, self.m_button_lihat_dari_database_onclick )
		self.m_button_reset.Bind( wx.EVT_BUTTON, self.m_button_reset_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_textCtrlNamaOnLeftUp( self, event ):
		event.Skip()

	def m_buttonInput_JawabanOnButtonClick( self, event ):
		event.Skip()

	def m_textCtrl6OnText( self, event ):
		event.Skip()

	def m_textCtrl47OnText( self, event ):
		event.Skip()

	def m_textCtrl7OnText( self, event ):
		event.Skip()

	def m_textCtrl48OnText( self, event ):
		event.Skip()

	def m_textCtrl71OnText( self, event ):
		event.Skip()

	def m_textCtrl481OnText( self, event ):
		event.Skip()

	def m_textCtrl303OnText( self, event ):
		event.Skip()

	def m_textCtrl181OnText( self, event ):
		event.Skip()

	def m_textCtrl100OnText( self, event ):
		event.Skip()

	def m_textCtrl196OnText( self, event ):
		event.Skip()

	def m_textCtrl74OnText( self, event ):
		event.Skip()

	def m_textCtrl484OnText( self, event ):
		event.Skip()

	def m_textCtrl75OnText( self, event ):
		event.Skip()

	def m_textCtrl485OnText( self, event ):
		event.Skip()

	def m_textCtrl76OnText( self, event ):
		event.Skip()

	def m_textCtrl486OnText( self, event ):
		event.Skip()

	def m_button6OnButtonClick( self, event ):
		event.Skip()

	def m_button_lihat( self, event ):
		event.Skip()

	def m_button_hapus_onclick( self, event ):
		event.Skip()

	def m_button_filter_onclick( self, event ):
		event.Skip()

	def m_button_lihat_dari_database_onclick( self, event ):
		event.Skip()

	def m_button_reset_onclick( self, event ):
		event.Skip()
