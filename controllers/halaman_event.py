#! usr/bin/env python


import wx
from views.istcore import ISTUtama
from models.query import SqliteDB
from pathlib import Path
import wx.dataview
from views.dataview import PanggilDataView,PanggilGrid
from controllers.ist_calculation import KalkulasiNilai


'''
Created on May 12, 2019

@author: cireng
'''


class DataView(ISTUtama):


    def __init__(self,parent):
        super().__init__(parent)
        # self.panggildataview = PanggilDataView(self)
        self.panggilgrid = PanggilGrid(self)
        # bsizerdataview = wx.BoxSizer(wx.VERTICAL)
        self.m_panel3.Layout()
        self.m_panel_input.Layout()

        # self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # bsizerdataview.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


    def m_button14OnButtonClick(self,event):
        # self.panggilgrid.getdata()
        print ("okay")
        print (self.panggilgrid.getdata())

        pass

class CekDB(DataView):

    def __init__(self,parent):
        super().__init__(parent)

        self.nama_file = "ist"
        self.connect_db = SqliteDB("ist")
        # print(self.connect_db.query_tabel_data_kelompok())
        

     

class HalamanEventControl(CekDB):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.m_sebelumnya.Disable()
        self.m_kembali_ke_awal.Disable()
        print (self.m_radioBox_biodata.GetSelection())
        self.tipe_biodata = 1

        pass

    def m_radiobox_biodata_on_click(self,event):
        if self.m_radioBox_biodata.GetSelection() == 0 :
            print ("Tipe Pendidikan")
            self.tipe_biodata =1
            self.m_panel16.Show()
            self.m_panel17.Hide()

        elif self.m_radioBox_biodata.GetSelection() == 1 :
            print ("Tipe Pekerjaan")
            self.tipe_biodata = 2
            self.m_panel17.Show()
            self.m_panel16.Hide()

        else :
            print ("Ada kesalahan di opsi tipe biodata")
        self.m_panel16.Layout()
        self.m_panel17.Layout()
        self.m_panel15.Layout()
        event.Skip()


    def m_kembali_ke_awalOnButtonClick(self,event):
        print("klik kembali ke awal")
        self.m_simplebook1.SetSelection(0)
        self.m_sebelumnya.Disable()
        self.m_selanjutnya.Enable()
        self.m_kembali_ke_awal.Disable()
        pass
        

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
            print ("hello")
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
            print("hello")

            # Menentukan input dari peserta , jika nilai self.select_input satu maka input dilakukan persoal
            # namun jika nilainya 2 maka input yang dimasukkan adalah total
            if self.select_input == 1 :
                print ("pilih satu")
                self.panggilgrid.getdata()
                KalkulasiNilai(self)


            elif self.select_input == 2 :
                print ("pilih 2")

            pass
        elif self.getSel == 4 :
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            pass
        else :
            # self.m_button3.Enable()
            pass

    def m_input_manualOnButtonClick(self,event):
        self.select_input = 1
        print (self.get_biodata())
        self.m_panel_input.Show()
        self.m_panel_input_total.Hide()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()     
        self.m_kembali_ke_awal.Enable()
        self.m_panel3.Layout()
        self.m_panel_input.Layout()
        pass
    
    def m_input_totalOnButtonClick(self,event):
        self.select_input = 2
        print (self.get_biodata())
        self.m_panel_input.Hide()
        self.m_panel_input_total.Show()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()        
        self.m_kembali_ke_awal.Enable()
        pass