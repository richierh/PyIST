# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Nov 24 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import wx.dataview
from wx.lib.agw import ultimatelistctrl as ULC

###########################################################################
## Class ISTUtama
###########################################################################

class ISTUtama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,686 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_simplebook1 = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 50), 0, 0, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"INTELLIGENCE STRUCTURE TEST", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer19.Add( ( 0, 0), 1, 0, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_data = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledpanel_pendidikan1 = wx.ScrolledWindow( self.m_panel_data, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledpanel_pendidikan1.SetScrollRate( 5, 5 )
		fgSizer21 = wx.FlexGridSizer( 14, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.AddGrowableRow( 0 )
		fgSizer21.AddGrowableRow( 1 )
		fgSizer21.AddGrowableRow( 2 )
		fgSizer21.AddGrowableRow( 3 )
		fgSizer21.AddGrowableRow( 4 )
		fgSizer21.AddGrowableRow( 5 )
		fgSizer21.AddGrowableRow( 6 )
		fgSizer21.AddGrowableRow( 7 )
		fgSizer21.AddGrowableRow( 8 )
		fgSizer21.AddGrowableRow( 9 )
		fgSizer21.AddGrowableRow( 10 )
		fgSizer21.AddGrowableRow( 11 )
		fgSizer21.AddGrowableRow( 12 )
		fgSizer21.AddGrowableRow( 13 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText292 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText292.Wrap( -1 )

		fgSizer21.Add( self.m_staticText292, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_no_tes = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl_no_tes, 0, wx.ALL, 5 )

		self.m_staticText22631 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22631.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22631, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker_tanggal_tes1 = wx.adv.DatePickerCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer21.Add( self.m_datePicker_tanggal_tes1, 0, wx.ALL, 5 )

		self.m_staticText_nama1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_nama1.Wrap( -1 )

		fgSizer21.Add( self.m_staticText_nama1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_nama = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl_nama, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticTextKelas1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextKelas1.Wrap( -1 )

		fgSizer21.Add( self.m_staticTextKelas1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_jenis_kelaminChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.m_choice_jenis_kelamin = wx.Choice( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_jenis_kelaminChoices, 0 )
		self.m_choice_jenis_kelamin.SetSelection( 0 )
		fgSizer21.Add( self.m_choice_jenis_kelamin, 0, wx.ALL, 5 )

		self.m_staticText23211 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23211.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23211, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker_tanggal_lahir = wx.adv.DatePickerCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer21.Add( self.m_datePicker_tanggal_lahir, 0, wx.ALL, 5 )

		self.m_staticTextUsia1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsia1.Wrap( -1 )

		fgSizer21.Add( self.m_staticTextUsia1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_spinCtrl_usia = wx.SpinCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 12, 20, 13 )
		bSizer151.Add( self.m_spinCtrl_usia, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2181 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Thn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2181.Wrap( -1 )

		bSizer48.Add( self.m_staticText2181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer151.Add( bSizer48, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer21.Add( bSizer151, 1, wx.EXPAND, 5 )

		self.m_staticText22721 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Asal Sekolah/Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22721.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22721, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_asal_sekolah_universitas = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_asal_sekolah_universitas, 0, wx.ALL, 5 )

		self.m_staticText22911 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22911.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22911, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_pendidikan_terakhir1Choices = [ u"SD", u"SMP", u"SMA", u"D3", u"S1", u"S2", u"S3" ]
		self.m_choice_pendidikan_terakhir1 = wx.Choice( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_pendidikan_terakhir1Choices, 0 )
		self.m_choice_pendidikan_terakhir1.SetSelection( 4 )
		fgSizer21.Add( self.m_choice_pendidikan_terakhir1, 0, wx.ALL, 5 )

		self.m_staticText22821 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22821.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22821, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jurusan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_jurusan, 0, wx.ALL, 5 )

		self.m_staticText23011 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Posisi Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23011.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23011, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_posisi_pekerjaan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_posisi_pekerjaan, 0, wx.ALL, 5 )

		self.m_staticText23111 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Perusahaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23111.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23111, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_perusahaan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_perusahaan, 0, wx.ALL, 5 )

		self.m_staticText23311 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23311.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23311, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_keterangan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_keterangan, 0, wx.ALL, 5 )


		self.m_scrolledpanel_pendidikan1.SetSizer( fgSizer21 )
		self.m_scrolledpanel_pendidikan1.Layout()
		fgSizer21.Fit( self.m_scrolledpanel_pendidikan1 )
		bSizer251.Add( self.m_scrolledpanel_pendidikan1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel_data.SetSizer( bSizer251 )
		self.m_panel_data.Layout()
		bSizer251.Fit( self.m_panel_data )
		bSizer27.Add( self.m_panel_data, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer19.Add( bSizer27, 5, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer19.Add( ( 0, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_logo_binakarir = wx.StaticBitmap( self.m_panel15, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_logo_binakarir, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer19.Add( ( 0, 0), 2, 0, 5 )


		bSizer5.Add( bSizer19, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel15.SetSizer( bSizer5 )
		self.m_panel15.Layout()
		bSizer5.Fit( self.m_panel15 )
		bSizer22.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer22 )
		self.m_panel1.Layout()
		bSizer22.Fit( self.m_panel1 )
		self.m_simplebook1.AddPage( self.m_panel1, u"Halaman Biodata", False )
		self.m_panel2 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )


		bSizer20.Add( ( 0, 50), 3, wx.EXPAND, 5 )

		self.m_staticText347 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Pilihan Cara Input", wx.DefaultPosition, wx.Size( 230,40 ), 0 )
		self.m_staticText347.Wrap( -1 )

		self.m_staticText347.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer20.Add( self.m_staticText347, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer20.Add( ( 0, 25), 1, wx.EXPAND, 5 )

		self.m_input_manual = wx.Button( self.m_panel2, wx.ID_ANY, u"Input Per Nomor", wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.m_input_manual.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer20.Add( self.m_input_manual, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_input_total = wx.Button( self.m_panel2, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.m_input_total.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer20.Add( self.m_input_total, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer20.Add( ( 0, 0), 3, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer20 )
		self.m_panel2.Layout()
		bSizer20.Fit( self.m_panel2 )
		self.m_simplebook1.AddPage( self.m_panel2, u"Pilihan Cara Input", False )
		self.m_panel3 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_input9 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_input9.Hide()

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel_input9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
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

		self.m_textCtrl1601 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl1601, 0, wx.ALL, 5 )

		self.m_staticText227 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText227.Wrap( -1 )

		fgSizer16.Add( self.m_staticText227, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1701 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl1701, 0, wx.ALL, 5 )

		self.m_staticText228 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText228.Wrap( -1 )

		fgSizer16.Add( self.m_staticText228, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1801 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_textCtrl1801, 0, wx.ALL, 5 )

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

		self.m_button6 = wx.Button( self.m_panel_input9, wx.ID_ANY, u"Hitung", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_button6, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer131, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel_input9.SetSizer( bSizer6 )
		self.m_panel_input9.Layout()
		bSizer6.Fit( self.m_panel_input9 )
		bSizer21.Add( self.m_panel_input9, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_input_total = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_input_total.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_panel_input_total.Hide()

		bSizer11 = wx.BoxSizer( wx.VERTICAL )


		bSizer11.Add( ( 0, 0), 3, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText84 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"Sub Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer9.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText83 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer9.Add( self.m_staticText83, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText74 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"SE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer9.Add( self.m_staticText74, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_se = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_se, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"WA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer9.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_wa = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_wa, 0, wx.ALL, 5 )

		self.m_staticText76 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"AN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer9.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_an = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_an, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"GE (0-32)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		fgSizer9.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_ge = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 32, 0 )
		fgSizer9.Add( self.m_spinCtrl_ge, 0, wx.ALL, 5 )

		self.m_staticText78 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"RA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		fgSizer9.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_ra = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_ra, 0, wx.ALL, 5 )

		self.m_staticText79 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"ZR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer9.Add( self.m_staticText79, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_zr = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_zr, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"FA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer9.Add( self.m_staticText80, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_fa = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_fa, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"WU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer9.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_wu = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_wu, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_panel_input_total, wx.ID_ANY, u"ME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer9.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl_me = wx.SpinCtrl( self.m_panel_input_total, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 20, 0 )
		fgSizer9.Add( self.m_spinCtrl_me, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer9, 1, wx.EXPAND, 5 )


		bSizer11.Add( ( 0, 0), 5, wx.EXPAND, 5 )


		self.m_panel_input_total.SetSizer( bSizer11 )
		self.m_panel_input_total.Layout()
		bSizer11.Fit( self.m_panel_input_total )
		bSizer21.Add( self.m_panel_input_total, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel_input = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer23.Add( fgSizer23, 1, wx.EXPAND, 5 )

		self.m_grid2 = wx.grid.Grid( self.m_panel_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 20, 18 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 30 )
		self.m_grid2.SetColSize( 1, 80 )
		self.m_grid2.SetColSize( 2, 30 )
		self.m_grid2.SetColSize( 3, 80 )
		self.m_grid2.SetColSize( 4, 30 )
		self.m_grid2.SetColSize( 5, 80 )
		self.m_grid2.SetColSize( 6, 30 )
		self.m_grid2.SetColSize( 7, 80 )
		self.m_grid2.SetColSize( 8, 30 )
		self.m_grid2.SetColSize( 9, 80 )
		self.m_grid2.SetColSize( 10, 30 )
		self.m_grid2.SetColSize( 11, 80 )
		self.m_grid2.SetColSize( 12, 30 )
		self.m_grid2.SetColSize( 13, 80 )
		self.m_grid2.SetColSize( 14, 30 )
		self.m_grid2.SetColSize( 15, 80 )
		self.m_grid2.SetColSize( 16, 30 )
		self.m_grid2.SetColSize( 17, 80 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( False )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( False )
		self.m_grid2.SetRowLabelSize( 1 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid2.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		# Cell Defaults
		self.m_grid2.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.m_grid2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer23.Add( self.m_grid2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel_input.SetSizer( bSizer23 )
		self.m_panel_input.Layout()
		bSizer23.Fit( self.m_panel_input )
		bSizer21.Add( self.m_panel_input, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel3.SetSizer( bSizer21 )
		self.m_panel3.Layout()
		bSizer21.Fit( self.m_panel3 )
		self.m_simplebook1.AddPage( self.m_panel3, u"Jenis Input", False )
		self.m_panel221 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer321 = wx.BoxSizer( wx.VERTICAL )


		bSizer321.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button = wx.Button( self.m_panel221, wx.ID_ANY, u"Norma Usia", wx.DefaultPosition, wx.Size( 250,75 ), 0 )
		bSizer321.Add( self.m_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button20 = wx.Button( self.m_panel221, wx.ID_ANY, u"Norma Pendidikan", wx.DefaultPosition, wx.Size( 250,75 ), 0 )
		bSizer321.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel35 = wx.Panel( self.m_panel221, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer26 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer26.AddGrowableCol( 0 )
		fgSizer26.AddGrowableCol( 1 )
		fgSizer26.AddGrowableCol( 2 )
		fgSizer26.AddGrowableRow( 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer26.Add( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button21 = wx.Button( self.m_panel35, wx.ID_ANY, u"Norma Sendiri", wx.DefaultPosition, wx.Size( 250,75 ), 0 )
		fgSizer26.Add( self.m_button21, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )


		bSizer54.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel36 = wx.Panel( self.m_panel35, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel36.SetBackgroundColour( wx.Colour( 138, 126, 126 ) )

		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		self.LNormaSendiri = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Belum ada", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.LNormaSendiri.Wrap( -1 )

		self.LNormaSendiri.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.LNormaSendiri.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer55.Add( self.LNormaSendiri, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel36.SetSizer( bSizer55 )
		self.m_panel36.Layout()
		bSizer55.Fit( self.m_panel36 )
		bSizer54.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button32 = wx.Button( self.m_panel35, wx.ID_ANY, u"Buka Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer54.Add( self.m_button32, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer26.Add( bSizer54, 1, wx.EXPAND, 5 )


		self.m_panel35.SetSizer( fgSizer26 )
		self.m_panel35.Layout()
		fgSizer26.Fit( self.m_panel35 )
		bSizer321.Add( self.m_panel35, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer321.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel221.SetSizer( bSizer321 )
		self.m_panel221.Layout()
		bSizer321.Fit( self.m_panel221 )
		self.m_simplebook1.AddPage( self.m_panel221, u"Pilih Norma", False )
		self.m_panel6 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		fgSizer161 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer161.SetFlexibleDirection( wx.BOTH )
		fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText199 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText199.Wrap( -1 )

		fgSizer161.Add( self.m_staticText199, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_biodata = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_textCtrl_biodata, 0, wx.ALL, 5 )

		self.m_button_rincian_biodata = wx.Button( self.m_panel6, wx.ID_ANY, u"Biodata", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_button_rincian_biodata, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer161, 0, 0, 5 )

		self.m_panel18 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_scrolledWindow7 = wx.ScrolledWindow( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel61 = wx.Panel( self.m_scrolledWindow7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32.Add( self.m_panel61, 2, wx.EXPAND |wx.ALL, 5 )

		fgSizer17 = wx.FlexGridSizer( 12, 3, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText204 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"RW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )

		fgSizer17.Add( self.m_staticText204, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText205 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"SW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )

		fgSizer17.Add( self.m_staticText205, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText206 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"SE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText206.Wrap( -1 )

		fgSizer17.Add( self.m_staticText206, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_se = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_se, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_se = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_se, 0, wx.ALL, 5 )

		self.m_staticText207 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"WA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )

		fgSizer17.Add( self.m_staticText207, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_wa = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_wa, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_wa = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_wa, 0, wx.ALL, 5 )

		self.m_staticText208 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"AN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		fgSizer17.Add( self.m_staticText208, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_an = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_an, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_an = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_an, 0, wx.ALL, 5 )

		self.m_staticText209 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"GE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		fgSizer17.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_ge = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_ge, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_ge = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_ge, 0, wx.ALL, 5 )

		self.m_staticText210 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"ME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		fgSizer17.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_me = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_me, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_me = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_me, 0, wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"RA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		fgSizer17.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_ra = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_ra, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_ra = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_ra, 0, wx.ALL, 5 )

		self.m_staticText212 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"ZR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		fgSizer17.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_zr = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_zr, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_zr = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_zr, 0, wx.ALL, 5 )

		self.m_staticText213 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"FA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		fgSizer17.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_fa = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_fa, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_fa = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_fa, 0, wx.ALL, 5 )

		self.m_staticText214 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"WU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		fgSizer17.Add( self.m_staticText214, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_wu = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_wu, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_sw_wu = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_sw_wu, 0, wx.ALL, 5 )

		self.m_staticText215 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		fgSizer17.Add( self.m_staticText215, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_nilai_rw_jumlah = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_rw_jumlah, 0, wx.ALL, 5 )

		self.m_textCtrl_nilai_total_sw = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_total_sw, 0, wx.ALL, 5 )


		fgSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText216 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"IQ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		fgSizer17.Add( self.m_staticText216, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_nilai_IQ = wx.TextCtrl( self.m_scrolledWindow7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		fgSizer17.Add( self.m_textCtrl_nilai_IQ, 0, wx.ALL, 5 )


		bSizer32.Add( fgSizer17, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow7.SetSizer( bSizer32 )
		self.m_scrolledWindow7.Layout()
		bSizer32.Fit( self.m_scrolledWindow7 )
		bSizer10.Add( self.m_scrolledWindow7, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel18.SetSizer( bSizer10 )
		self.m_panel18.Layout()
		bSizer10.Fit( self.m_panel18 )
		bSizer9.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer9 )
		self.m_panel6.Layout()
		bSizer9.Fit( self.m_panel6 )
		self.m_simplebook1.AddPage( self.m_panel6, u"Hasil Norma", False )
		self.m_panel7 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer12.Add( ( 0, 25), 0, 0, 5 )

		self.m_staticText2191 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"HASIL ANALISIS IST", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2191.Wrap( -1 )

		self.m_staticText2191.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		bSizer12.Add( self.m_staticText2191, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer12.Add( ( 0, 25), 0, 0, 5 )

		self.m_panel22 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText217 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Keunggulan akan terisi apabila subjek mendapat skor SW lebih dari 100 pada beberapa subtest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		self.m_staticText217.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer12.Add( self.m_staticText217, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel7.SetSizer( bSizer12 )
		self.m_panel7.Layout()
		bSizer12.Fit( self.m_panel7 )
		self.m_simplebook1.AddPage( self.m_panel7, u"Hasil Analisis IST", False )
		self.m_panel9 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		fgSizer231 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer231.SetFlexibleDirection( wx.BOTH )
		fgSizer231.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_save_as_pdf = wx.Button( self.m_panel9, wx.ID_ANY, u"Save As PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer231.Add( self.m_button_save_as_pdf, 0, wx.ALL, 5 )

		self.m_button_print_pdf = wx.Button( self.m_panel9, wx.ID_ANY, u"Print PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer231.Add( self.m_button_print_pdf, 0, wx.ALL, 5 )

		self.m_button_simpan = wx.Button( self.m_panel9, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer231.Add( self.m_button_simpan, 0, wx.ALL, 5 )

		self.m_button_reset_1 = wx.Button( self.m_panel9, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer231.Add( self.m_button_reset_1, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer231, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListCtrl1.Hide()

		self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"Bidang Keilmuan", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"Fakultas", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"Jurusan", wx.dataview.DATAVIEW_CELL_INERT, 300, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer14.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel26 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel9.SetSizer( bSizer14 )
		self.m_panel9.Layout()
		bSizer14.Fit( self.m_panel9 )
		self.m_simplebook1.AddPage( self.m_panel9, u"Penjurusan", False )
		self.m_panel10 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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

		self.custom_ultimateList .Hide()

		bSizer16.Add( self.custom_ultimateList , 1, wx.ALL|wx.EXPAND, 5 )

		self.m_dataViewListCtrl2 = wx.dataview.DataViewListCtrl( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn4 = self.m_dataViewListCtrl2.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn5 = self.m_dataViewListCtrl2.AppendTextColumn( u"No Tes", wx.dataview.DATAVIEW_CELL_INERT, 150, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn6 = self.m_dataViewListCtrl2.AppendTextColumn( u"Nama Kandidat", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn7 = self.m_dataViewListCtrl2.AppendTextColumn( u"Tanggal Lahir", wx.dataview.DATAVIEW_CELL_INERT, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer16.Add( self.m_dataViewListCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer16 )
		self.m_panel10.Layout()
		bSizer16.Fit( self.m_panel10 )
		self.m_simplebook1.AddPage( self.m_panel10, u"Halaman Terakhir", False )

		bSizer3.Add( self.m_simplebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer18 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer18.AddGrowableCol( 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_kembali_ke_awal = wx.Button( self.m_panel11, wx.ID_ANY, u"Ke Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_kembali_ke_awal, 0, wx.ALL, 5 )

		self.m_sebelumnya = wx.Button( self.m_panel11, wx.ID_ANY, u"Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_sebelumnya, 0, wx.ALL, 5 )

		self.m_selanjutnya = wx.Button( self.m_panel11, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_selanjutnya, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( fgSizer18 )
		self.m_panel11.Layout()
		fgSizer18.Fit( self.m_panel11 )
		bSizer3.Add( self.m_panel11, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu_keluar = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menu_keluar )

		self.m_menubar1.Append( self.m_menu1, u"Berkas" )

		self.m_menu3 = wx.Menu()
		self.MenuTabelNorma = wx.Menu()
		self.m_menuItem_daftar_tabel_norma = wx.MenuItem( self.MenuTabelNorma, wx.ID_ANY, u"Daftar Tabel Norma", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuTabelNorma.Append( self.m_menuItem_daftar_tabel_norma )

		self.MenuTabelNorma.AppendSeparator()

		self.m_menuItem5 = wx.MenuItem( self.MenuTabelNorma, wx.ID_ANY, u"Lihat Data Peserta", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/menubar/man.png", wx.BITMAP_TYPE_ANY ) )
		self.MenuTabelNorma.Append( self.m_menuItem5 )

		self.m_menu3.AppendSubMenu( self.MenuTabelNorma, u"Data" )

		self.m_menubar1.Append( self.m_menu3, u"Pengaturan" )

		self.m_menu2 = wx.Menu()
		self.m_menu_bantuan = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Bantuan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menu_bantuan )

		self.m_menubar1.Append( self.m_menu2, u"Tentang" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl_no_tes.Bind( wx.EVT_TEXT, self.requiredclick )
		self.m_textCtrl_nama.Bind( wx.EVT_LEFT_UP, self.m_textCtrl_namaOnLeftUp )
		self.m_input_manual.Bind( wx.EVT_BUTTON, self.m_input_manualOnButtonClick )
		self.m_input_total.Bind( wx.EVT_BUTTON, self.m_input_totalOnButtonClick )
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
		self.m_button.Bind( wx.EVT_BUTTON, self.m_button_norma_usia )
		self.m_button20.Bind( wx.EVT_BUTTON, self.m_button_norma_pekerjaan )
		self.m_button21.Bind( wx.EVT_BUTTON, self.m_button_norma_sendiri )
		self.m_button32.Bind( wx.EVT_BUTTON, self.m_buka_pilih_norma )
		self.m_button_rincian_biodata.Bind( wx.EVT_BUTTON, self.m_button_rincian_biodata_on_buttonclick )
		self.m_button_save_as_pdf.Bind( wx.EVT_BUTTON, self.m_button_save_as_pdfOnButtonClick )
		self.m_button_print_pdf.Bind( wx.EVT_BUTTON, self.m_button_print_pdfOnButtonClick )
		self.m_button_simpan.Bind( wx.EVT_BUTTON, self.m_button_simpanOnButtonClick )
		self.m_button_reset_1.Bind( wx.EVT_BUTTON, self.m_button_reset_1OnButtonClick )
		self.m_button_hapus.Bind( wx.EVT_BUTTON, self.m_button_hapus_onclick )
		self.m_button_filter.Bind( wx.EVT_BUTTON, self.m_button_filter_onclick )
		self.m_button_lihat_dari_database.Bind( wx.EVT_BUTTON, self.m_button_lihat_dari_database_onclick )
		self.m_button_reset.Bind( wx.EVT_BUTTON, self.m_button_reset_onclick )
		self.m_kembali_ke_awal.Bind( wx.EVT_BUTTON, self.m_kembali_ke_awalOnButtonClick )
		self.m_sebelumnya.Bind( wx.EVT_BUTTON, self.m_sebelumnyaOnButtonClick )
		self.m_selanjutnya.Bind( wx.EVT_BUTTON, self.m_selanjutnyaOnButtonClick )
		self.Bind( wx.EVT_MENU, self.m_menu_keluarOnMenuSelection, id = self.m_menu_keluar.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem_daftar_tabel_normaOnMenuSelection, id = self.m_menuItem_daftar_tabel_norma.GetId() )
		self.Bind( wx.EVT_MENU, self.menubar_lihat_data_peserta, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menu_bantuanOnMenuSelection, id = self.m_menu_bantuan.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def requiredclick( self, event ):
		event.Skip()

	def m_textCtrl_namaOnLeftUp( self, event ):
		event.Skip()

	def m_input_manualOnButtonClick( self, event ):
		event.Skip()

	def m_input_totalOnButtonClick( self, event ):
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

	def m_button_norma_usia( self, event ):
		event.Skip()

	def m_button_norma_pekerjaan( self, event ):
		event.Skip()

	def m_button_norma_sendiri( self, event ):
		event.Skip()

	def m_buka_pilih_norma( self, event ):
		event.Skip()

	def m_button_rincian_biodata_on_buttonclick( self, event ):
		event.Skip()

	def m_button_save_as_pdfOnButtonClick( self, event ):
		event.Skip()

	def m_button_print_pdfOnButtonClick( self, event ):
		event.Skip()

	def m_button_simpanOnButtonClick( self, event ):
		event.Skip()

	def m_button_reset_1OnButtonClick( self, event ):
		event.Skip()

	def m_button_hapus_onclick( self, event ):
		event.Skip()

	def m_button_filter_onclick( self, event ):
		event.Skip()

	def m_button_lihat_dari_database_onclick( self, event ):
		event.Skip()

	def m_button_reset_onclick( self, event ):
		event.Skip()

	def m_kembali_ke_awalOnButtonClick( self, event ):
		event.Skip()

	def m_sebelumnyaOnButtonClick( self, event ):
		event.Skip()

	def m_selanjutnyaOnButtonClick( self, event ):
		event.Skip()

	def m_menu_keluarOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem_daftar_tabel_normaOnMenuSelection( self, event ):
		event.Skip()

	def menubar_lihat_data_peserta( self, event ):
		event.Skip()

	def m_menu_bantuanOnMenuSelection( self, event ):
		event.Skip()


###########################################################################
## Class Norma
###########################################################################

class Norma ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 498,383 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer21.AddGrowableCol( 4 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button22 = wx.Button( self.m_panel23, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button_buat_tabel_norma = wx.Button( self.m_panel23, wx.ID_ANY, u"Buat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_buat_tabel_norma, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self.m_panel23, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self.m_panel23, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button_tutup_norma = wx.Button( self.m_panel23, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_tutup_norma, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer34.Add( fgSizer21, 0, wx.EXPAND, 5 )

		self.text_norma_pendidikan = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Norma Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_norma_pendidikan.Wrap( -1 )

		self.text_norma_pendidikan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer34.Add( self.text_norma_pendidikan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_dataViewListCtrl8 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn45 = self.m_dataViewListCtrl8.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_REORDERABLE|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn46 = self.m_dataViewListCtrl8.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_REORDERABLE|wx.dataview.DATAVIEW_COL_RESIZABLE|wx.dataview.DATAVIEW_COL_SORTABLE )
		self.m_dataViewListColumn47 = self.m_dataViewListCtrl8.AppendTextColumn( u"Nama Norma", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_REORDERABLE|wx.dataview.DATAVIEW_COL_RESIZABLE|wx.dataview.DATAVIEW_COL_SORTABLE )
		self.m_dataViewListColumn50 = self.m_dataViewListCtrl8.AppendTextColumn( u"Usia", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_REORDERABLE|wx.dataview.DATAVIEW_COL_RESIZABLE|wx.dataview.DATAVIEW_COL_SORTABLE )
		self.m_dataViewListColumn49 = self.m_dataViewListCtrl8.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_REORDERABLE|wx.dataview.DATAVIEW_COL_RESIZABLE|wx.dataview.DATAVIEW_COL_SORTABLE )
		bSizer34.Add( self.m_dataViewListCtrl8, 3, wx.ALL|wx.EXPAND, 5 )

		self.text_norma_pekerjaan = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Norma Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_norma_pekerjaan.Wrap( -1 )

		self.text_norma_pekerjaan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer34.Add( self.text_norma_pekerjaan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_dataViewListCtrl9 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn42 = self.m_dataViewListCtrl9.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn43 = self.m_dataViewListCtrl9.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn44 = self.m_dataViewListCtrl9.AppendTextColumn( u"Nama Norma", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn48 = self.m_dataViewListCtrl9.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer34.Add( self.m_dataViewListCtrl9, 1, wx.ALL|wx.EXPAND, 5 )

		self.text_norma_sendiri = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Norma Sendiri", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_norma_sendiri.Wrap( -1 )

		self.text_norma_sendiri.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer34.Add( self.text_norma_sendiri, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_dataViewListCtrl3 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn9 = self.m_dataViewListCtrl3.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn56 = self.m_dataViewListCtrl3.AppendTextColumn( u"IdNorma", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn10 = self.m_dataViewListCtrl3.AppendTextColumn( u"Nama Norma", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn57 = self.m_dataViewListCtrl3.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn8 = self.m_dataViewListCtrl3.AppendTextColumn( u"NormaId", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer34.Add( self.m_dataViewListCtrl3, 3, wx.ALL|wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer34 )
		self.m_panel23.Layout()
		bSizer34.Fit( self.m_panel23 )
		bSizer33.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_buat_tabel_norma.Bind( wx.EVT_BUTTON, self.m_button_buat_tabel_normaOnButtonClick )
		self.m_button25.Bind( wx.EVT_BUTTON, self.hapus_data_peserta )
		self.m_button_tutup_norma.Bind( wx.EVT_BUTTON, self.m_button_tutup_normaOnButtonClick )
		self.m_dataViewListCtrl8.Bind( wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.m_dataViewListCtrl8OnDataViewListCtrlItemValueChanged, id = wx.ID_ANY )
		self.m_dataViewListCtrl9.Bind( wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.m_dataViewListCtrl9OnDataViewListCtrlItemValueChanged, id = wx.ID_ANY )
		self.m_dataViewListCtrl3.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.m_dataViewListCtrl3OnDataViewListCtrlItemActivated, id = wx.ID_ANY )
		self.m_dataViewListCtrl3.Bind( wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.m_dataViewListCtrl3OnDataViewListCtrlItemValueChanged, id = wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_buat_tabel_normaOnButtonClick( self, event ):
		event.Skip()

	def hapus_data_peserta( self, event ):
		event.Skip()

	def m_button_tutup_normaOnButtonClick( self, event ):
		event.Skip()

	def m_dataViewListCtrl8OnDataViewListCtrlItemValueChanged( self, event ):
		event.Skip()

	def m_dataViewListCtrl9OnDataViewListCtrlItemValueChanged( self, event ):
		event.Skip()

	def m_dataViewListCtrl3OnDataViewListCtrlItemActivated( self, event ):
		event.Skip()

	def m_dataViewListCtrl3OnDataViewListCtrlItemValueChanged( self, event ):
		event.Skip()


###########################################################################
## Class TabelDataPeserta
###########################################################################

class TabelDataPeserta ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tabel Data Peserta", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel23.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer21.AddGrowableCol( 4 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button22 = wx.Button( self.m_panel23, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button_buat_tabel_norma = wx.Button( self.m_panel23, wx.ID_ANY, u"Buat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_buat_tabel_norma, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self.m_panel23, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self.m_panel23, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button_tutup_norma = wx.Button( self.m_panel23, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_tutup_norma, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer34.Add( fgSizer21, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl3 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListCtrl3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		self.m_dataViewListColumn9 = self.m_dataViewListCtrl3.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 75, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn8 = self.m_dataViewListCtrl3.AppendTextColumn( u"ID Peserta", wx.dataview.DATAVIEW_CELL_INERT, 150, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn10 = self.m_dataViewListCtrl3.AppendTextColumn( u"Nama Peserta", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn36 = self.m_dataViewListCtrl3.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer34.Add( self.m_dataViewListCtrl3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer34 )
		self.m_panel23.Layout()
		bSizer34.Fit( self.m_panel23 )
		bSizer33.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.pilih_data_peserta )
		self.m_button_buat_tabel_norma.Bind( wx.EVT_BUTTON, self.buat_data_peserta )
		self.m_button24.Bind( wx.EVT_BUTTON, self.edit_data_peserta )
		self.m_button25.Bind( wx.EVT_BUTTON, self.hapus_data_peserta )
		self.m_button_tutup_norma.Bind( wx.EVT_BUTTON, self.tutup_data_peserta )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pilih_data_peserta( self, event ):
		event.Skip()

	def buat_data_peserta( self, event ):
		event.Skip()

	def edit_data_peserta( self, event ):
		event.Skip()

	def hapus_data_peserta( self, event ):
		event.Skip()

	def tutup_data_peserta( self, event ):
		event.Skip()


###########################################################################
## Class BuatNormaSendiri
###########################################################################

class BuatNormaSendiri ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText267 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Buat Norma Sendiri", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText267.Wrap( -1 )

		bSizer49.Add( self.m_staticText267, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel31 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer29.AddGrowableCol( 1 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText265 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Nama Norma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText265.Wrap( -1 )

		fgSizer29.Add( self.m_staticText265, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_nama_norma_sendiri = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer29.Add( self.m_nama_norma_sendiri, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText266 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText266.Wrap( -1 )

		fgSizer29.Add( self.m_staticText266, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_keterangan_norma_sendiri = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer29.Add( self.m_keterangan_norma_sendiri, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer51.Add( fgSizer29, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel31.SetSizer( bSizer51 )
		self.m_panel31.Layout()
		bSizer51.Fit( self.m_panel31 )
		bSizer49.Add( self.m_panel31, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_batal = wx.Button( self.m_panel30, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.button_batal, 0, wx.ALL, 5 )

		self.m_lanjut = wx.Button( self.m_panel30, wx.ID_ANY, u"Lanjut", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.m_lanjut, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer49.Add( bSizer50, 0, wx.ALIGN_RIGHT, 5 )


		self.m_panel30.SetSizer( bSizer49 )
		self.m_panel30.Layout()
		bSizer49.Fit( self.m_panel30 )
		bSizer48.Add( self.m_panel30, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer48 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_batal.Bind( wx.EVT_BUTTON, self.batal_norma_sendiri )
		self.m_lanjut.Bind( wx.EVT_BUTTON, self.lanjut_simpan_norma_sendiri )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def batal_norma_sendiri( self, event ):
		event.Skip()

	def lanjut_simpan_norma_sendiri( self, event ):
		event.Skip()


###########################################################################
## Class NormaAll
###########################################################################

class NormaAll ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_pilih_norma_all = wx.Button( self.m_panel23, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_pilih_norma_all, 0, wx.ALL, 5 )

		self.m_button_tutup_normaAll = wx.Button( self.m_panel23, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button_tutup_normaAll, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer34.Add( fgSizer21, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl3 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn9 = self.m_dataViewListCtrl3.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn37 = self.m_dataViewListCtrl3.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn8 = self.m_dataViewListCtrl3.AppendTextColumn( u"Nama Norma", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn10 = self.m_dataViewListCtrl3.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer34.Add( self.m_dataViewListCtrl3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer34 )
		self.m_panel23.Layout()
		bSizer34.Fit( self.m_panel23 )
		bSizer33.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_pilih_norma_all.Bind( wx.EVT_BUTTON, self.m_button_pilih_norma_allOnButtonClick )
		self.m_button_tutup_normaAll.Bind( wx.EVT_BUTTON, self.m_button_tutup_normaAllOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_pilih_norma_allOnButtonClick( self, event ):
		event.Skip()

	def m_button_tutup_normaAllOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class NormaSendiri
###########################################################################

class NormaSendiri ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Norma Sendiri", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_pilih_norma_sendiri_1 = wx.Button( self.m_panel23, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_pilih_norma_sendiri_1, 0, wx.ALL, 5 )

		self.m_tutup_norma_sendiri_1 = wx.Button( self.m_panel23, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_tutup_norma_sendiri_1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer34.Add( fgSizer21, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl30 = wx.dataview.DataViewListCtrl( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn56 = self.m_dataViewListCtrl30.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn31 = self.m_dataViewListCtrl30.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn32 = self.m_dataViewListCtrl30.AppendTextColumn( u"Nama Norma", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn33 = self.m_dataViewListCtrl30.AppendTextColumn( u"Keterangan", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn55 = self.m_dataViewListCtrl30.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN|wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer34.Add( self.m_dataViewListCtrl30, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer34 )
		self.m_panel23.Layout()
		bSizer34.Fit( self.m_panel23 )
		bSizer33.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_pilih_norma_sendiri_1.Bind( wx.EVT_BUTTON, self.m_button_pilih_norma_allOnButtonClick )
		self.m_tutup_norma_sendiri_1.Bind( wx.EVT_BUTTON, self.m_button_tutup_normaAllOnButtonClick )
		self.m_dataViewListCtrl30.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.m_data_aktif_tabel_norma_sendiri, id = wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_pilih_norma_allOnButtonClick( self, event ):
		event.Skip()

	def m_button_tutup_normaAllOnButtonClick( self, event ):
		event.Skip()

	def m_data_aktif_tabel_norma_sendiri( self, event ):
		event.Skip()


###########################################################################
## Class TabelNorma
###########################################################################

class TabelNorma ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_ok_tabel_norma = wx.Button( self.m_panel24, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_button_ok_tabel_norma, 0, wx.ALL, 5 )

		self.m_button_batal_tabel_norma = wx.Button( self.m_panel24, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_button_batal_tabel_norma, 0, wx.ALL, 5 )


		bSizer36.Add( fgSizer23, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.No = self.m_dataViewListCtrl4.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn12 = self.m_dataViewListCtrl4.AppendTextColumn( u"RS", wx.dataview.DATAVIEW_CELL_EDITABLE, 75, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn13 = self.m_dataViewListCtrl4.AppendTextColumn( u"SE", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn14 = self.m_dataViewListCtrl4.AppendTextColumn( u"WA", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn15 = self.m_dataViewListCtrl4.AppendTextColumn( u"AN", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn16 = self.m_dataViewListCtrl4.AppendTextColumn( u"GE", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn21 = self.m_dataViewListCtrl4.AppendTextColumn( u"ME", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn17 = self.m_dataViewListCtrl4.AppendTextColumn( u"RA", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn18 = self.m_dataViewListCtrl4.AppendTextColumn( u"ZR", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn19 = self.m_dataViewListCtrl4.AppendTextColumn( u"FA", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn20 = self.m_dataViewListCtrl4.AppendTextColumn( u"WU", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer36.Add( self.m_dataViewListCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel24.SetSizer( bSizer36 )
		self.m_panel24.Layout()
		bSizer36.Fit( self.m_panel24 )
		bSizer35.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_ok_tabel_norma.Bind( wx.EVT_BUTTON, self.m_button_ok_tabel_normaOnButtonClick )
		self.m_button_batal_tabel_norma.Bind( wx.EVT_BUTTON, self.m_button_batal_tabel_normaOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_ok_tabel_normaOnButtonClick( self, event ):
		event.Skip()

	def m_button_batal_tabel_normaOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class TabelNormaLihat
###########################################################################

class TabelNormaLihat ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_ok_tabel_norma = wx.Button( self.m_panel24, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer23.Add( self.m_button_ok_tabel_norma, 0, wx.ALL, 5 )


		bSizer36.Add( fgSizer23, 0, wx.EXPAND, 5 )

		self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.No = self.m_dataViewListCtrl4.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn12 = self.m_dataViewListCtrl4.AppendTextColumn( u"RS", wx.dataview.DATAVIEW_CELL_INERT, 75, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn13 = self.m_dataViewListCtrl4.AppendTextColumn( u"SE", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn14 = self.m_dataViewListCtrl4.AppendTextColumn( u"WA", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn15 = self.m_dataViewListCtrl4.AppendTextColumn( u"AN", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn16 = self.m_dataViewListCtrl4.AppendTextColumn( u"GE", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn17 = self.m_dataViewListCtrl4.AppendTextColumn( u"RA", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn18 = self.m_dataViewListCtrl4.AppendTextColumn( u"ZR", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn19 = self.m_dataViewListCtrl4.AppendTextColumn( u"FA", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn20 = self.m_dataViewListCtrl4.AppendTextColumn( u"WU", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn21 = self.m_dataViewListCtrl4.AppendTextColumn( u"ME", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer36.Add( self.m_dataViewListCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel24.SetSizer( bSizer36 )
		self.m_panel24.Layout()
		bSizer36.Fit( self.m_panel24 )
		bSizer35.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_ok_tabel_norma.Bind( wx.EVT_BUTTON, self.m_button_ok_tabel_norma_all )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_ok_tabel_norma_all( self, event ):
		event.Skip()


###########################################################################
## Class FrameRow
###########################################################################

class FrameRow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText260 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Jumlah Baris Maksimal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText260.Wrap( -1 )

		fgSizer22.Add( self.m_staticText260, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl11 = wx.SpinCtrl( self.m_panel25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer22.Add( self.m_spinCtrl11, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_batal_baris = wx.Button( self.m_panel25, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button_batal_baris, 0, wx.ALL, 5 )

		self.m_button_ok_baris = wx.Button( self.m_panel25, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button_ok_baris, 0, wx.ALL, 5 )


		fgSizer22.Add( bSizer39, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer22, 1, wx.EXPAND, 5 )


		self.m_panel25.SetSizer( bSizer38 )
		self.m_panel25.Layout()
		bSizer38.Fit( self.m_panel25 )
		bSizer37.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer37 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_batal_baris.Bind( wx.EVT_BUTTON, self.m_button_batal_barisOnButtonClick )
		self.m_button_ok_baris.Bind( wx.EVT_BUTTON, self.m_button_ok_barisOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_batal_barisOnButtonClick( self, event ):
		event.Skip()

	def m_button_ok_barisOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Biodata
###########################################################################

class Biodata ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel34.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText268 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Biodata Peserta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText268.Wrap( -1 )

		bSizer52.Add( self.m_staticText268, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel34.SetSizer( bSizer52 )
		self.m_panel34.Layout()
		bSizer52.Fit( self.m_panel34 )
		bSizer29.Add( self.m_panel34, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.Hide()

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledpanel_pendidikan = wx.ScrolledWindow( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledpanel_pendidikan.SetScrollRate( 5, 5 )
		fgSizer2 = wx.FlexGridSizer( 14, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText_nama = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_nama.Wrap( -1 )

		fgSizer2.Add( self.m_staticText_nama, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_nama = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Ketik Nama Anda", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl_nama, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2263 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2263.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2263, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_tanggal_tes = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl_tanggal_tes, 0, wx.ALL, 5 )

		self.m_staticTextUsia = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsia.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextUsia, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_usia = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer15.Add( self.m_textCtrl_usia, 0, wx.ALL, 5 )

		self.m_staticText218 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Thn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		bSizer15.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_staticTextKelas = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextKelas.Wrap( -1 )

		fgSizer2.Add( self.m_staticTextKelas, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jenis_kelamin = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl_jenis_kelamin, 0, wx.ALL, 5 )

		self.m_staticText2321 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2321.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2321, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_tanggal_lahir = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl_tanggal_lahir, 0, wx.ALL, 5 )

		self.m_staticText2272 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Asal sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2272.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2272, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_asal_sekolah = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_asal_sekolah, 0, wx.ALL, 5 )

		self.m_staticText2282 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2282.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2282, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jurusan_sekolah = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_jurusan_sekolah, 0, wx.ALL, 5 )

		self.m_staticText2291 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2291.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2291, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_asal_universitas = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_asal_universitas, 0, wx.ALL, 5 )

		self.m_staticText2301 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2301.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2301, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jurusan_universitas = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_jurusan_universitas, 0, wx.ALL, 5 )

		self.m_staticText2311 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2311.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2311, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_kota = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_kota, 0, wx.ALL, 5 )

		self.m_staticText2331 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2331.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2331, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_hobi = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl_hobi, 0, wx.ALL, 5 )

		self.m_staticText2341 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2341.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2341, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_prestasi_akademik = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.m_textCtrl_prestasi_akademik, 0, wx.ALL, 5 )

		self.m_staticText2351 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2351.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2351, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_prestasi_non_akademik = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.m_textCtrl_prestasi_non_akademik, 0, wx.ALL, 5 )

		self.m_staticText2361 = wx.StaticText( self.m_scrolledpanel_pendidikan, wx.ID_ANY, u"Ekskul Yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2361.Wrap( -1 )

		fgSizer2.Add( self.m_staticText2361, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_ekskul_yang_diikuti = wx.TextCtrl( self.m_scrolledpanel_pendidikan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), wx.TE_MULTILINE )
		fgSizer2.Add( self.m_textCtrl_ekskul_yang_diikuti, 0, wx.ALL, 5 )


		self.m_scrolledpanel_pendidikan.SetSizer( fgSizer2 )
		self.m_scrolledpanel_pendidikan.Layout()
		fgSizer2.Fit( self.m_scrolledpanel_pendidikan )
		bSizer25.Add( self.m_scrolledpanel_pendidikan, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel16.SetSizer( bSizer25 )
		self.m_panel16.Layout()
		bSizer25.Fit( self.m_panel16 )
		bSizer27.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel17 = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel17.Hide()

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledpanel_pekerjaan = wx.ScrolledWindow( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledpanel_pekerjaan.SetScrollRate( 5, 5 )
		fgSizer20 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2271 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2271.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2271, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_no_tes = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_no_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2352 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2352.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2352, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_tanggal_tes2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_tanggal_tes2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2262 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2262.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2262, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_nama2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_nama2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2281 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2281.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2281, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_jenis_kelamin2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_jenis_kelamin2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_Tanggal_Lahir = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Tanggal_Lahir.Wrap( -1 )

		fgSizer20.Add( self.m_staticText_Tanggal_Lahir, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_tanggal_lahir2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_tanggal_lahir2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2171 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2171.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2171, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_pendidikan_terakhir = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl_pendidikan_terakhir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2222 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2222.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2222, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jurusan_pendidikan2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl_jurusan_pendidikan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2232 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2232.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2232, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_kota2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl_kota2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2242 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Perusahaan / Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2242.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2242, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_perusahaan_instansi2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl_perusahaan_instansi2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText2252 = wx.StaticText( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2252.Wrap( -1 )

		fgSizer20.Add( self.m_staticText2252, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_posisi_jabatan2 = wx.TextCtrl( self.m_scrolledpanel_pekerjaan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl_posisi_jabatan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_scrolledpanel_pekerjaan.SetSizer( fgSizer20 )
		self.m_scrolledpanel_pekerjaan.Layout()
		fgSizer20.Fit( self.m_scrolledpanel_pekerjaan )
		bSizer26.Add( self.m_scrolledpanel_pekerjaan, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel17.SetSizer( bSizer26 )
		self.m_panel17.Layout()
		bSizer26.Fit( self.m_panel17 )
		bSizer27.Add( self.m_panel17, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel_data = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledpanel_pendidikan1 = wx.ScrolledWindow( self.m_panel_data, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledpanel_pendidikan1.SetScrollRate( 5, 5 )
		self.m_scrolledpanel_pendidikan1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer21 = wx.FlexGridSizer( 14, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.AddGrowableRow( 0 )
		fgSizer21.AddGrowableRow( 1 )
		fgSizer21.AddGrowableRow( 2 )
		fgSizer21.AddGrowableRow( 3 )
		fgSizer21.AddGrowableRow( 4 )
		fgSizer21.AddGrowableRow( 5 )
		fgSizer21.AddGrowableRow( 6 )
		fgSizer21.AddGrowableRow( 7 )
		fgSizer21.AddGrowableRow( 8 )
		fgSizer21.AddGrowableRow( 9 )
		fgSizer21.AddGrowableRow( 10 )
		fgSizer21.AddGrowableRow( 11 )
		fgSizer21.AddGrowableRow( 12 )
		fgSizer21.AddGrowableRow( 13 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText292 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText292.Wrap( -1 )

		self.m_staticText292.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer21.Add( self.m_staticText292, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_no_tes1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl_no_tes1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText22631 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22631.Wrap( -1 )

		self.m_staticText22631.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer21.Add( self.m_staticText22631, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer33 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl_tanggal_tes1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer33.Add( self.m_textCtrl_tanggal_tes1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes = wx.adv.DatePickerCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer33.Add( self.tanggal_tes, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer33, 1, wx.EXPAND, 5 )

		self.m_staticText_nama1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_nama1.Wrap( -1 )

		self.m_staticText_nama1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer21.Add( self.m_staticText_nama1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl_nama1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_textCtrl_nama1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticTextKelas1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextKelas1.Wrap( -1 )

		self.m_staticTextKelas1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer21.Add( self.m_staticTextKelas1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer35 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl_jenis_kelamin1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_textCtrl_jenis_kelamin1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelaminChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin = wx.Choice( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelaminChoices, 0 )
		self.jenis_kelamin.SetSelection( 0 )
		fgSizer35.Add( self.jenis_kelamin, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer35, 1, wx.EXPAND, 5 )

		self.m_staticText23211 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23211.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23211, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer34 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl_tanggal_lahir1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer34.Add( self.m_textCtrl_tanggal_lahir1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir = wx.adv.DatePickerCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer34.Add( self.tanggal_lahir, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer34, 1, wx.EXPAND, 5 )

		self.m_staticTextUsia1 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsia1.Wrap( -1 )

		fgSizer21.Add( self.m_staticTextUsia1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl_usia1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_textCtrl_usia1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		usiaChoices = [ u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", wx.EmptyString, wx.EmptyString, wx.EmptyString ]
		self.usia = wx.Choice( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, usiaChoices, 0 )
		self.usia.SetSelection( 0 )
		fgSizer36.Add( self.usia, 0, wx.ALL, 5 )


		bSizer151.Add( fgSizer36, 0, 0, 5 )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2181 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Thn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2181.Wrap( -1 )

		bSizer48.Add( self.m_staticText2181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer151.Add( bSizer48, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer21.Add( bSizer151, 1, wx.EXPAND, 5 )

		self.m_staticText22721 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Asal Sekolah/Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22721.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22721, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_asal_sekolah_universitas = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_asal_sekolah_universitas, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText22911 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22911.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22911, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer37 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl_pendidikan_terakhir1 = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_textCtrl_pendidikan_terakhir1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Tpendidikan_terakhirChoices = []
		self.Tpendidikan_terakhir = wx.Choice( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Tpendidikan_terakhirChoices, 0 )
		self.Tpendidikan_terakhir.SetSelection( 0 )
		fgSizer37.Add( self.Tpendidikan_terakhir, 0, wx.ALL, 5 )


		fgSizer21.Add( fgSizer37, 1, wx.EXPAND, 5 )

		self.m_staticText22821 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22821.Wrap( -1 )

		fgSizer21.Add( self.m_staticText22821, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_jurusan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_jurusan, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText23011 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Posisi Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23011.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23011, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_posisi_pekerjaan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_posisi_pekerjaan, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText23111 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Perusahaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23111.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23111, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_perusahaan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl_perusahaan, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText23311 = wx.StaticText( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23311.Wrap( -1 )

		fgSizer21.Add( self.m_staticText23311, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_keterangan = wx.TextCtrl( self.m_scrolledpanel_pendidikan1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), wx.TE_MULTILINE )
		fgSizer21.Add( self.m_textCtrl_keterangan, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_scrolledpanel_pendidikan1.SetSizer( fgSizer21 )
		self.m_scrolledpanel_pendidikan1.Layout()
		fgSizer21.Fit( self.m_scrolledpanel_pendidikan1 )
		bSizer251.Add( self.m_scrolledpanel_pendidikan1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_data.SetSizer( bSizer251 )
		self.m_panel_data.Layout()
		bSizer251.Fit( self.m_panel_data )
		bSizer27.Add( self.m_panel_data, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel19.SetSizer( bSizer27 )
		self.m_panel19.Layout()
		bSizer27.Fit( self.m_panel19 )
		bSizer29.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel32 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer30 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_lanjut = wx.Button( self.m_panel32, wx.ID_ANY, u"Lanjut", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer30.Add( self.m_lanjut, 0, wx.ALL, 5 )

		self.Tutup = wx.Button( self.m_panel32, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer30.Add( self.Tutup, 0, wx.ALL, 5 )


		self.m_panel32.SetSizer( fgSizer30 )
		self.m_panel32.Layout()
		fgSizer30.Fit( self.m_panel32 )
		bSizer29.Add( self.m_panel32, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl_nama.Bind( wx.EVT_LEFT_UP, self.m_textCtrl_namaOnLeftUp )
		self.m_textCtrl_no_tes1.Bind( wx.EVT_TEXT, self.requiredtext )
		self.m_textCtrl_nama1.Bind( wx.EVT_LEFT_UP, self.m_textCtrl_namaOnLeftUp )
		self.m_lanjut.Bind( wx.EVT_BUTTON, self.m_lanjut_biodataOnClick )
		self.Tutup.Bind( wx.EVT_BUTTON, self.m_tutup_biodata )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_textCtrl_namaOnLeftUp( self, event ):
		event.Skip()

	def requiredtext( self, event ):
		event.Skip()


	def m_lanjut_biodataOnClick( self, event ):
		event.Skip()

	def m_tutup_biodata( self, event ):
		event.Skip()


###########################################################################
## Class TipeNorma
###########################################################################

class TipeNorma ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel40 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		fgSizer35 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer35.AddGrowableCol( 1 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText308 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Tipe Norma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText308.Wrap( -1 )

		fgSizer35.Add( self.m_staticText308, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer35.Add( self.m_choice3, 0, wx.ALL, 5 )

		self.m_staticText309 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Jenis Norma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText309.Wrap( -1 )

		fgSizer35.Add( self.m_staticText309, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		fgSizer35.Add( self.m_choice4, 0, wx.ALL, 5 )

		self.m_staticText310 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Nama Norma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText310.Wrap( -1 )

		fgSizer35.Add( self.m_staticText310, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = []
		self.m_choice5 = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		fgSizer35.Add( self.m_choice5, 0, wx.ALL, 5 )


		bSizer64.Add( fgSizer35, 1, wx.EXPAND, 5 )

		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_batal_tipe_norma = wx.Button( self.m_panel40, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_batal_tipe_norma, 0, wx.ALL, 5 )

		self.m_simpan_tipe_norma = wx.Button( self.m_panel40, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_simpan_tipe_norma, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer64.Add( fgSizer36, 0, wx.ALIGN_RIGHT, 5 )


		self.m_panel40.SetSizer( bSizer64 )
		self.m_panel40.Layout()
		bSizer64.Fit( self.m_panel40 )
		bSizer62.Add( self.m_panel40, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer62 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice3.Bind( wx.EVT_CHOICE, self.m_tipe_norma_event )
		self.m_choice4.Bind( wx.EVT_CHOICE, self.m_jenisnorma_event )
		self.m_batal_tipe_norma.Bind( wx.EVT_BUTTON, self.m_batal_tipe_normaOnButtonClick )
		self.m_simpan_tipe_norma.Bind( wx.EVT_BUTTON, self.m_simpan_tipe_normaOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_tipe_norma_event( self, event ):
		event.Skip()

	def m_jenisnorma_event( self, event ):
		event.Skip()

	def m_batal_tipe_normaOnButtonClick( self, event ):
		event.Skip()

	def m_simpan_tipe_normaOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class PilihInput
###########################################################################

class PilihInput ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText272 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText272.Wrap( -1 )

		bSizer56.Add( self.m_staticText272, 0, wx.ALL, 5 )

		self.Bpilih_input_manual = wx.Button( self, wx.ID_ANY, u"Input Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.Bpilih_input_manual, 0, wx.ALL, 5 )

		self.Bpilih_input_total = wx.Button( self, wx.ID_ANY, u"Input Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.Bpilih_input_total, 0, wx.ALL, 5 )


		self.SetSizer( bSizer56 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bpilih_input_manual.Bind( wx.EVT_BUTTON, self.pilih_input_manual )
		self.Bpilih_input_total.Bind( wx.EVT_BUTTON, self.pilih_input_total )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pilih_input_manual( self, event ):
		event.Skip()

	def pilih_input_total( self, event ):
		event.Skip()


###########################################################################
## Class GridViewInputManual
###########################################################################

class GridViewInputManual ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Manual", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel41 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 20, 18 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 30 )
		self.m_grid2.SetColSize( 1, 80 )
		self.m_grid2.SetColSize( 2, 30 )
		self.m_grid2.SetColSize( 3, 80 )
		self.m_grid2.SetColSize( 4, 30 )
		self.m_grid2.SetColSize( 5, 80 )
		self.m_grid2.SetColSize( 6, 30 )
		self.m_grid2.SetColSize( 7, 80 )
		self.m_grid2.SetColSize( 8, 30 )
		self.m_grid2.SetColSize( 9, 80 )
		self.m_grid2.SetColSize( 10, 30 )
		self.m_grid2.SetColSize( 11, 80 )
		self.m_grid2.SetColSize( 12, 30 )
		self.m_grid2.SetColSize( 13, 80 )
		self.m_grid2.SetColSize( 14, 30 )
		self.m_grid2.SetColSize( 15, 80 )
		self.m_grid2.SetColSize( 16, 30 )
		self.m_grid2.SetColSize( 17, 80 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( False )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( False )
		self.m_grid2.SetRowLabelSize( 1 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.m_grid2.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		# Cell Defaults
		self.m_grid2.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.m_grid2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer64.Add( self.m_grid2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.gridOk = wx.Button( self.m_panel41, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer64.Add( self.gridOk, 0, wx.ALL, 5 )


		self.m_panel41.SetSizer( bSizer64 )
		self.m_panel41.Layout()
		bSizer64.Fit( self.m_panel41 )
		bSizer63.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer63 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.gridOk.Bind( wx.EVT_BUTTON, self.gridOkOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def gridOkOnButtonClick( self, event ):
		event.Skip()


