#! usr/bin/env python


import wx
from views.istcore import ISTUtama

'''
Created on May 12, 2019

@author: cireng
'''

class HalamanEventControl(ISTUtama):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.m_sebelumnya.Disable()
        self.m_kembali_ke_awal.Disable()

 
    def m_kembali_ke_awalOnButtonClick(self,event):
        print("klik kembali ke awal")
        self.m_simplebook1.SetSelection(0)
        self.m_sebelumnya.Disable()
        self.m_selanjutnya.Enable()
        self.m_kembali_ke_awal.Disable()
    

    def m_sebelumnyaOnButtonClick(self,event):
        print("klik sebelumnya")
        self.getSel = self.m_simplebook1.GetSelection()
        self.m_simplebook1.SetSelection(self.getSel - 1)
        self.getSel = self.m_simplebook1.GetSelection()
        print (self.getSel)

        if self.getSel == 0:
            self.m_selanjutnya.Enable()        
            self.m_sebelumnya.Disable()
            self.m_kembali_ke_awal.Disable()
            pass

        elif self.getSel == 1:
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            self.m_kembali_ke_awal.Enable()
            pass
   
        
        elif self.getSel == 3 :
            'Proses hitung dimulai ketika halaman 3 , atau pada saat penyajian grafik'
            pass
        elif self.getSel == 4 :
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            pass
        else :
            # self.m_button3.Enable()
            pass


    def m_selanjutnyaOnButtonClick(self,event):
        print("klik Selanjutnya")
        print ("work nggak")

        self.getSel = self.m_simplebook1.GetSelection()
        self.m_simplebook1.SetSelection(self.getSel + 1)
        self.getSel = self.m_simplebook1.GetSelection()
        if self.getSel == 1:
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            pass
        elif self.getSel == 3 :
            'Proses hitung dimulai ketika halaman 3 , atau pada saat penyajian grafik'
            pass
        elif self.getSel == 4 :
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            pass
        else :
            # self.m_button3.Enable()
            pass

    def m_input_manualOnButtonClick(self,event):
        self.m_panel_input.Show()
        self.m_panel_input_total.Hide()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()     
        self.m_kembali_ke_awal.Enable()
   


        pass
    
    def m_input_totalOnButtonClick(self,event):
        self.m_panel_input.Hide()
        self.m_panel_input_total.Show()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()        
        self.m_kembali_ke_awal.Enable()




        pass