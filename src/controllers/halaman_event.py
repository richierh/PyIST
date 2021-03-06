import pandas as pd
import numpy as np
from numpy import arange, sin, pi,array
from statistics import mean
import pathlib
import os
import wx
import wx.dataview
from views.istcore import ISTUtama,NormaSendiri,TabelDataPeserta,BuatNormaSendiri
from models.query import SqliteDB,KonversiGE,TabelJawaban, \
    InputJawaban,Peserta,NoTes,HasilJawaban,\
    KunciJawabanGE,Usia,NilaiNorma,Geasamt,Iq,\
    BidangKeilmuan
from pathlib import Path
from views.dataview import RWSWScore, PanggilDataView, PanggilGrid, \
    PanggilInputTotal
from controllers.biodata import Biodata
from controllers.grafik_tabel import *
from views.pilih_tabel_norma import PilihTabel

class PilihTabelInherited(PilihTabel):

    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent
        self.SetTitle("Pilih Norma")
        self.m_staticText1.SetLabel("Norma Usia")
        self.m_staticText2.SetLabel("Norma Pendidikan")
        self.m_staticText3.SetLabel("Norma Sendiri")

        # Norma Pendidikan dan Usia
    def normapendidikanOnButtonClick(self,event):
        self.parent.norma_pilih = "Norma Usia"
        self.buka_tabel_norma = NormaInherited(self.parent)
        self.buka_tabel_norma.m_dataViewListCtrl8.Show()
        self.buka_tabel_norma.m_dataViewListCtrl9.Hide()
        self.buka_tabel_norma.m_dataViewListCtrl3.Hide()
        self.buka_tabel_norma.text_norma_pendidikan.Show()
        self.buka_tabel_norma.text_norma_pekerjaan.Hide()
        self.buka_tabel_norma.text_norma_sendiri.Hide()
        self.buka_tabel_norma.m_button24.Disable()
        self.buka_tabel_norma.m_button25.Disable()
        self.buka_tabel_norma.Layout()
        self.buka_tabel_norma.Show() 
        pass


    def normapekerjaanOnButtonClick(self,event):
        self.parent.norma_pilih = "Norma Pendidikan"

        self.buka_tabel_norma = NormaInherited(self.parent)
        self.buka_tabel_norma.m_dataViewListCtrl8.Hide()
        self.buka_tabel_norma.m_dataViewListCtrl9.Show()
        self.buka_tabel_norma.m_dataViewListCtrl3.Hide()
        self.buka_tabel_norma.text_norma_pendidikan.Hide()
        self.buka_tabel_norma.text_norma_pekerjaan.Show()
        self.buka_tabel_norma.text_norma_sendiri.Hide()
        self.buka_tabel_norma.m_button24.Disable()
        self.buka_tabel_norma.m_button25.Disable()
        self.buka_tabel_norma.Layout()
        self.buka_tabel_norma.Show() 

        pass
    

    def normasendiriOnButtonClick( self, event ):
        self.parent.norma_pilih = "Norma Sendiri"


        self.buka_tabel_norma = NormaInherited(self.parent)
        self.buka_tabel_norma.m_dataViewListCtrl8.Hide()
        self.buka_tabel_norma.m_dataViewListCtrl9.Hide()
        self.buka_tabel_norma.m_dataViewListCtrl3.Show()
        self.buka_tabel_norma.text_norma_pendidikan.Hide()
        self.buka_tabel_norma.text_norma_pekerjaan.Hide()
        self.buka_tabel_norma.text_norma_sendiri.Show()
        self.buka_tabel_norma.m_button24.Enable()
        self.buka_tabel_norma.m_button25.Enable()
        self.buka_tabel_norma.Layout()
        self.buka_tabel_norma.Show() 

 
        pass

    def normatabelclose(self,event):
        self.Close()


class NormaSendiriInherited(NormaSendiri):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        
        self.__generate()
    
    def __generate(self):
        from models.query import TabelNormaSendiri
        self.run_data = TabelNormaSendiri(self.parent.connect_db)
        self.data = self.run_data.select_data()
        self.data_str =[]

        # ubah data tabel norma sendiri kedalama bentuk string semua
        for data in self.data :
            self.data_str.append([str(self.data.index(data)+1),str(data[0]),str(data[1]),str(data[2]),str(data[3])])

        # menampilkan data tabel sendiri kedalam aplikasi GUI
        for data in self.data_str:
            self.m_dataViewListCtrl30.AppendItem(data)


    def m_data_aktif_tabel_norma_sendiri(self,event):
        # print ("nyala")
        pass

    def m_button_tutup_normaAllOnButtonClick(self,event):
        print ('lew')
        self.Close()
        

    def m_button_pilih_norma_allOnButtonClick(self,event):
        pass


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
        self.nama_file = "istcore.sqlite"
        self.connect_db = SqliteDB("istcore.sqlite")
        self.connect_db.connect_db()


class HalamanEventControl(CekDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.pilih = 0
        self.parent = parent
        self.m_sebelumnya.Disable()
        self.m_kembali_ke_awal.Disable()
        self.pathpict = pathlib.Path.cwd() / "icons/menubar/man.png"
        self.gaya_pemecahan_masalah.SetLabel("Kemantapan Berpikir")

        print (str(self.pathpict))
        self.image2 = wx.Image(str(self.pathpict))
        print (self.image2)
        self.re_image2 = self.image2.Rescale(200, 200)
        self.m_menuItem5.SetBitmap(wx.Bitmap(self.re_image2))
        #  print (f"Setting Tipe Biodata atau Radio Button ke
        # {self.m_radioBox_biodata.SetSelection(0)}")
        self.tipe_biodata = 0
        pass


    def m_kembali_ke_awalOnButtonClick(self, event):
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel1))
        self.m_sebelumnya.Disable()
        self.m_selanjutnya.Enable()
        self.m_kembali_ke_awal.Disable()
        pass

    def halaman_terakhir(self,value):
        self.datapeserta = Peserta(self.connect_db)
        self.halaman_database_peserta = self.datapeserta.query_data_peserta(self)
        self.halaman_database_peserta_np = np.array(self.halaman_database_peserta)
        self.index_column = {0:"id",1:"No Tes",2:"Tanggal Tes",3:"Nama Kandidat"
        ,4:"Jenis Kelamin",5:"Tanggal Lahir",6:"Usia",7:"Asal Sekolah",8:"Pendidikan",
        9:"Jurusan",10:"Posisi Pekerjaan",11:"Perusahaan",12:"Keterangan",13:"Tipe Norma"}

        self.halaman_database_peserta_pd = pd.DataFrame(self.halaman_database_peserta_np)
        self.hasil_akhir = self.halaman_database_peserta_pd.rename(columns = self.index_column)

        # Kebutuhan halaman terakhir 
        # No,No Tes , Nama Kandidat, Tanggal Lahir, 
        # Ubah untuk menyesuaikan dengan halaman terakhir
        self.hasil_akhir_column = self.hasil_akhir[["id","No Tes","Nama Kandidat","Tanggal Lahir"]]
        self.No = []
        for no in range(1,len(self.hasil_akhir_column)+1):
            self.No.append(no)
        self.hasil_akhir_column.insert(0,'No',self.No)

        self.data = self.hasil_akhir_column.to_numpy().astype('str').tolist()
        # import pdb
        # pdb.set_trace()

        # self.data = [tuple(data) for data in self.data]
        # self.hasil_akhir_column.columns[0] = "No"
        # self.hasil_akhir_column["No"] = self.hasil_akhir_column.index+1
        # import pdb
        # pdb.set_trace()
        for data in self.data:
            self.m_dataViewListCtrl2.AppendItem(data)

    def hapuspesertaHalamanTerakhir(self,event):
        print ("hello")
        if self.m_dataViewListCtrl2.GetSelectedRow() != -1:
            self.data = self.m_dataViewListCtrl2.GetValue(self.m_dataViewListCtrl2.GetSelectedRow(),1)

            self.m_dataViewListCtrl2.DeleteItem(self.m_dataViewListCtrl2.GetSelectedRow())
            print(self.data)
            self.m_dataViewListCtrl2.DeleteAllItems()
            self.data_peserta_halaman_terakhir = Peserta(self.connect_db)
            self.data_peserta_halaman_terakhir.hapus_peserta(self.data)
            self.halaman_terakhir(self)
        pass



    def m_sebelumnyaOnButtonClick(self, event):

    #     self.getSel = self.m_simplebook1.GetSelection()
    #     self.m_simplebook1.SetSelection(self.getSel - 1)
    #     self.getSel = self.m_simplebook1.GetSelection()
        
        if self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() )== "Pilihan Cara Input":
            self.m_selanjutnya.Enable()        
            self.m_sebelumnya.Disable()
            self.m_kembali_ke_awal.Disable()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel1))
            pass
        
        # elif self.getSel == 1:
        #     self.m_selanjutnya.Disable()        
        #     self.m_sebelumnya.Enable()
        #     self.m_kembali_ke_awal.Enable()
        #     pass
        
        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() )== "Jenis Input":
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel2))
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            self.m_kembali_ke_awal.Enable()


        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() ) == "Pilih Norma":
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel3))
            self.m_selanjutnya.Enable()

        # elif self.getSel == 3:
        #     'Proses hitung dimulai ketika halaman 3, atau pada saat penyajian grafik'
        #     # print ("di halaman 3 penyajian grafik")
        #     self.m_selanjutnya.Disable()
        #     # import pdb
        #     # pdb.set_trace()
        #     # self.grafik = (self)
        #     # self.grafik.draw(self.input_peserta_rw_sw)
        #     from models.query import Peserta
        #     self.id = self.databasepeserta.last_row()
        #     self.datapeserta = Peserta(self.connect_db)
        #     self.datapeserta.hapus_peserta(self.id)

        #     pass

        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() ) == "Hasil Norma":
        # elif self.getSel == 4:

            self.id = self.databasepeserta.last_row()
            self.datapeserta = Peserta(self.connect_db)
            self.datapeserta.hapus_peserta(self.id)

            self.m_selanjutnya.Disable()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel221))


        elif self.m_simplebook1.GetPageText(self.m_simplebook1.GetSelection()) == "Hasil Analisis IST":
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))



            # global bsizer12
            # self.grafik_y = {}

            # self.grafik_y["Kemampuan Berhitung"] = mean([self.input_peserta_rw_sw[5][1]\
            #    , self.input_peserta_rw_sw[6][1]])
            # self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            # self.grafik_y["Kreatifitas"] = mean([self.input_peserta_rw_sw[7][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            # self.grafik_y["Judgement"] = self.input_peserta_rw_sw[0][1]
            # self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1], self.input_peserta_rw_sw[6][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1], self.input_peserta_rw_sw[3][1]])

            # self.grafik_hasil = GrafikHasilLayoutInherited(self)
            # self.grafik_hasil.draw(self.grafik_y)
            pass

        elif self.m_simplebook1.GetPageText(self.m_simplebook1.GetSelection()) == "Penjurusan":
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel7))

        # elif self.getSel == 5:

        #     self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        #     self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        #     self.gab = []

        #     self.i = 0
        #     for data in self.input_peserta:
        #         self.gab.append([*data,*self.jawaban_list[self.i]])
        #         print (self.i)
        #         self.i += 1

        #     self.m_selanjutnya.Disable()

        # elif self.getSel == 6 :
        #     self.m_selanjutnya.Enable()

        # else:
        #     pass

        elif self.m_simplebook1.GetPageText(self.m_simplebook1.GetSelection()) == "Halaman Terakhir":
            self.m_selanjutnya.Enable()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel9))
            pass

    # pilihan norma usia
    def m_button_norma_usia(self, event):
        from controllers.hitung_ge import GE

        self.pilih_norma = 1
        self.kelompok_usia = self.m_spinCtrl_usia.GetValue()
        self.input_peserta = self.panggilgrid.getdata()


        if self.input_peserta[0][5] == 0 or self.input_peserta[0][5] == "":
            self.ge = 0
        else:
            self.ge = self.input_peserta[5][0]


        # Pilihan input manual atau input total
        if self.select_input == "Input Manual" :
            self.input_peserta 
        
        elif self.select_input == "Input Total":
            self.panggil_input_total = PanggilInputTotal(self)
            self.input_peserta = [self.panggil_nilai_total.getdata()]
            self.ge = self.input_peserta[0][3]

        # Data Peserta dari halaman pertama
        # Ambil data peserta dari form awal data peserta menggunakan method get_biodata()
        # Format column No tes , tanggal tes, nama , jenis kelamin ,
        # tanggal lahir, usia ,asal sekolah, pendidikan , jurusan,
        # posisi pekerjaan, perusahaan, keterangan, tipe norma = 1 (tetap) 

        self.peserta = self.data_peserta.get_biodata()[1]
        self.peserta['Tipe Norma'] = '1'        

        # input data peserta ke dalam database
        self.databasepeserta = Peserta(self.connect_db)
        self.databasepeserta.insert_data_peserta(no_tes=self.peserta.get('No Tes'),
        tanggal_tes = self.peserta.get('Tanggal Tes'),
        nama = self.peserta.get('Nama'),
        jenis_kelamin=self.peserta.get("Jenis Kelamin"),
        tanggal_lahir = self.peserta.get('Tanggal Lahir'),
        usia = self.peserta.get("Usia"),
        asal_sekolah=self.peserta.get("Asal Sekolah"),
        pendidikan_terakhir = self.peserta.get("Pendidikan Terakhir"),
        jurusan = self.peserta.get("Jurusan"),
        posisi_pekerjaan = self.peserta.get("Posisi Pekerjaan"),
        perusahaan = self.peserta.get("Perusahaan"),
        keterangan = self.peserta.get("Keterangan"),
        tipe_norma = self.peserta.get("Tipe Norma")
        )

        # for data in self.input_peserta:
        #     data.insert(0,self.peserta.get('No Tes'))
        #     data.insert(0,self.select_input)    

        # Memasukkan Nomor tes kedalam database dengan id_peserta
        self.No_Tes = NoTes(self.connect_db)
        self.No_Tes.insert(self.peserta.get('No Tes'),self.databasepeserta.last_row())
 
        # Mengambil id_tes dari tabel No tes dari id_peserta
        self.get_id_tes = self.No_Tes.get_id_test(self.databasepeserta.last_row())[0]
        
        
        # Mengolah data dari input peserta / jawaban sebelum masuk database
        # lalu di ubah ke dalam tabulasi panda
        self.get_jawaban = self.panggilgrid.getdata()    
        self.data_panda = pd.DataFrame(self.get_jawaban)
        self.no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,7,18,19,20]
        self.data_panda.insert(0,"No",self.no)
        self.id_tes = []
        for data in self.no :
            self.id_tes.append(self.get_id_tes)
        self.data_panda["id_tes"] = self.id_tes
        self.data_panda["id_kunci_jawaban"] = self.no
        self.data_numpy = pd.DataFrame.to_numpy(self.data_panda)
        # self.data_numpy = np.char.upper(self.data_numpy)
        self.data_jadi = self.data_numpy.tolist()

        # Ambil Data dari database kunci jawaban peserta untuk mencocokan dengan
        # jawaban dari peserta
        self.jawaban = TabelJawaban(self.connect_db)
        self.jawaban.query_kunci_jawaban()
        self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        self.gab = []
        self.input_jawaban = InputJawaban(self.connect_db)
        self.data_jadi =[tuple(x) for x in self.data_jadi ]
        self.input_jawaban.insert_data(self.data_jadi)
        self.get_data = self.input_jawaban.join_table(self.get_id_tes)
 
        # menghitung nilai dari input jawaban
        self.np_data = np.array(self.get_data)
        self.np_first = self.np_data[:,2:11]
        self.np_second = self.np_data[:,15:24]
        self.pengurangan = np.array([0,0,0,3,0,0,0,0,0])
        self.data_hitung = self.np_first==self.np_second
        self.jumlah = np.sum(self.data_hitung,axis=0)
        self.total = np.subtract(self.jumlah,self.pengurangan)
        self.id_tes = [self.get_id_tes]

        self.total = np.append(self.total,self.id_tes,axis = 0)
        
        # mengambil kunci jawaban untuk diolah
        # mencocokan antara kunci jawaban ge dengan input oleh peserta
        # lalu menempatkan jawaban ge yang sudah dicocokan tersebut ke total perhitungan
        self.kunci_jwbn_ge = GE(self)
        self.total[3]= self.kunci_jwbn_ge.result()

        # Melakukan konversi ge yang masih raw menjadi nilai ge yang sebenarnya

        if self.select_input == "Input Total":
            self.panggil_input_total = PanggilInputTotal(self)
            self.input_peserta = self.panggil_nilai_total.getdata()
            self.total = self.input_peserta
            self.total.append(self.id_tes[0])
            self.total = np.array(self.total)
            
        self.total = self.total.tolist()


        self.Jawaban = HasilJawaban(self.connect_db)
        self.Jawaban.insert(self.total)
        self.hasil_jawaban = self.Jawaban.query(self.id_tes)



        # self.total = np.array(self.total)

        self.GE_value = KonversiGE(self.connect_db)
        self.ge = self.GE_value.convert_ge(self.hasil_jawaban[4])[3]

        self.total = np.array(self.total)
        self.total[3] = self.ge
                     

        self.total = self.total.tolist()


        # self.input_peserta adalah input peserta (contoh di bawah adalah 
        # self.input_peserta = self.panggilgrid.getdata_arrange()) dari 
        # GUI GRID yang kemudian di hitung menghasilkan 
        # bentuk output yang diterima oleh proses selanjutnya, yakni menghitung SW

        # self.input_peserta = self.panggilgrid.getdata_arrange()
        # class untuk menghitung Nilai
        # self.input_peserta_rw_sw, self.sum_rw = self.hasil_sw.get_value_sw(self.input_peserta)
        # print (self.sum_rw)
        # self.geasamt = self.hasil_sw.get_geasamt(self.sum_rw)
        # self.iq = self.hasil_sw.get_iq(self.geasamt)
        
        self.usia= int(self.peserta.get("Usia"))
        self.NormaId = Usia(self.connect_db)
        self.get_norma_id = self.NormaId.query(self.usia)[2]

        self.NormaId = Usia(self.connect_db)
        self.get_norma_id_keilmuan = self.NormaId.query(19)[2]

        
        self.nilai_norma = NilaiNorma(self.connect_db)
        self.get_nilai_norma = self.nilai_norma.query_by_norma_id(int(self.get_norma_id))

        self.nilai_norma = NilaiNorma(self.connect_db)
        self.get_nilai_norma_keilmuan = self.nilai_norma.query_by_norma_id(int(self.get_norma_id_keilmuan))

        self.norma_np = np.array(self.get_nilai_norma)
        self.norma_pd = pd.DataFrame(self.norma_np)

        self.norma_np_keilmuan = np.array(self.get_nilai_norma_keilmuan)
        self.norma_pd_keilmuan = pd.DataFrame(self.norma_np_keilmuan)


        self.list_norma_rw_sw =[]

        self.list_norma_rw_sw_keilmuan=[]

        j = 0
        for i in range(9):
            # self.total[i]
            # import pdb
            # pdb.set_trace()
            self.nilai = self.norma_pd.loc[(self.norma_pd[2].astype(int))== int(self.total[i])]
            self.nilai_keilmuan=self.norma_pd_keilmuan.loc[(self.norma_pd_keilmuan[2].astype(int))==int(self.total[i])]
            # self.list_norma_rw_sw.append([self.total[j]])

            self.list_norma_rw_sw_keilmuan.append([self.total[i],self.nilai_keilmuan[i+3].tolist()[0]])
            self.list_norma_rw_sw.append([self.total[i],self.nilai[i+3].tolist()[0]])
            j = j+1
 

        if self.pilih_norma == 1:
            pass


        self.norma_np = np.array(self.list_norma_rw_sw)
        self.norma_pd = pd.DataFrame(self.norma_np)

        self.norma_np_keilmuan = np.array(self.list_norma_rw_sw_keilmuan)
        self.norma_pd_keilmuan = pd.DataFrame(self.norma_np_keilmuan)

        self.rw = self.norma_pd[0].astype(int).tolist()
        self.sw = self.norma_pd[1].astype(int).tolist()
        self.sum_rts = sum(self.rw)

        self.rw_keilmuan = self.norma_pd_keilmuan[0].astype(int).tolist()
        self.sw_keilmuan = self.norma_pd_keilmuan[1].astype(int).tolist()
        self.sum_rts_keilmuan = sum(self.rw_keilmuan)


        self.usia = Usia(self.connect_db)
        self.id_usia = self.usia.query(int(self.peserta.get("Usia")))[0]

        self.geasamt = Geasamt(self.connect_db)
        self.nilai_geasamt = self.geasamt.query_by_rts(self.sum_rts,self.id_usia)[2]        
        self.iq = Iq(self.connect_db)
        self.nilai_iq = self.iq.query_by_geasamt(self.nilai_geasamt)[2]
        self.nilairwsw = RWSWScore(self)
        self.grafik = GrafikLayoutInherited(self)
        
        self.grafik.draw(self.list_norma_rw_sw)
        # self.grafik.save_figure()
        # print (self.nilai_ge[3])_jawaban()
        # self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        # self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        # self.gab = []

        # self.i = 0
        # for data in self.input_peserta:
            # self.gab.append([*data,*self.jawaban_list[self.i]])
            # print (self.i)
            # self.i += 1
        # print (self.gab)

        # self.input_jawaban 
        # self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue()) 
        # Ini adalah nama yang ditampilkan di label halaman 5
        self.databasepeserta.query_data_peserta()
        self.nama = self.peserta.get('Nama')
        self.m_textCtrl_biodata.SetValue(self.nama)
        self.m_selanjutnya.Enable()
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))
        pass

    def m_button_norma_pendidikan(self, event):
        self.pilih_norma = 2

        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))
        self.m_selanjutnya.Enable()
        self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue())


        from controllers.hitung_ge import GE

        self.kelompok_usia = self.m_spinCtrl_usia.GetValue()
        self.input_peserta = self.panggilgrid.getdata()


        if self.input_peserta[0][5] == 0 or self.input_peserta[0][5] == "":
            self.ge = 0
        else:
            self.ge = self.input_peserta[5][0]


        # Pilihan input manual atau input total
        if self.select_input == "Input Manual" :
            self.input_peserta 
        
        elif self.select_input == "Input Total":
            self.panggil_input_total = PanggilInputTotal(self)
            self.input_peserta = [self.panggil_nilai_total.getdata()]
            self.ge = self.input_peserta[0][3]

        # Data Peserta dari halaman pertama
        # Ambil data peserta dari form awal data peserta menggunakan method get_biodata()
        # Format column No tes , tanggal tes, nama , jenis kelamin ,
        # tanggal lahir, usia ,asal sekolah, pendidikan , jurusan,
        # posisi pekerjaan, perusahaan, keterangan, tipe norma = 1 (tetap) 

        self.peserta = self.data_peserta.get_biodata()[1]
        self.peserta['Tipe Norma'] = '1'        

        # input data peserta ke dalam database
        self.databasepeserta = Peserta(self.connect_db)
        self.databasepeserta.insert_data_peserta(no_tes=self.peserta.get('No Tes'),
        tanggal_tes = self.peserta.get('Tanggal Tes'),
        nama = self.peserta.get('Nama'),
        jenis_kelamin=self.peserta.get("Jenis Kelamin"),
        tanggal_lahir = self.peserta.get('Tanggal Lahir'),
        usia = self.peserta.get("Usia"),
        asal_sekolah=self.peserta.get("Asal Sekolah"),
        pendidikan_terakhir = self.peserta.get("Pendidikan Terakhir"),
        jurusan = self.peserta.get("Jurusan"),
        posisi_pekerjaan = self.peserta.get("Posisi Pekerjaan"),
        perusahaan = self.peserta.get("Perusahaan"),
        keterangan = self.peserta.get("Keterangan"),
        tipe_norma = self.peserta.get("Tipe Norma")
        )

        # for data in self.input_peserta:
        #     data.insert(0,self.peserta.get('No Tes'))
        #     data.insert(0,self.select_input)    

        # Memasukkan Nomor tes kedalam database dengan id_peserta
        self.No_Tes = NoTes(self.connect_db)
        self.No_Tes.insert(self.peserta.get('No Tes'),self.databasepeserta.last_row())

       # Mengambil id_tes dari tabel No tes dari id_peserta
        self.get_id_tes = self.No_Tes.get_id_test(self.databasepeserta.last_row())[0]
        
        
        # Mengolah data dari input peserta / jawaban sebelum masuk database
        # lalu di ubah ke dalam tabulasi panda
        self.get_jawaban = self.panggilgrid.getdata()    
        self.data_panda = pd.DataFrame(self.get_jawaban)
        self.no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,7,18,19,20]
        self.data_panda.insert(0,"No",self.no)
        self.id_tes = []
        for data in self.no :
            self.id_tes.append(self.get_id_tes)
        self.data_panda["id_tes"] = self.id_tes

        self.data_panda["id_kunci_jawaban"] = self.no
        self.data_numpy = pd.DataFrame.to_numpy(self.data_panda)
        # self.data_numpy = np.char.upper(self.data_numpy)
        self.data_jadi = self.data_numpy.tolist()

        # Ambil Data dari database kunci jawaban peserta untuk mencocokan dengan
        # jawaban dari peserta
        self.jawaban = TabelJawaban(self.connect_db)
        self.jawaban.query_kunci_jawaban()
        self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        self.gab = []
        self.input_jawaban = InputJawaban(self.connect_db)
        self.data_jadi =[tuple(x) for x in self.data_jadi ]
        self.input_jawaban.insert_data(self.data_jadi)
        self.get_data = self.input_jawaban.join_table(self.get_id_tes)
 
        # menghitung nilai dari input jawaban
        self.np_data = np.array(self.get_data)
        self.np_first = self.np_data[:,2:11]
        self.np_second = self.np_data[:,15:24]
        self.pengurangan = np.array([0,0,0,3,0,0,0,0,0])
        self.data_hitung = self.np_first==self.np_second
        self.jumlah = np.sum(self.data_hitung,axis=0)
        self.total = np.subtract(self.jumlah,self.pengurangan)
        self.id_tes = [self.get_id_tes]

        self.total = np.append(self.total,self.id_tes,axis = 0)
        
        # mengambil kunci jawaban untuk diolah
        # mencocokan antara kunci jawaban ge dengan input oleh peserta
        # lalu menempatkan jawaban ge yang sudah dicocokan tersebut ke total perhitungan
        self.kunci_jwbn_ge = GE(self)
        self.total[3]= self.kunci_jwbn_ge.result()

        # Melakukan konversi ge yang masih raw menjadi nilai ge yang sebenarnya

        if self.select_input == "Input Total":
            self.panggil_input_total = PanggilInputTotal(self)
            self.input_peserta = self.panggil_nilai_total.getdata()
            self.total = self.input_peserta
            self.total.append(self.id_tes[0])
            self.total = np.array(self.total)
            
        self.total = self.total.tolist()

        self.Jawaban = HasilJawaban(self.connect_db)
        self.Jawaban.insert(self.total)
        self.hasil_jawaban = self.Jawaban.query(self.id_tes)

        # self.total = np.array(self.total)

        self.GE_value = KonversiGE(self.connect_db)
        self.ge = self.GE_value.convert_ge(self.hasil_jawaban[4])[3]

        self.total = np.array(self.total)
        self.total[3] = self.ge
                     

        self.total = self.total.tolist()

        # self.input_peserta adalah input peserta (contoh di bawah adalah 
        # self.input_peserta = self.panggilgrid.getdata_arrange()) dari 
        # GUI GRID yang kemudian di hitung menghasilkan 
        # bentuk output yang diterima oleh proses selanjutnya, yakni menghitung SW

        # self.input_peserta = self.panggilgrid.getdata_arrange()
        # class untuk menghitung Nilai
        # self.input_peserta_rw_sw, self.sum_rw = self.hasil_sw.get_value_sw(self.input_peserta)
        # print (self.sum_rw)
        # self.geasamt = self.hasil_sw.get_geasamt(self.sum_rw)
        # self.iq = self.hasil_sw.get_iq(self.geasamt)

        
        # self.usia= int(self.peserta.get(19))
        self.usia = 19

        # self.NormaId = Usia(self.connect_db)
        # self.get_norma_id = self.NormaId.query(self.usia)[2]

        # karena norma Pendidikan maka digunakan self.get_norma_id = 2

        self.get_norma_id = 2
        self.nilai_norma = NilaiNorma(self.connect_db)
        self.get_nilai_norma = self.nilai_norma.query_by_norma_id(int(self.get_norma_id))
        

        self.NormaId = Usia(self.connect_db)
        self.get_norma_id_keilmuan = self.NormaId.query(19)[2]
        self.nilai_norma = NilaiNorma(self.connect_db)
        self.get_nilai_norma_keilmuan = self.nilai_norma.query_by_norma_id(int(self.get_norma_id_keilmuan))

        self.norma_np_keilmuan = np.array(self.get_nilai_norma_keilmuan)
        self.norma_pd_keilmuan = pd.DataFrame(self.norma_np_keilmuan)

        self.norma_np = np.array(self.get_nilai_norma)
        self.norma_pd = pd.DataFrame(self.norma_np)
        self.list_norma_rw_sw =[]

        self.list_norma_rw_sw_keilmuan=[]

        j = 0
        for i in range(9):
            # self.total[i]
            # import pdb
            # pdb.set_trace()
            self.nilai = self.norma_pd.loc[(self.norma_pd[2].astype(int))== int(self.total[i])]
            self.nilai_keilmuan=self.norma_pd_keilmuan.loc[(self.norma_pd_keilmuan[2].astype(int))==int(self.total[i])]

            # self.list_norma_rw_sw.append([self.total[j]])
            self.list_norma_rw_sw_keilmuan.append([self.total[i],self.nilai_keilmuan[i+3].tolist()[0]])

            self.list_norma_rw_sw.append([self.total[i],self.nilai[i+3].tolist()[0]])
            j = j+1
 

        if self.pilih_norma == 1:
            pass


        self.norma_np = np.array(self.list_norma_rw_sw)
        self.norma_pd = pd.DataFrame(self.norma_np)
 
        self.norma_np_keilmuan = np.array(self.list_norma_rw_sw_keilmuan)
        self.norma_pd_keilmuan = pd.DataFrame(self.norma_np_keilmuan)
 
        self.rw = self.norma_pd[0].astype(int).tolist()
        self.sw = self.norma_pd[1].astype(int).tolist()
        self.sum_rts = sum(self.rw)

        self.rw_keilmuan = self.norma_pd_keilmuan[0].astype(int).tolist()
        self.sw_keilmuan = self.norma_pd_keilmuan[1].astype(int).tolist()
        self.sum_rts_keilmuan = sum(self.rw_keilmuan)

 
        self.usia = Usia(self.connect_db)
        self.id_usia = self.usia.query(int(self.peserta.get("Usia")))[0]

        self.id_usia = 10
        self.geasamt = Geasamt(self.connect_db)
        self.nilai_geasamt = self.geasamt.query_by_rts(self.sum_rts,self.id_usia)[2]        
        self.iq = Iq(self.connect_db)
        self.nilai_iq = self.iq.query_by_geasamt(self.nilai_geasamt)[2]
        self.nilairwsw = RWSWScore(self)
        self.grafik = GrafikLayoutInherited(self)

        # import pdb
        # pdb.set_trace()

        self.grafik.draw(self.list_norma_rw_sw)
        # self.grafik.save_figure()
        # print (self.nilai_ge[3])_jawaban()
        # self.jawab_tambah =  self.jawaban.query_kunci_jawaban()
        # self.jawaban_list = [data[2:] for data in self.jawab_tambah]
        # self.gab = []

        # self.i = 0
        # for data in self.input_peserta:
            # self.gab.append([*data,*self.jawaban_list[self.i]])
            # print (self.i)
            # self.i += 1
        # print (self.gab)

        # self.input_jawaban 
        # self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue()) 
        # Ini adalah nama yang ditampilkan di label halaman 5
        self.databasepeserta.query_data_peserta()
        self.nama = self.peserta.get('Nama')
        self.m_textCtrl_biodata.SetValue(self.nama)
        self.m_selanjutnya.Enable()
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))
 

        pass

    def m_button_norma_sendiri(self, event):
        self.pilih_norma = 3
        self.m_textCtrl_biodata.SetValue(self.m_textCtrl_nama.GetValue())

        import pdb
        pdb.set_trace()

        if self.pilih == 1:

            #  Disini perhitungannya dimulai 
            print(self.buka_jendela_norma.getdata)
            print(self.buka_jendela_norma.data_norma)
            
        else:
            self.buka_jendela_norma = NormaInherited(self)
            self.buka_jendela_norma.Show()
            self.buka_jendela_norma.m_dataViewListCtrl8.Hide()
            self.buka_jendela_norma.m_dataViewListCtrl9.Hide()
            self.buka_jendela_norma.m_dataViewListCtrl3.Show()
            self.buka_jendela_norma.text_norma_pendidikan.Hide()
            self.buka_jendela_norma.text_norma_pekerjaan.Hide()
            self.buka_jendela_norma.text_norma_sendiri.Show()
            self.buka_jendela_norma.m_button24.Enable()
            self.buka_jendela_norma.m_button25.Enable()
            self.buka_jendela_norma.Layout()
            self.buka_jendela_norma.Show() 

            # self.m_staticText_pilih_norma_sendir.SetLabel(self.buka_jendela_norma.getdata[2])
            # self.m_panel29.Layout()
            # self.m_panel221.Layout()

        # print ("norma sendiri")
        # self.getSel = self.m_simplebook1.GetSelection()
        # self.getSel = self.getSel + 1
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))
        pass

    def m_buka_pilih_norma(self,event):
        self.buka_jendela_norma = NormaInherited(self)
        self.buka_jendela_norma.Show()
        self.buka_jendela_norma.m_dataViewListCtrl8.Hide()
        self.buka_jendela_norma.m_dataViewListCtrl9.Hide()
        self.buka_jendela_norma.m_dataViewListCtrl3.Show()
        self.buka_jendela_norma.text_norma_pendidikan.Hide()
        self.buka_jendela_norma.text_norma_pekerjaan.Hide()
        self.buka_jendela_norma.text_norma_sendiri.Show()
        self.buka_jendela_norma.m_button24.Enable()
        self.buka_jendela_norma.m_button25.Enable()
        self.buka_jendela_norma.Layout()
        self.buka_jendela_norma.Show() 



    def m_selanjutnyaOnButtonClick(self, event):
        # print("klik Selanjutnya")
        # self.getSel = self.m_simplebook1.GetSelection()

        if self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection()) == "Halaman Biodata":
            # import pdb
            # pdb.set_trace()
            self.m_selanjutnya.Disable()        
            self.m_sebelumnya.Enable()
            self.m_kembali_ke_awal.Enable()
            if self.m_textCtrl_no_tes.GetValue() == "":
                from views.required_field import RequiredField
                self.buka_required_not_complete = RequiredField(self)
                self.buka_required_not_complete.Show()
                self.m_selanjutnya.Disable()        
                self.m_sebelumnya.Disable()
            else :
                self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel2))
                # self.m_simplebook1.GetSelection(self.m_simplebook1.FindPage(self.m_panel2))

                # self.getSel = self.getSel + 1
            pass


        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() ) == "Jenis Input":
            
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel221))
            self.m_selanjutnya.Disable()

            pass
        

        # elif self.getSel == 4:
        #     # self.m_textCtrl_biodata.SetValue(self.biodata[2])
        #     # self.m_choice3.SetItems(["0", "2"])
        #     # import pdb
        #     # pdb.set_trace()
        #     if self.pilih == 0:
        #         pass
        #     else:
        #         self.m_staticText_pilih_norma_sendir.SetLabel(self.buka_jendela_norma.getdata[2])

        #         # self.m_panel221.Layout()
        #         pass
            
        #     # Tempat memasukkan data input total atau input manual
        #     self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel6))

        #     # self.getSel = self.getSel +1


            # import pdb
            # pdb.set_trace()



            pass

        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() ) == "Hasil Norma":

            self.list_norma_dict = {}
            # urutan SE,WA,AN, GE, RA,ZR,FA,WU,ME

            self.list_norma_dict["SE"] = self.list_norma_rw_sw[0]
            self.list_norma_dict["WA"] = self.list_norma_rw_sw[1]
            self.list_norma_dict["AN"] = self.list_norma_rw_sw[2]
            self.list_norma_dict["GE"] = self.list_norma_rw_sw[3]
            self.list_norma_dict["RA"] = self.list_norma_rw_sw[4]
            self.list_norma_dict["ZR"] = self.list_norma_rw_sw[5]
            self.list_norma_dict["FA"] = self.list_norma_rw_sw[6]
            self.list_norma_dict["WU"] = self.list_norma_rw_sw[7]
            self.list_norma_dict["ME"] = self.list_norma_rw_sw[8]


            # Perhitungan untuk analisa hasil IST
            # Kemampuan berhitung = Ra dan zr
            self.hasil_analisa_dict ={}
            import statistics
            self.data =[self.list_norma_dict["ZR"][1],self.list_norma_dict["FA"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Kemampuan Berhitung"] = self.value_dict

            self.data = [self.list_norma_dict["ME"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Daya Ingat dan Konsentrasi"] = self.value_dict
            
            # Kreatifitas
            self.data = [self.list_norma_dict["FA"][1],self.list_norma_dict["WU"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Kreatifitas"] = self.value_dict

            # Ketelitian
            self.data = [self.list_norma_dict["RA"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Ketelitian"] = self.value_dict

            # Judgment
            self.data = [self.list_norma_dict["SE"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Judgment"] = self.value_dict

            # Daya Analisis
            self.data = [self.list_norma_dict["AN"][1],self.list_norma_dict["WU"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Daya Analisis"] = self.value_dict

            # Pengambilan Keputusan
            self.data = [self.list_norma_dict["SE"][1],self.list_norma_dict["WU"][1],self.list_norma_dict["ZR"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Pengmabilan Keputusan"] = self.value_dict

            # Kemampuan Berbahasa
            self.data = [self.list_norma_dict["GE"][1],self.list_norma_dict["WA"][1]]
            self.value_dict = statistics.mean(self.data)
            # self.value_dict = sum(self.data)

            self.hasil_analisa_dict["Kemampuan Berbahasa"] = self.value_dict

            # import pdb
            # pdb.set_trace()

            'Proses hitung dimulai ketika halaman 3, atau pada saat penyajian grafik'
            print("penyajian grafik proses hitung")
            self.grafik_hasil = GrafikHasilLayoutInherited(self)
            self.tampilan_grafik = self.grafik_hasil.draw()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel7))
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
            # self.getSel = self.getSel +1
            #  jika penjumlahan an + zr > GE + RA
            self.sum_an_zr = self.list_norma_dict["AN"][1] + self.list_norma_dict["ZR"][1]
            self.sum_ge_ra = self.list_norma_dict["GE"][1] + self.list_norma_dict["RA"][1]
            if not self.sum_an_zr >= self.sum_ge_ra:
                self.gaya_pemecahan_masalah.SetLabel("Fleksibilitas Berpikir")
            else :
                self.gaya_pemecahan_masalah.SetLabel("Kemantapan Berpikir")
            pass

        # elif self.m_simplebook1.GetPageText( self.m_simplebook1.FindPage(self.m_panel221 ) ) == "Pilih Norma":
        #     import pdb
        #     pdb.set_trace()
        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() )=="Hasil Analisis IST":
            self.list_norma_dict_keilmuan = {}
            # urutan SE,WA,AN, GE, RA,ZR,FA,WU,ME

            self.list_norma_dict_keilmuan["SE"] = self.list_norma_rw_sw_keilmuan[0]
            self.list_norma_dict_keilmuan["WA"] = self.list_norma_rw_sw_keilmuan[1]
            self.list_norma_dict_keilmuan["AN"] = self.list_norma_rw_sw_keilmuan[2]
            self.list_norma_dict_keilmuan["GE"] = self.list_norma_rw_sw_keilmuan[3]
            self.list_norma_dict_keilmuan["RA"] = self.list_norma_rw_sw_keilmuan[4]
            self.list_norma_dict_keilmuan["ZR"] = self.list_norma_rw_sw_keilmuan[5]
            self.list_norma_dict_keilmuan["FA"] = self.list_norma_rw_sw_keilmuan[6]
            self.list_norma_dict_keilmuan["WU"] = self.list_norma_rw_sw_keilmuan[7]
            self.list_norma_dict_keilmuan["ME"] = self.list_norma_rw_sw_keilmuan[8]
            
            
            self.database_bidang_keilmuan = BidangKeilmuan(self.connect_db)
            self.data_bidang_keilmuan= self.database_bidang_keilmuan.query_bidang_keilmuan()
            self.data_keilmuan_np = np.array(self.data_bidang_keilmuan)
            self.data_keilmuan_pd = pd.DataFrame(self.data_keilmuan_np)

            self.bidang_keilmuan = []
            if self.list_norma_dict_keilmuan["RA"][1]>100 and \
                self.list_norma_dict_keilmuan["ZR"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100:
                    # print ("Sajikan tabel")
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Matematika & Ilmu Pengetahuan Alam'] 
                    self.rslt_df_mipa = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_mipa)
                    pass
            
            if self.list_norma_dict_keilmuan["AN"][1]>100 and \
                self.list_norma_dict_keilmuan["GE"][1]>100 and \
                    self.list_norma_dict_keilmuan["FA"][1]>100 and \
                        self.list_norma_dict_keilmuan['WU']>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Ilmu Pertanian'] 
                    self.rslt_df_pertanian = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_pertanian)

                    # print ("Sajikan tabel")
                    pass

            if self.list_norma_dict_keilmuan["WU"][1]>100 and \
                self.list_norma_dict_keilmuan["FA"][1]>100 and \
                    self.list_norma_dict_keilmuan["RA"][1]>100:
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Teknik Sipil & Perencanaan'] 
                    self.rslt_df_sipil = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_sipil)

                    # print ("Sajikan tabel")
                    pass

            if self.list_norma_dict_keilmuan["RA"][1]>100 and \
                self.list_norma_dict_keilmuan["ZR"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Teknik Industri'] 
                    self.rslt_df_industri = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_industri)

                    # print ("Sajikan tabel")
                    pass

            if self.list_norma_dict_keilmuan["FA"][1]>100 and \
                self.list_norma_dict_keilmuan["RA"][1]>100 and \
                    self.list_norma_dict_keilmuan["ZR"][1]>100:
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Teknologi Mineral'] 
                    self.rslt_df_mineral = self.rslt_df.to_numpy().tolist()

                    self.bidang_keilmuan.extend(self.rslt_df_mineral)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["ME"][1]>100 and \
                self.list_norma_dict_keilmuan["GE"][1]>100 and \
                self.list_norma_dict_keilmuan["AN"][1]>100 and \
                self.list_norma_dict_keilmuan["FA"][1]>100 and \
                    self.list_norma_dict_keilmuan["WU"][1]>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Ilmu Kesehatan'] 
                    self.rslt_df_kesehatan = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_kesehatan)

                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["WA"][1]>100 and \
                self.list_norma_dict_keilmuan["GE"][1]>100 and \
                self.list_norma_dict_keilmuan["ME"][1]>100 and \
                    self.list_norma_dict_keilmuan["SE"][1]>100:
                    
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Ilmu Sastra & Budaya'] 
                    self.rslt_df_sastra = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_sastra)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["FA"][1]>100 and \
                self.list_norma_dict_keilmuan["WA"][1]>100 and \
                self.list_norma_dict_keilmuan["GE"][1]>100 and \
                self.list_norma_dict_keilmuan["AN"][1]>100 and \
                    self.list_norma_dict_keilmuan["ZR"][1]>100:
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Seni Rupa & Desain'] 
                    self.rslt_df_senirupa = self.rslt_df.to_numpy().tolist()

                    self.bidang_keilmuan.extend(self.rslt_df_senirupa)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["RA"][1]>100 and \
                self.list_norma_dict_keilmuan["GE"][1]>100 and \
                    self.list_norma_dict_keilmuan["ZR"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Ekonomi'] 
                    self.rslt_df_ekonomi = self.rslt_df.to_numpy().tolist()

                    self.bidang_keilmuan.extend(self.rslt_df_ekonomi)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["SE"][1]>100 and \
                self.list_norma_dict_keilmuan["ME"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100 and \
                    self.list_norma_dict_keilmuan["WA"][1]>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Hukum'] 
                    self.rslt_df_hukum = self.rslt_df.to_numpy().tolist()
                    
                    self.bidang_keilmuan.extend(self.rslt_df_hukum)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["SE"][1]>100 and \
                self.list_norma_dict_keilmuan["WA"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100 and \
                    self.list_norma_dict_keilmuan["GE"][1]>100:

                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Sosial & Politik'] 
                    self.rslt_df_sospol = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_sospol)

                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["ME"][1]>100 and \
                self.list_norma_dict_keilmuan["WA"][1]>100 and \
                    self.list_norma_dict_keilmuan["AN"][1]>100:
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Komunikasi'] 
                    self.rslt_df_komunikasi = self.rslt_df.to_numpy().tolist()

                    self.bidang_keilmuan.extend(self.rslt_df_komunikasi)
                    # print ("Sajikan tabel")
                    pass
            if self.list_norma_dict_keilmuan["SE"][1]>100 and \
                self.list_norma_dict_keilmuan["AN"][1]>100 and \
                    self.list_norma_dict_keilmuan["WA"][1]>100:
                    self.rslt_df = self.data_keilmuan_pd[self.data_keilmuan_pd[2] == 'Psikologi'] 
                    self.rslt_df_psikologi = self.rslt_df.to_numpy().tolist()
                    self.bidang_keilmuan.extend(self.rslt_df_psikologi)
                    pass
            # import pdb 
            # pdb.set_trace()            

                    # print ("Sajikan tabel")
                    

            # elif self.getSel == 6:
            # self.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            # global bsizer12
            # # self.properties_tamp.tabel_show()
            # self.grafik_y = {}
            # self.grafik_y["Kemampuan Berhitung"] = mean([self.input_peserta_rw_sw[5][1]\
            #    , self.input_peserta_rw_sw[6][1]])
            # self.grafik_y["Daya Ingat dan Konsentrasi"] = self.input_peserta_rw_sw[4][1]
            # self.grafik_y["Kreatifitas"] = mean([self.input_peserta_rw_sw[7][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Ketelitian"] = self.input_peserta_rw_sw[5][1]
            # self.grafik_y["Judgement"] = self.input_peserta_rw_sw[0][1]
            # self.grafik_y["Daya Analisis"] = mean([self.input_peserta_rw_sw[2][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Pengembalian Keputusan"] = mean([self.input_peserta_rw_sw[0][1], self.input_peserta_rw_sw[6][1], self.input_peserta_rw_sw[8][1]])
            # self.grafik_y["Kemampuan Berbahasa"] = mean([self.input_peserta_rw_sw[1][1], self.input_peserta_rw_sw[3][1]])

            # self.grafik_hasil = GrafikHasilLayoutInherited(self)
            # self.grafik_hasil.draw(self.grafik_y)

            # self.m_dataViewListCtrl1.InsertItem(0, ["df", "dfs", "sdf"])
            # self.m_staticText_berpikir.SetValue()
            self.sajikan_grafik = GrafikProfesiInherited(self)
            self.sajikan_grafik.draw()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel9))
            pass

        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() )=="Penjurusan":
        # elif self.getSel == 7:
            # if self.tipe_biodata == 0:
            #     self.grafik_profesi = GrafikProfesi(self)
            #     self.grafik_profesi.draw()

            #     pass

            # if self.tipe_biodata == 1:
            #     self.biodata_kandidat = [
            #         self.tipe_biodata,
            #         self.get_biodata()[0],
            #         self.get_biodata()[1],
            #         self.get_biodata()[3],
            #         self.get_biodata()[4]
            #     ]
            #     self.biodata_kandidat_tamb1 = [
            #         self.get_biodata()[5],
            #         self.get_biodata()[6],
            #         self.get_biodata()[7],
            #         self.get_biodata()[8],
            #         self.get_biodata()[9],
            #         self.get_biodata()[10],
            #         self.get_biodata()[11],
            #         self.get_biodata()[12],
            #         self.get_biodata()[13],
            #         self.kelompok_usia
            #     ]
            # elif self.tipe_biodata == 2:
            #     self.biodata_kandidat = [
            #         self.tipe_biodata,
            #         self.get_biodata()[2],
            #         self.get_biodata()[1],
            #         self.get_biodata()[3],
            #         self.get_biodata()[4]
            #     ]
            #     self.biodata_kandidat_tamb2 = [
            #         self.get_biodata()[5],
            #         self.get_biodata()[6],
            #         self.get_biodata()[7],
            #         self.get_biodata()[8],
            #         self.get_biodata()[9]
            #     ]
            # self.grafik_profesi = GrafikProfesi(self)
            # self.grafik_profesi.draw()
            self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel10))
            self.m_selanjutnya.Disable()
            self.m_dataViewListCtrl2.DeleteAllItems()
            self.halaman_terakhir(self)
            pass

        elif self.m_simplebook1.GetPageText( self.m_simplebook1.GetSelection() ) == "Halaman Terakhir":
        # elif self.getSel == 8:
            # self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel10))
            pass

        else:
            # self.m_button3.Enable()
            # print ("masuk halaman 5")
            pass
        # self.m_simplebook1.SetSelection(self.getSel)
        # print ("kesini nggak")
        pass

    def m_input_manualOnButtonClick(self, event):
        self.select_input = "Input Manual"
        # print (self.get_biodata())
        self.m_panel_input.Show()
        self.m_panel_input_total.Hide()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel3))
        self.m_selanjutnya.Enable()     
        self.m_kembali_ke_awal.Enable()
        self.m_panel3.Layout()

        self.m_panel_input.Layout()
        # import pdb
        # pdb.set_trace()
        pass

    def m_input_totalOnButtonClick(self, event):
        self.select_input = "Input Total"
        # print (self.get_biodata())
        self.m_panel_input.Hide()
        self.m_panel_input_total.Show()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(self.m_simplebook1.FindPage(self.m_panel3))
        self.m_selanjutnya.Enable()        
        self.m_kembali_ke_awal.Enable()
        pass

    def m_button_rincian_biodata_on_buttonclick(self, event):
        # from controllers.properties_ist import PropertiesInput
        # self.data_peserta = PropertiesInput(self)
        self.tampilkan_rincian_biodata = BiodataInherited(self)
        self.tampilkan_rincian_biodata.Show()


        # print ("lihat rincian biodata")
        pass


class BiodataInherited(Biodata):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        self.m_textCtrl_no_tes1.SetValue(self.parent.data_peserta[0])
        self.m_textCtrl_tanggal_tes1.SetValue(self.parent.data_peserta[1])
        self.m_textCtrl_nama1.SetValue(self.parent.data_peserta[2])
        self.m_textCtrl_jenis_kelamin1.SetValue(self.parent.data_peserta[3])
        self.m_textCtrl_tanggal_lahir1.SetValue(self.parent.data_peserta[4])
        self.m_textCtrl_usia1.SetValue(str(self.parent.data_peserta[5]))
        self.m_textCtrl_asal_sekolah_universitas.SetValue(self.parent.data_peserta[6])
        self.m_textCtrl_pendidikan_terakhir1.SetValue(self.parent.data_peserta[7])
        self.m_textCtrl_jurusan.SetValue(self.parent.data_peserta[8])
        self.m_textCtrl_posisi_pekerjaan.SetValue(self.parent.data_peserta[9])
        self.m_textCtrl_perusahaan.SetValue(self.parent.data_peserta[10])
        self.m_textCtrl_keterangan.SetValue(self.parent.data_peserta[11])
        

    def m_tutup_biodataOnClick(self,event) :
        self.Close()