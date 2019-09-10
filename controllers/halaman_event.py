#! usr/bin/env python
from numpy import arange, sin, pi

from statistics import mean
import pathlib
import os
import wx
import wx.dataview

from views.istcore import ISTUtama,Norma,TabelNorma,FrameRow
from models.query import SqliteDB
from pathlib import Path
from views.dataview import RWSWScore, PanggilDataView,PanggilGrid,PanggilInputTotal
from controllers.ist_calculation import KalkulasiNilai
from views.grafik_ist import GrafikLayout,GrafikHasil,GrafikProfesi
from controllers.biodata import Biodata
from controllers.database_control import DataKonversiGE,DatabaseConnect,TableDataKelompokUmurConnect\
,DataBaseInput


'''
Created on May 12, 2019

@author: cireng
'''
class GrafikLayoutInherited(GrafikLayout):

    def __init__(self,parent):
        super().__init__(parent)

    def save_figure(self):
        import pathlib
        self.pathpar=pathlib.Path(__file__).parent
        # print (f"path{self.pathpar}")
        self.path = pathlib.Path(self.pathpar/"reporting"/"image1.png")
        print(self.path)
        print ("lewat sini nggak")
        return self.figure.savefig(self.path,dpi='figure')


class GrafikHasilLayoutInherited(GrafikHasil):

    def __init__(self,parent):
        super().__init__(parent)


    def draw(self,nilai_grafik = None):

        self.grafik = nilai_grafik
        print (self.grafik)
        # print (t)
        y = ["Kemampuan\nberhitung","Daya ingat\ndan konsentrasi","Kreatifitas",
            "Ketelitian","Judgement", "Daya\nanalisis", "Pengembalian\nkeputusan","Kemampuan\n Berbahasa" ]
        self.y = arange(len(y))
        nilai = []
        for value in self.grafik.values():
            print (value)
            nilai.append(int(value))
        print (nilai)
        # x = [130,136,79,125,128,146,128]
        x = nilai
        self.rects = self.axes.barh(y,x,color='green')
        # self.axes.invert_yaxis()
        self.axes.set_xlim(left=50,right=150)
        self.axes.set_yticks(self.y)
        self.axes.set_title("PROFIL KEUNGGULAN IST")
        self.autolabel()

    def save_figure(self):
        import pathlib
        self.pathpar=pathlib.Path(__file__).parent
        self.path = pathlib.Path(self.pathpar/"reporting"/"image2.png")
        print(self.path)
        print ("lewat sini nggak")
        return self.figure.savefig(self.path,dpi='figure')

class FrameRowInherited(FrameRow):

    def __init__(self,parent):
        super().__init__(parent)
    

    def m_button_ok_barisOnButtonClick(self,event):
        self.buka_tabel_norma = TabelNorma(self)
        self.buka_tabel_norma.Show()     
        self.Hide()
        pass

    def m_button_batal_barisOnButtonClick(self,event):
        self.Close()

        pass

class NormaInherited(Norma):

    def __init__(self,parent):
        super().__init__(parent)
        self.m_button_buat_tabel_norma.Bind( wx.EVT_BUTTON, self.m_button_buat_tabel_normaOnButtonClick )

    def m_button_buat_tabel_normaOnButtonClick(self,event):
        self.buka_row = FrameRowInherited(self)
        self.buka_row.Show()
        # self.buka_tabel_norma = TabelNorma(self)
        # self.buka_tabel_norma.Show()
        pass


class TabelNormaInherited(TabelNorma):


    def __init__(self,parent):
        super().__init__(parent)

    
    

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
            self.grafik = (self)
            self.grafik.draw(self.input_peserta_rw_sw)
            pass

        elif self.getSel == 4 :
            print ('hell0kl;k')
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            # self.m_selanjutnyaOnButtonClick(self,event)            
            
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            global bsizer12
            # self.properties_tamp.tabel_show()
            self.grafik_y = {}

            self.grafik_y["Kemampuan Berhitung"]=mean([self.input_peserta_rw_sw[5][1]\
                ,self.input_peserta_rw_sw[6][1]])
            self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            self.grafik_y["Kreatifitas"] =  mean([self.input_peserta_rw_sw[7][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            self.grafik_y["Judgement"]  = self.input_peserta_rw_sw[0][1]
            self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1],self.input_peserta_rw_sw[6][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1],self.input_peserta_rw_sw[3][1]])



            self.grafik_hasil = GrafikHasilLayoutInherited(self)
            self.grafik_hasil.draw(self.grafik_y)
            
            pass
        elif self.getSel == 6 :
            self.m_selanjutnya.Enable()
        else :
            # self.m_button3.Enable()
            pass

    def m_button_norma_usia(self,event):
        self.pilih_norma = 1
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel+1
        self.kelompok_usia = self.m_spinCtrl_usia.GetValue()
        self.input_peserta = self.panggilgrid.getdata()
        print (f"tipe {type(self.input_peserta[3][0])} adalah {self.input_peserta[3][0]}")
        if self.input_peserta[3][0]==0 or self.input_peserta[3][0]=="" :
            self.ge = 0
            print ("lewat sini kah")
        else :
            self.ge = self.input_peserta[3][0]
        self.databasekon = DatabaseConnect(self.nama_file)
        # konversi nilai GE , hasil akhirnya adalah self.nilai_ge
        # self.nilai_ge adalah hasil input yang telah dikonversi kedalam GE
        self.con_datakonversi_ge = DataKonversiGE(self.databasekon)
        self.nilai_ge = self.con_datakonversi_ge.konversi_ge(self.ge)
        self.nilai_ge = self.nilai_ge[3]
        # Ambil Data dari database kunci jawaban peserta untuk mencocokan dengan
        # jawaban peserta
        self.jawaban = DataBaseInput(self.databasekon)
        self.jawaban.query_data_jawaban()
        # self.input_peserta adalah input peserta (contoh di bawah adalah 
        # self.input_peserta = self.panggilgrid.getdata_arrange()) dari 
        # GUI GRID yang kemudian di hitung menghasilkan 
        # bentuk output yang diterima oleh proses selanjutnya , yakni menghitung SW
        self.input_peserta = self.panggilgrid.getdata_arrange()
        self.m_simplebook1.SetSelection(self.getSel)
        # class untuk menghitung Nilai
        self.nilai = KalkulasiNilai(self)
        self.hasil_sw = TableDataKelompokUmurConnect(self.databasekon,self)
        # self.hasil_sw.query_sw()
        self.input_peserta_rw_sw , self.sum_rw = self.hasil_sw.get_value_sw(self.input_peserta)
        print (self.sum_rw)
        self.geasamt = self.hasil_sw.get_geasamt(self.sum_rw)
        self.iq = self.hasil_sw.get_iq(self.geasamt)

        self.grafik = GrafikLayoutInherited(self)
        self.grafik.draw(self.input_peserta_rw_sw)
        self.grafik.save_figure()
        # print (self.nilai_ge[3])
        self.hasil_hal3 = RWSWScore(self)
        self.m_selanjutnya.Enable()        

        pass

    def m_button_norma_pekerjaan(self,event):
        self.pilih_norma = 2
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel+1
        self.m_simplebook1.SetSelection(self.getSel)
        self.m_selanjutnya.Enable()        

        pass

    def m_button_norma_sendiri(self,event):
        self.pilih_norma = 3
        print ("norma sendiri")
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel+1
        # self.m_simplebook1.SetSelection(self.getSel)
        self.buka_jendela_norma = NormaInherited(self)
        self.buka_jendela_norma.Show()
        pass

    def m_selanjutnyaOnButtonClick(self,event):
        # print("klik Selanjutnya")
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel+1

        # print (self.getSel)
        # self.getSel = self.m_simplebook1.GetSelection()

        

        if self.getSel == 1:
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            pass

        elif self.getSel==3 :
            self.m_selanjutnya.Disable()        
            print ("disini kita")    
            pass

        elif self.getSel == 4 :

            # 'Proses hitung dimulai ketika halaman 3 , atau pada saat penyajian grafik'
            # print("penyajian grafik proses hitung")
            # if self.select_input == 1 :
            #     pass
            # elif self.select_input == 2 :
            #     self.ambil_ge = self.panggil_nilai_total.getdata()
            #     self.ge = self.ambil_ge[3]
            #     self.kelompok_usia = self.m_spinCtrl_usia.GetValue()
            #     self.databasekon = DatabaseConnect(self.nama_file)
            #     # konversi nilai GE, hasil akhirnya adalah self.nilai_ge
            #     # self.nilai_ge adalah hasil input yang telah dikonversi kedalam GE
            #     self.con_datakonversi_ge = DataKonversiGE(self.databasekon)
            #     self.nilai_ge = self.con_datakonversi_ge.konversi_ge(self.ge)
            #     self.nilai_ge = self.nilai_ge[3]
            #     # self.input_peserta adalah input peserta total (contoh di bawah adalah 
            #     # self.input_peserta = self.panggil_nilai_total.getdata_arrange()) dari 
            #     # GUI SpinControl yang kemudian di hitung menghasilkan 
            #     # bentuk output yang diterima oleh proses selanjutnya , yakni menghitung SW
            #     self.input_peserta = self.panggil_nilai_total.getdata_arrange()
            # else:
            #     error_text == "select input tidak terdefinisikan"
            #     return error_text
            
            pass

        elif self.getSel == 5:

            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            global bsizer12
            # self.properties_tamp.tabel_show()
            self.grafik_y = {}

            self.grafik_y["Kemampuan Berhitung"]=mean([self.input_peserta_rw_sw[5][1]\
                ,self.input_peserta_rw_sw[6][1]])
            self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            self.grafik_y["Kreatifitas"] =  mean([self.input_peserta_rw_sw[7][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            self.grafik_y["Judgement"]  = self.input_peserta_rw_sw[0][1]
            self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1],self.input_peserta_rw_sw[6][1],self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1],self.input_peserta_rw_sw[3][1]])

            self.grafik_hasil = GrafikHasilLayoutInherited(self)
            self.grafik_hasil.draw(self.grafik_y)
            
            self.m_dataViewListCtrl1.InsertItem(0,["df","dfs","sdf"])
            # self.m_staticText_berpikir.SetValue()
            pass

        elif self.getSel == 6:
            if self.tipe_biodata == 1 :
                self.biodata_kandidat = [
                    self.tipe_biodata,
                    self.get_biodata()[0],
                    self.get_biodata()[1],
                    self.get_biodata()[3],
                    self.get_biodata()[4]
                ]
                self.biodata_kandidat_tamb1=[
                    self.get_biodata()[5],
                    self.get_biodata()[6],
                    self.get_biodata()[7],
                    self.get_biodata()[8],
                    self.get_biodata()[9],
                    self.get_biodata()[10],
                    self.get_biodata()[11],
                    self.get_biodata()[12],
                    self.get_biodata()[13],
                    self.kelompok_usia
                ]
            elif self.tipe_biodata == 2 :
                self.biodata_kandidat = [
                    self.tipe_biodata,
                    self.get_biodata()[2],
                    self.get_biodata()[1],
                    self.get_biodata()[3],
                    self.get_biodata()[4]
                ]
                self.biodata_kandidat_tamb2=[
                    self.get_biodata()[5],
                    self.get_biodata()[6],
                    self.get_biodata()[7],
                    self.get_biodata()[8],
                    self.get_biodata()[9]
                ]

            self.grafik_profesi = GrafikProfesi(self)
            self.grafik_profesi.draw()

            pass
        
        elif self.getSel ==  7 :
            self.m_selanjutnya.Disable()
            pass
        else :
            # self.m_button3.Enable()
            print ("masuk halaman 5")
            pass
        
        self.m_simplebook1.SetSelection(self.getSel)
        print ("kesini nggak")
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