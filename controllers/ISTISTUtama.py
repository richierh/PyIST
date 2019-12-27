"""Subclass of ISTUtama, which is generated by wxFormBuilder."""
import wx
from controllers.properties_ist import ISTInheritedProperties ,PropertiesInput
from controllers.properties_tampilan import PropertiesTampilan, AddTextCtrlProperties
# Implementing ISTUtama


class ISTISTUtama(ISTInheritedProperties):

	def __init__(self, parent , *args, **kwds):
		super().__init__(parent, *args, **kwds)
		self.m_simplebook1.SetSelection(0)
		self.properties_tamp = PropertiesTampilan(self)
		self.properties_tamp.logo_show()
		self.properties_tamp.tabel_show()
		self.data_peserta = PropertiesInput(self)
		# print (self.properties_listcontrol.list_an)
		# for listtext in self.properties_listcontrol.list_an :
		# 	print (listtext.SetValue("A"))

		self.Maximize()
		pass
	
	# def m_button_hapus_onclick( self, event ):
	# 	print ("hapus dari database")
	# 	event.Skip()

	# def m_button_filter_onclick( self, event ):
	# 	print ("you have click 'Filter'")
	# 	self.openfilter = BukaFilter(self)
	# 	self.openfilter.Show()
	# 	event.Skip()

	# def m_button_lihat_dari_database_onclick( self, event ):
	# 	print ("lihat dari database")
	# 	event.Skip()

	# def m_button_reset_onclick( self, event ):
	# 	print ("reset dari halaman terakhir")
	# 	event.Skip()
	
	def m_buttonInput_JawabanOnButtonClick(self, event):
		self.m_notebook1.SetSelection(1)
		print ("Input Jawaban is over here")
	
		# 	def m_buttonInput_TotalOnButtonClick(self, event):
		# 		self.m_notebook1.SetSelection(2)
		# 		print ("Input Total is over here")
		
	def m_textCtrl47OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolse()
		
		pass
	
	def m_textCtrl6OnText(self, event):
		print ("respon on 'input jawaban'")

		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolsetotal()
		self.se = ListControlProperties(self)
		print (self.se.totalse())
		pass
	
	def m_textCtrl48OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolwa()
		pass
	
	def m_textCtrl7OnText(self, event):
		print ("respon on 'input jawaban'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolwatotal()
		pass
	
	def m_textCtrl481OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolan()
		pass
	
	def m_textCtrl71OnText(self, event):
		print ("respon on 'input jawaban'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolantotal()
		pass

	def m_textCtrl181OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolra()
		pass
	
	def m_textCtrl30OnText(self, event):
		print ("respon on 'input jawaban'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolratotal()
		pass

	def m_textCtrl196OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolzr()
		pass
	
	def m_textCtrl10OnText(self, event):
		print ("respon on 'input jawaban'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolzrtotal()
		pass

	def m_textCtrl484OnText(self, event):
		print ("respon on 'input total'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolfa()
		pass
	
	def m_textCtrl74OnText(self, event):
		print ("respon on 'input jawaban'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolfatotal()
		pass

	def m_textCtrl75OnText(self, event):
		print ("respon on 'input jawaban'")

		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolwutotal()
		pass
	
	def m_textCtrl485OnText(self, event):
		print ("respon on 'input jawaban a'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolwu()
		pass

	def m_textCtrl76OnText(self, event):
		print ("respon on 'input jawaban'")

		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolmetotal()
		pass
	
	def m_textCtrl486OnText(self, event):
		print ("respon on 'input jawaban a'")
		self.control = AddTextCtrlProperties(self)
		self.control.enabledisablecontrolme()
		pass
	
	def m_button6OnButtonClick(self, event):
		# Klik for calculating \
		print ("over here")
		self.run_calculate = ListControlProperties(self)
		
		pass
	
	def m_textCtrl_namaOnLeftUp(self, event):

		if self.m_textCtrl_nama.GetValue() == "Ketik Nama Anda":
			# event.SetString("")
			self.m_textCtrl_nama.SetValue("")
			print ("lewat sini")
		
		else :

			pass
		print ("okay")
		pass

