from numpy import arange, sin, pi,array
from statistics import mean
import pathlib
import os
import wx
import wx.dataview
from views.istcore import ISTUtama,NormaSendiri
from models.query import SqliteDB,KonversiGE,TabelJawaban, \
    InputJawaban,Peserta
from pathlib import Path
from views.dataview import RWSWScore, PanggilDataView, PanggilGrid, \
    PanggilInputTotal
from controllers.ist_calculation import KalkulasiNilai
# from views.grafik_ist import GrafikLayout,GrafikHasil,GrafikProfesi
from controllers.biodata import Biodata
from controllers.grafik_tabel import *

from controllers.database_control import DatabaseConnect

class NormaSendiriInherited(NormaSendiri):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent


    def m_button_tutup_normaAllOnButtonClick(self,event):
        print ('lew')
        self.Close()
        

    def m_button_pilih_norma_allOnButtonClick(self,event):
        print ("sadfasdfs")


class DataView(ISTUtama):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.panggildataview = PanggilDataView(self)
        self.panggilgrid = PanggilGrid(self)
        self.panggil_nilai_total = PanggilInputTotal(self)
        # bsizerdataview = wx.BoxSizer(wx.VERTICAL)
        self.m_panel3.Layout()
        self.m_panel_input.Layout()
       
        pass

    def MenuTabelPendidikanOnMenuSelection(self, event):
        self.buka_tabel_norma_pekerjaan = TabelNormaLihatInherited(self)
        self.buka_tabel_norma_pekerjaan.Show()
        pass

    def TabelNormaPendidikanOnMenuSelection(self, event):
        # self.buka_tabel_norma = NormaInherited(self)
        # self.buka_tabel_norma.Show()
        # self.buka_jendela_norma.Close()
        self.buka_jendela_norma = NormaInherited(self)
        self.buka_jendela_norma.Show()

        # self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # bsizerdataview.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
        pass

        # Menu


class CekDB(DataView):

    def __init__(self, parent):
        super().__init__(parent)
        self.nama_file = "istcore"
        self.connect_db = SqliteDB("istcore")


class HalamanEventControl(CekDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.pilih = 0
        self.parent = parent
        self.m_sebelumnya.Disable()
        self.m_kembali_ke_awal.Disable()
        self.pathpict = pathlib.Path.cwd() / "icons/menubar/man.png"

        print (str(self.pathpict))
        self.image2 = wx.Image(str(self.pathpict))
        print (self.image2)
        self.re_image2 = self.image2.Rescale(200, 200)
        self.m_menuItem5.SetBitmap(wx.Bitmap(self.re_image2))

        #  print (f"Setting Tipe Biodata atau Radio Button ke
        # {self.m_radioBox_biodata.SetSelection(0)}")
        self.tipe_biodata = 0


        pass

    # def m_menuItem8OnMenuSelection(self,event):
    #     print ("hhh")
    #     pass

    def m_kembali_ke_awalOnButtonClick(self, event):
        # print("klik kembali ke awal")
        self.m_simplebook1.SetSelection(0)
        self.m_sebelumnya.Disable()
        self.m_selanjutnya.Enable()
        self.m_kembali_ke_awal.Disable()
        pass

    def m_sebelumnyaOnButtonClick(self, event):
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

        elif self.getSel == 3:
            'Proses hitung dimulai ketika halaman 3, atau pada saat penyajian grafik'
            # print ("di halaman 3 penyajian grafik")
            self.grafik = (self)
            self.grafik.draw(self.input_peserta_rw_sw)
            pass

        elif self.getSel == 4:
            # print ('hell0kl;k')
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            # self.m_selanjutnyaOnButtonClick(self, event)            

            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            global bsizer12
            # self.properties_tamp.tabel_show()
            self.grafik_y = {}

            self.grafik_y["Kemampuan Berhitung"] = mean([self.input_peserta_rw_sw[5][1]\
               , self.input_peserta_rw_sw[6][1]])
            self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            self.grafik_y["Kreatifitas"] = mean([self.input_peserta_rw_sw[7][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            self.grafik_y["Judgement"] = self.input_peserta_rw_sw[0][1]
            self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1], self.input_peserta_rw_sw[6][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1], self.input_peserta_rw_sw[3][1]])

            self.grafik_hasil = GrafikHasilLayoutInherited(self)
            self.grafik_hasil.draw(self.grafik_y)
            pass

        elif self.getSel == 6:
            self.m_selanjutnya.Enable()
        
        else:
            # self.m_button3.Enable()
            pass

    def m_button_norma_usia(self, event):

        self.pilih_norma = 1
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel + 1
        self.kelompok_usia = self.m_spinCtrl_usia.GetValue()
        self.input_peserta = self.panggilgrid.getdata()


        if self.input_peserta[0][5] == 0 or self.input_peserta[0][5] == "":
            self.ge = 0
        else:
            self.ge = self.input_peserta[5][0]

        if self.select_input == "Input Manual" :
            self.input_peserta 
            # kode kalkulasi nilai jawaban benar dan salah dibawah ini
        
        elif self.select_input == "Input Total":
            self.panggil_input_total = PanggilInputTotal(self)
            self.input_peserta = [self.panggil_nilai_total.getdata()]
            self.ge = self.input_peserta[0][3]

            # self.input_peserseta.insert(0,self.data_peserta.get_biodata()[0])
            # self.input_peserta.insert(0,self.select_input)

        for data in self.input_peserta:
            data.insert(0,self.data_peserta.get_biodata()[0])
            data.insert(0,self.select_input)

        # Ambil data peserta dari form awal data peserta menggunakan method get_biodata()
        # Format column No tes , tanggal tes, nama , jenis kelamin ,
        # tanggal lahir, usia ,asal sekolah, pendidikan , jurusan,
        # posisi pekerjaan, perusahaan, keterangan, tipe norma = 1 (tetap) 
        self.data_peserta.get_biodata()[0]
        self.data_peserta = self.data_peserta.get_biodata()
        self.data_peserta.append(1)

        self.databasepeserta = Peserta(self.connect_db)
        self.databasepeserta.insert_data_peserta(self.data_peserta)

        # Ambil Data dari database kunci jawaban peserta untuk mencocokan dengan
        # jawaban dari peserta
        self.jawaban = TabelJawaban(self.connect_db)
        self.jawaban.query_kunci_jawaban()
        self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        self.gab = []
        for data in self.input_peserta:
            self.gab.append([*data,*self.jawaban_list[self.input_peserta.index(data)]])

        self.column_name = ["SE","WA","AN",'GE','RA','ZR','FA','WU','ME']
        self.column_name_kunci_jawaban = ["KSE","KWA","KAN","KGE","KRA","KZR","KFA","KWU","KME"]

        # self.data = [1,2,2,2,2,2,2,2,2,2,2]
        self.input_jawaban = InputJawaban(self.connect_db)
        self.input_jawaban.insert_data(self.gab)


        
        
        # self.input_peserta adalah input peserta (contoh di bawah adalah 
        # self.input_peserta = self.panggilgrid.getdata_arrange()) dari 
        # GUI GRID yang kemudian di hitung menghasilkan 
        # bentuk output yang diterima oleh proses selanjutnya, yakni menghitung SW

        # konversi nilai GE, hasil akhirnya adalah self.nilai_ge
        # self.nilai_ge adalah hasil input yang telah dikonversi kedalam GE
        self.con_datakonversi_ge = KonversiGE(self.connect_db)
        self.list_konversi_ge = self.con_datakonversi_ge.query_konversi(self.ge)
        self.nilai_ge = self.list_konversi_ge[3]


        self.input_peserta = self.panggilgrid.getdata_arrange()
        self.m_simplebook1.SetSelection(self.getSel)
        # class untuk menghitung Nilai
        self.nilai = KalkulasiNilai(self)
        self.hasil_sw = TableDataKelompokUmurConnect(self.databasekon, self)
        # self.hasil_sw.query_sw()
        self.input_peserta_rw_sw, self.sum_rw = self.hasil_sw.get_value_sw(self.input_peserta)
        # print (self.sum_rw)
        self.geasamt = self.hasil_sw.get_geasamt(self.sum_rw)
        self.iq = self.hasil_sw.get_iq(self.geasamt)

        self.grafik = GrafikLayoutInherited(self)
        self.grafik.draw(self.input_peserta_rw_sw)
        self.grafik.save_figure()
        # print (self.nilai_ge[3])
        self.hasil_hal3 = RWSWScore(self)
        self.m_selanjutnya.Enable()     
        # print ("hhtet")   
        # self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue()) 
        # Ini adalah nama yang ditampilkan di label halaman 5
        self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue())
        pass

    def m_button_norma_pekerjaan(self, event):
        self.pilih_norma = 2

        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel + 1
        self.m_simplebook1.SetSelection(self.getSel)
        self.m_selanjutnya.Enable()
        self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue())

        pass

    def m_button_norma_sendiri(self, event):
        self.pilih_norma = 3
        self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue())

        if self.pilih == 1:
            print(self.buka_jendela_norma.getdata)
            print(self.buka_jendela_norma.data_norma)
            
        else:
            self.buka_jendela_norma = NormaInherited(self)
            self.buka_jendela_norma.Show()
            # self.m_staticText_pilih_norma_sendir.SetLabel(self.buka_jendela_norma.getdata[2])
            # self.m_panel29.Layout()
            # self.m_panel221.Layout()

        # print ("norma sendiri")
        self.getSel = self.m_simplebook1.GetSelection()
        self.getSel = self.getSel + 1
        # self.m_simplebook1.SetSelection(self.getSel)
        pass

    def m_buka_pilih_norma(self,event):
        self.buka_jendela_norma_sendiri = NormaSendiriInherited(self)
        Data = ["0","0","0","0"]
        self.buka_jendela_norma_sendiri.m_dataViewListCtrl30.AppendItem(Data)


        self.buka_jendela_norma_sendiri.Show()


    def m_selanjutnyaOnButtonClick(self, event):
        # print("klik Selanjutnya")
        self.getSel = self.m_simplebook1.GetSelection()

        if self.getSel == 0 :
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            if self.m_textCtrl_no_tes.GetValue() == "":
                from views.required_field import RequiredField
                self.buka_required_not_complete = RequiredField(self)
                self.buka_required_not_complete.Show()
                self.m_selanjutnya.Disable()        
                self.m_sebelumnya.Disable()
            else :
                self.getSel = self.getSel + 1
            pass

        elif self.getSel == 2 :
            self.getSel = self.getSel + 1
            pass

        elif self.getSel == 3:
            # self.m_textCtrl_biodata.SetValue(self.biodata[2])
            self.m_selanjutnya.Disable()
            self.m_choice3.SetItems(["0", "2"])

            if self.pilih == 0:
                pass
            else:
                self.m_staticText_pilih_norma_sendir.SetLabel(self.buka_jendela_norma.getdata[2])

                # self.m_panel221.Layout()
                pass
            
            # Tempat memasukkan data input total atau input manual

            pass

        elif self.getSel == 4:

            # 'Proses hitung dimulai ketika halaman 3, atau pada saat penyajian grafik'
            # print("penyajian grafik proses hitung")
            # if self.select_input == 1:
            #    pass
            # elif self.select_input == 2:
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
            #     # bentuk output yang diterima oleh proses selanjutnya, yakni menghitung SW
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
            self.grafik_y["Kemampuan Berhitung"] = mean([self.input_peserta_rw_sw[5][1]\
               , self.input_peserta_rw_sw[6][1]])
            self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            self.grafik_y["Kreatifitas"] = mean([self.input_peserta_rw_sw[7][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            self.grafik_y["Judgement"] = self.input_peserta_rw_sw[0][1]
            self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1], self.input_peserta_rw_sw[6][1], self.input_peserta_rw_sw[8][1]])
            self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1], self.input_peserta_rw_sw[3][1]])

            self.grafik_hasil = GrafikHasilLayoutInherited(self)
            self.grafik_hasil.draw(self.grafik_y)

            self.m_dataViewListCtrl1.InsertItem(0, ["df", "dfs", "sdf"])
            # self.m_staticText_berpikir.SetValue()
            pass

        elif self.getSel == 6:
            # if self.tipe_biodata == 0:
            #     self.grafik_profesi = GrafikProfesi(self)
            #     self.grafik_profesi.draw()

            #     pass

            if self.tipe_biodata == 1:
                self.biodata_kandidat = [
                    self.tipe_biodata,
                    self.get_biodata()[0],
                    self.get_biodata()[1],
                    self.get_biodata()[3],
                    self.get_biodata()[4]
                ]
                self.biodata_kandidat_tamb1 = [
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
            elif self.tipe_biodata == 2:
                self.biodata_kandidat = [
                    self.tipe_biodata,
                    self.get_biodata()[2],
                    self.get_biodata()[1],
                    self.get_biodata()[3],
                    self.get_biodata()[4]
                ]
                self.biodata_kandidat_tamb2 = [
                    self.get_biodata()[5],
                    self.get_biodata()[6],
                    self.get_biodata()[7],
                    self.get_biodata()[8],
                    self.get_biodata()[9]
                ]

            self.grafik_profesi = GrafikProfesi(self)
            self.grafik_profesi.draw()

            pass

        elif self.getSel == 7:
            self.m_selanjutnya.Disable()
            pass

        else:
            # self.m_button3.Enable()
            # print ("masuk halaman 5")
            pass
        self.m_simplebook1.SetSelection(self.getSel)
        # print ("kesini nggak")
        pass

    def m_input_manualOnButtonClick(self, event):
        self.select_input = "Input Manual"
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

    def m_input_totalOnButtonClick(self, event):
        self.select_input = "Input Total"
        # print (self.get_biodata())
        self.m_panel_input.Hide()
        self.m_panel_input_total.Show()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)
        self.m_selanjutnya.Enable()        
        self.m_kembali_ke_awal.Enable()




        pass

    def m_button_rincian_biodata_on_buttonclick(self, event):
        self.tampilkan_rincian_biodata = Biodata(self)
        self.tampilkan_rincian_biodata.Show()
        # print ("lihat rincian biodata")
        pass
