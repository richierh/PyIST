#! usr/bin/env python

import pathlib
import os
import wx
import wx.dataview

from views.istcore import ISTUtama
from models.query import SqliteDB
from pathlib import Path
from views.dataview import RWSWScore, PanggilDataView,PanggilGrid,PanggilInputTotal
from controllers.ist_calculation import KalkulasiNilai
from views.grafik_ist import GrafikLayout,GrafikHasil
from controllers.biodata import Biodata
from controllers.database_control import DataKonversiGE,DatabaseConnect,TableDataKelompokUmurConnect


'''
Created on May 12, 2019

@author: cireng
'''

class DataView(ISTUtama):


    def __init__(self,parent):
        super().__init__(parent)
        # self.panggildataview = PanggilDataView(self)
        self.panggilgrid = PanggilGrid(self)
        self.panggil_nilai_total = PanggilInputTotal(self)
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
        # print (self.connect_db.path_db)
        # print(self.connect_db.query_tabel_data_kelompok())

class HalamanEventControl(CekDB):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.m_sebelumnya.Disable()
        self.m_kembali_ke_awal.Disable()
        print (f"Setting Tipe Biodata atau Radio Button ke {self.m_radioBox_biodata.SetSelection(0)}")
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
        # print("klik kembali ke awal")
        self.m_simplebook1.SetSelection(0)
        self.m_sebelumnya.Disable()
        self.m_selanjutnya.Enable()
        self.m_kembali_ke_awal.Disable()
        pass
        

    def m_sebelumnyaOnButtonClick(self,event):
        # print("klik sebelumnya")
        self.getSel = self.m_simplebook1.GetSelection()
        self.m_simplebook1.SetSelection(self.getSel - 1)
        self.getSel = self.m_simplebook1.GetSelection()
        # print (self.getSel)

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
            print ("di halaman 3 penyajian grafik")
            self.grafik = GrafikLayout(self)
            self.grafik.draw()
            pass

        elif self.getSel == 4 :
            print ('hell0kl;k')
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            self.grafik_hasil = GrafikHasil(self)
            self.grafik_hasil.draw()
            pass

        else :
            # self.m_button3.Enable()
            pass

    def m_selanjutnyaOnButtonClick(self,event):
        # print("klik Selanjutnya")

        self.getSel = self.m_simplebook1.GetSelection()
        self.m_simplebook1.SetSelection(self.getSel + 1)
        self.getSel = self.m_simplebook1.GetSelection()

        if self.getSel == 1:
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            pass

        elif self.getSel == 3 :
            'Proses hitung dimulai ketika halaman 3 , atau pada saat penyajian grafik'
            print("penyajian grafik proses hitung")

            if self.select_input == 1 :
                self.input_peserta = self.panggilgrid.getdata()
                self.ge = self.input_peserta[3][0]

            elif self.select_input == 2 :
                self.input_peserta = self.panggil_nilai_total.getdata()
                self.ge = self.input_peserta[3]

            else:
                error_text == "select input tidak terdefinisikan"
                return error_text

            # class untuk menghitung Nilai
            self.nilai = KalkulasiNilai(self)
            self.databasekon = DatabaseConnect(self.nama_file)

            # konversi nilai GE
            self.con_datakonversi_ge = DataKonversiGE(self.databasekon)
            self.nilai_ge = self.con_datakonversi_ge.konversi_ge(self.ge)
            self.nilai_ge = self.nilai_ge[3]
            print (f"ini nilai {self.nilai_ge}")
            self.kelompok_usia = self.m_spinCtrl_usia.GetValue()


            self.hasil_sw = TableDataKelompokUmurConnect(self.databasekon)
            self.hasil_sw.query_sw()



            self.grafik = GrafikLayout(self)
            self.grafik.draw()

            # print (self.nilai_ge[3])


            self.hasil_hal3 = RWSWScore(self)

            pass

        elif self.getSel == 4 :
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            global bsizer12
            self.properties_tamp.tabel_show()
            self.grafik_hasil = GrafikHasil(self)
            self.grafik_hasil.draw()
            
            self.m_dataViewListCtrl1.InsertItem(0,["df","dfs","sdf"])
            # self.m_staticText_berpikir.SetValue()
            pass

        elif self.getSel == 5 :
            
            
            pass

        else :
            # self.m_button3.Enable()
            print ("masuk halaman 5")
            pass

    def m_input_manualOnButtonClick(self,event):
        self.select_input = 1
        # print (self.get_biodata())
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
        # print (self.get_biodata())
        self.m_panel_input.Hide()
        self.m_panel_input_total.Show()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()        
        self.m_kembali_ke_awal.Enable()
        pass

    
    def m_button_rincian_biodata_on_buttonclick(self,event):
        self.tampilkan_rincian_biodata = Biodata(self)
        self.tampilkan_rincian_biodata.Show()
        print ("lihat rincian biodata")

        pass