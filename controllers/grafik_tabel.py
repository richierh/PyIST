import wx
from numpy import arange, sin, pi

from views.grafik_ist import GrafikLayout, GrafikHasil, GrafikProfesi
from views.istcore import Norma, TabelNorma, FrameRow, NormaAll, TabelNormaLihat,BuatNormaSendiri
from controllers.nama_norma_inherited import NamaNormaInherited
from models.query import JenisNorma,TabelNormaSendiri,TabelNormaPendidikan,NormaSendiri\
    ,TabelNormaPekerjaan

class TabelNormaSendiriInherited(TabelNorma):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.connect_db = self.parent.parent.parent.connect_db
        
        self.m_dataViewListCtrl3 = self.parent.parent.m_dataViewListCtrl3
        self.m_dataViewListCtrl8 = self.parent.parent.m_dataViewListCtrl8
        self.m_dataViewListCtrl9 = self.parent.parent.m_dataViewListCtrl9


        if self.m_dataViewListCtrl3.IsShown() == True :
            print ("kesini")
            for data in range(1,34):
                self.m_dataViewListCtrl4.AppendItem([str(data),"","","","","","","","","",""])

        elif self.m_dataViewListCtrl8.IsShown() == True :
            # Berdasarkan kelompok umur 
            self.getRow = self.m_dataViewListCtrl8.GetSelectedRow
            self.NormaID = self.m_dataViewListCtrl8.GetTextValue(self.getRow,0)
            
            pass        

        elif self.m_dataViewListCtrl9.IsShown() == True :
            pass


        else :
            print ("tidak ada pilihan")

        pass

    def m_button_ok_tabel_normaOnButtonClick(self,event):
        self.insertDataNorma = TabelNormaSendiri(self.connect_db)
        self.data = [self.parent.m_nama_norma_sendiri.GetValue(),self.parent.m_keterangan_norma_sendiri.GetValue()]
        self.insertDataNorma.insert_data(self.data)
        self.selectNorma = TabelNormaSendiri(self.connect_db)
        # memperoleh nilai IdNorma
        self.selectNorma.select_from(self.parent.m_nama_norma_sendiri.GetValue())
        self.parent.parent.m_dataViewListCtrl3.DeleteAllItems()


        self.data = self.selectNorma.select_data()
        self.data_str =[]

        # ubah data tabel norma sendiri kedalama bentuk string semua
        for data in self.data :
            self.data_str.append([str(self.data.index(data)+1),str(data[0]),str(data[1]),str(data[2]),str(data[3])])

        # menampilkan data tabel sendiri kedalam aplikasi GUI
        for data in self.data_str:
            self.parent.parent.m_dataViewListCtrl3.AppendItem(data)


        self.data_norma_sendiri = []
        for data in range(0,self.m_dataViewListCtrl4.GetItemCount()):
            self.datainput= [
            self.m_dataViewListCtrl4.GetTextValue(data,0),
            self.m_dataViewListCtrl4.GetTextValue(data,1),
            self.m_dataViewListCtrl4.GetTextValue(data,2),
            self.m_dataViewListCtrl4.GetTextValue(data,3),
            self.m_dataViewListCtrl4.GetTextValue(data,4),
            self.m_dataViewListCtrl4.GetTextValue(data,5),
            self.m_dataViewListCtrl4.GetTextValue(data,6),
            self.m_dataViewListCtrl4.GetTextValue(data,7),
            self.m_dataViewListCtrl4.GetTextValue(data,8),
            self.m_dataViewListCtrl4.GetTextValue(data,9),
            self.m_dataViewListCtrl4.GetTextValue(data,10),
            self.selectNorma.select_from(self.parent.m_nama_norma_sendiri.GetValue())[0]
            ]
            self.data_norma_sendiri.append(self.datainput)


        self.insertDataNorma.insert_data_sendiri_tabel(self.data_norma_sendiri)   
        self.Close()
    
        pass
    
    def m_button_batal_tabel_normaOnButtonClick(self,event):
        self.Close()
        pass

class BuatNormaSendiriInherited(BuatNormaSendiri):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        pass

    def batal_norma_sendiri(self,event):
        self.Close()

    def lanjut_simpan_norma_sendiri(self,event):
        self.buka_tabel_norma_sendiri = TabelNormaSendiriInherited(self)
        self.buka_tabel_norma_sendiri.Show()
        self.buka_tabel_norma_sendiri.Maximize(True)
        self.Hide()
        self.data_norma = [self.m_nama_norma_sendiri.GetValue(),\
            self.m_keterangan_norma_sendiri.GetValue()]

        pass

class GrafikLayoutInherited(GrafikLayout):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def save_figure(self):
        import pathlib
        self.pathpar = pathlib.Path(__file__).parent
        # print (f"path{self.pathpar}")
        self.path = pathlib.Path(self.pathpar / "reporting" / "image1.png")
        print(self.path)
        print("lewat sini nggak")
        return self.figure.savefig(self.path, dpi='figure')


class GrafikHasilLayoutInherited(GrafikHasil):

    def __init__(self, parent):
        super().__init__(parent)

    def draw(self, nilai_grafik=None):
        self.grafik = nilai_grafik
        print(self.grafik)
        # print (t)
        y = ["Kemampuan\nberhitung", "Daya ingat\ndan konsentrasi", "Kreatifitas",
            "Ketelitian", "Judgement", "Daya\nanalisis", "Pengembalian\nkeputusan", "Kemampuan\n Berbahasa" ]
        self.y = arange(len(y))
        nilai = []
        for value in self.grafik.values():
            print (value)
            nilai.append(int(value))
        print(nilai)
        # x = [130,136,79,125,128,146,128]
        x = nilai
        self.rects = self.axes.barh(y, x, color='green')
        # self.axes.invert_yaxis()
        self.axes.set_xlim(left=50, right=150)
        self.axes.set_yticks(self.y)
        self.axes.set_title("PROFIL KEUNGGULAN IST")
        self.autolabel()

    def save_figure(self):
        import pathlib
        self.pathpar = pathlib.Path(__file__).parent
        self.path = pathlib.Path(self.pathpar / "reporting" / "image2.png")
        print(self.path)
        print("lewat sini nggak")
        return self.figure.savefig(self.path, dpi='figure')


class NormaAllInherited(NormaAll):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.Maximize(True)
        # self.m_dataViewListCtrl3.AppendItem(["1","1","Norma Pekerjaan",""])
        # self.m_dataViewListCtrl3.AppendItem(["2","2","Norma Pendidikan Usia 12 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["3","3","Norma Pendidikan Usia 13 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["4","4","Norma Pendidikan Usia 14 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["5","5","Norma Pendidikan Usia 15 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["6","6","Norma Pendidikan Usia 16 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["7","7","Norma Pendidikan Usia 17 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["8","8","Norma Pendidikan Usia 18 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["9","9","Norma Pendidikan Usia 19 Thn",""])

        # self.data_tarik = TabelNormaSendiriConnect(self.parent.databasekon)
        # self.data_tarik.query_norma_sendiri()

        # self.no = 10
        # for data in self.data_tarik.query_norma_sendiri():
        #     if data[3] == None:
        #         data = list(data)
        #         data.insert(3,"Tidak ada keterangan")
        #         print (data[3])
        #     self.m_dataViewListCtrl3.AppendItem([str(11+data[1]),str(self.no),str(data[2]),str(data[3])])
        #     self.no += 1
        pass

    def m_button_pilih_norma_allOnButtonClick(self, event):
        if self.m_dataViewListCtrl3.GetSelectedRow() == -1:
            self.getV = 0
        else:
            self.getV = self.m_dataViewListCtrl3.GetSelectedRow()
        print(self.m_dataViewListCtrl3.GetStore())
        self.getdata = []

        for data in range(0, 3):
            # print(self.m_dataViewListCtrl3.GetValue(self.getV,1))
            self.getdata.append(self.m_dataViewListCtrl3.GetValue(self.getV, data))

        print(self.getdata)

        if int(self.getdata[0]) == 2 :
            self.tabelumur = 12
        elif int(self.getdata[0]) == 3:
            self.tabelumur = 13
        elif int(self.getdata[0]) == 4:
            self.tabelumur = 13
        elif int(self.getdata[0]) == 5:
            self.tabelumur = 14
        elif int(self.getdata[0]) == 6:
            self.tabelumur = 15
        elif int(self.getdata[0]) == 7:
            self.tabelumur = 16
        elif int(self.getdata[0]) == 8:
            self.tabelumur = 17
        elif int(self.getdata[0]) == 9:
            self.tabelumur = 18
        elif int(self.getdata[0]) == 10:
            self.tabelumur = 19
        elif int(self.getdata[0]) == 11:
            self.tabelumur = 20
        
        else :
            self.tabelumur = "0"
        
        if int(self.getdata[0]) <= 11:
            print (self.getdata[0])
            print ("lewat")
            self.query_data = TableDataKelompokUmurConnect(self.parent.databasekon)
            self.query_data.query_all(self.tabelumur)

        else :
            self.query_data = TabelNormaSendiriConnect(self.parent.databasekon)
            # print (self.query_data)
            self.tabelumur = 15
            print ("kkasdk")
            self.query_data.query_all(self.tabelumur)
            print (self.tabelumur)

        self.lihat_tabel_norma = TabelNormaLihatInherited(self)
        self.lihat_tabel_norma.Maximize()
        self.lihat_tabel_norma.Show()
        for i in range(0, len(self.query_data.query_all(self.tabelumur))):
            self.query_list = list(map(str, self.query_data.query_all(self.tabelumur)[i]))
            self.query_list.insert(0, str(i))
            print (self.query_list)
            self.lihat_tabel_norma.m_dataViewListCtrl4.InsertItem(i, self.query_list)
        return self.getdata

    def m_button_tutup_normaAllOnButtonClick(self, event):
        self.Close()


class NormaInherited(Norma):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.Maximize(True)
        # self.m_dataViewListColumn8.
        # from models.query import SqliteDB
        # self.nama_file = "istcore"
        # self.connect_db = SqliteDB("istcore")
        self.norm_pekerjaan = JenisNorma(self.parent.connect_db)
        self.datanormapekerjaan = self.norm_pekerjaan.select_data_norma_pekerjaan(2)[0]
        self.datanormapekerjaan = [str(x) for x in self.datanormapekerjaan]
        self.datanormapekerjaan.insert(1, "1")
        print(self.datanormapekerjaan)
        self.norm_usia = JenisNorma(self.parent.connect_db)
        self.datanormausia = self.norm_usia.select_data_norma_pendidikan(1)
        self.re_datanormausia = []
        for i in self.datanormausia :
            self.databaru = [str(x) for x in i]
            self.databaru.insert(1, str(self.datanormausia.index(i) + 1))
            self.re_datanormausia.append(self.databaru)

        for data in self.re_datanormausia:
            self.m_dataViewListCtrl8.AppendItem(data)

        self.m_dataViewListCtrl9.AppendItem(self.datanormapekerjaan)
        self.m_dataViewListCtrl3.SetId(188989)


        from models.query import TabelNormaSendiri
        self.run_data = TabelNormaSendiri(self.parent.connect_db)
        self.data = self.run_data.select_data()
        self.data_str =[]

        # ubah data tabel norma sendiri kedalama bentuk string semua
        for data in self.data :
            self.data_str.append([str(self.data.index(data)+1),str(data[0]),str(data[1]),str(data[2]),str(data[3])])

        # menampilkan data tabel sendiri kedalam aplikasi GUI
        for data in self.data_str:
            self.m_dataViewListCtrl3.AppendItem(data)


        # self.m_dataViewListCtrl3.AppendItem(["1","1","Norma Pekerjaan",""])
        # self.m_dataViewListCtrl3.AppendItem(["2","2","Norma Pendidikan Usia 12 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["3","3","Norma Pendidikan Usia 13 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["4","4","Norma Pendidikan Usia 14 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["5","5","Norma Pendidikan Usia 15 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["6","6","Norma Pendidikan Usia 16 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["7","7","Norma Pendidikan Usia 17 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["8","8","Norma Pendidikan Usia 18 Thn",""])
        # self.m_dataViewListCtrl3.AppendItem(["9","9","Norma Pendidikan Usia 19 Thn",""])

        # self.data_tarik = TabelNormaSendiriConnect(self.parent.databasekon)
        # self.data_tarik.query_norma_sendiri()

        # self.no = 10
        # for data in self.data_tarik.query_norma_sendiri():
        #     if data[3] == None:
        #         data = list(data)
        #         data.insert(3,"Tidak ada keterangan")
        #         print (data[3])
        #     self.m_dataViewListCtrl3.AppendItem([str(11+data[1]),str(self.no),str(data[2]),str(data[3])])
        #     self.no += 1
        self.m_button_buat_tabel_norma.Bind(wx.EVT_BUTTON, self.buat_data_peserta)
        self.m_button22.Bind(wx.EVT_BUTTON, self.m_button_pilih_tabel_normaOnButtonClick)
        self.m_button24.Bind(wx.EVT_BUTTON, self.m_button_edit_tabel_normaOnButtonClick)
        self.m_button25.Bind(wx.EVT_BUTTON, self.hapus_data_peserta)
        pass

    def buat_data_peserta(self, event):
        if self.m_dataViewListCtrl8.GetSelectedRow() != -1 or self.m_dataViewListCtrl8.IsShown == True :
            self.getRow = self.m_dataViewListCtrl8.GetSelectedRow()
            self.IdNorma = self.m_dataViewListCtrl8.GetTextValue(self.getRow,0)
            self.buka_norma_sendiri = BuatNormaSendiriInherited(self)
            self.buka_norma_sendiri.Show()

        elif self.m_dataViewListCtrl9.GetSelectedRow() != -1 or self.m_dataViewListCtrl9.IsShown == True :             
            self.getRow = self.m_dataViewListCtrl9.GetSelectedRow()
            self.IdNorma = self.m_dataViewListCtrl9.GetTextValue(self.getRow,0)
            self.buka_norma_sendiri = BuatNormaSendiriInherited(self)
            self.buka_norma_sendiri.Show()

        elif self.m_dataViewListCtrl3.GetSelectedRow() != -1 :
            self.getRow = self.m_dataViewListCtrl3.GetSelectedRow()
            self.IdNorma = self.m_dataViewListCtrl3.GetTextValue(self.getRow,0)
            self.buka_norma_sendiri = BuatNormaSendiriInherited(self)
            self.buka_norma_sendiri.Show()
        
        elif self.m_dataViewListCtrl3.IsShown() == True:
            self.buka_norma_sendiri = BuatNormaSendiriInherited(self)
            self.buka_norma_sendiri.Show()

    

    def m_button_edit_tabel_normaOnButtonClick(self, event):
        if self.m_dataViewListCtrl3.GetSelectedRow() == -1:
            # print ("lewat sini")
            self.getV = 0
        else :
            self.getV = self.m_dataViewListCtrl3.GetSelectedRow()
            # print("kkee")
        self.getdata = []
        
        for data in range(0, 4):
            # print(self.m_dataViewListCtrl3.GetValue(self.getV,1))
            self.getdata.append(self.m_dataViewListCtrl3.GetValue(self.getV, data))

        if int(self.getdata[0]) <= 11:
            # self.buat_baru_norma = 1 ,artinya norma yang diedit dari data 10 kebawah, 
            # mengharuskan norma baru dibuat
            self.buat_baru_norma = 1
        else :
            # self.buat_baru_norma = 0, artinya edit data dari norma yang sudah ada,
            # syaratnya norma bukan bawaan dari aplikasi atau dengan kata lain norma
            # yang bisa di edit adalah norma yang dibuat sendiri
            self.buat_baru_norma = 0

        if self.m_dataViewListCtrl3.GetSelectedRow() != -1:
            self.buka_tabel_norma = TabelNormaInherited(self)
            # method set_data() adalah menyajikan tabel yang sudah ada kedalam gui tabel
            self.buka_tabel_norma.set_data()
            self.buka_tabel_norma.Show()

    def hapus_data_peserta(self, event):
        if self.m_dataViewListCtrl3.GetSelectedRow() != -1:
            self.IdNorma = self.m_dataViewListCtrl3.GetTextValue(\
                self.m_dataViewListCtrl3.GetSelectedRow(),1)
            self.run_data.hapus_data(self.IdNorma)
            self.m_dataViewListCtrl3.DeleteItem(\
                self.m_dataViewListCtrl3.GetSelectedRow())
            self.delete_norma_sendiri = NormaSendiri(self.parent.connect_db)
            self.delete_norma_sendiri.delete(self.IdNorma)
        
    def m_dataViewListCtrl3OnDataViewListCtrlItemActivated(self,event):
        self.m_dataViewListCtrl3.SetId(12345)
        pass

    def m_button_pilih_tabel_normaOnButtonClick(self, event):
        self.parent.pilih = 1
        if self.m_dataViewListCtrl3.GetSelectedRow() != -1:
            self.getRow = self.m_dataViewListCtrl3.GetSelectedRow()
            self.getdata = []
        
            self.getdata.append(self.m_dataViewListCtrl3.GetTextValue(self.getRow, 0))
            self.getdata.append(self.m_dataViewListCtrl3.GetTextValue(self.getRow, 1))
            self.getdata.append(self.m_dataViewListCtrl3.GetTextValue(self.getRow, 2))
            self.getdata.append(self.m_dataViewListCtrl3.GetTextValue(self.getRow, 3))

            self.IdNorma = self.getdata[1]
            self.query_data = NormaSendiri(self.parent.connect_db)
            self.data_norma = self.query_data.query_all(self.IdNorma)

            self.saji_tabel = []
            for data in self.data_norma :
                self.saji_tabel.append(data[0:10])

            print (self.saji_tabel)
            self.parent.LNormaSendiri.SetLabel(self.getdata[2])
    
            pass
            
        elif self.m_dataViewListCtrl8.GetSelectedRow() != -1 :
            self.getRow = self.m_dataViewListCtrl8.GetSelectedRow()
            self.getdata = []
        
            self.getdata.append(self.m_dataViewListCtrl8.GetTextValue(self.getRow, 0))
            self.getdata.append(self.m_dataViewListCtrl8.GetTextValue(self.getRow, 1))
            self.getdata.append(self.m_dataViewListCtrl8.GetTextValue(self.getRow, 2))
            self.getdata.append(self.m_dataViewListCtrl8.GetTextValue(self.getRow, 3))

            self.NormaPendidikanID = self.getdata[1]
            self.query_data = TabelNormaPendidikan(self.parent.connect_db)
            self.data_norma = self.query_data.query(self.NormaPendidikanID)

            self.saji_tabel = []
            for data in self.data_norma :
                self.saji_tabel.append(data[0:10])

            print (self.saji_tabel)
            pass

        elif self.m_dataViewListCtrl9.GetSelectedRow() != -1 :
            self.getRow = self.m_dataViewListCtrl9.GetSelectedRow()
            self.getdata = []
        
            self.getdata.append(self.m_dataViewListCtrl9.GetTextValue(self.getRow, 0))
            self.getdata.append(self.m_dataViewListCtrl9.GetTextValue(self.getRow, 1))
            self.getdata.append(self.m_dataViewListCtrl9.GetTextValue(self.getRow, 2))
            self.getdata.append(self.m_dataViewListCtrl9.GetTextValue(self.getRow, 3))

            self.NormaPekerjaanID = self.getdata[1]
            self.query_data = TabelNormaPekerjaan(self.parent.connect_db)
            
            self.data_norma = self.query_data.query(self.NormaPekerjaanID)

            self.saji_tabel = []
            for data in self.data_norma :
                self.saji_tabel.append(data[0:10])

            print (self.saji_tabel)
            pass

        self.Close()

        return self.getdata, self.data_norma

    def m_button_tutup_normaOnButtonClick(self, event):
        self.Close()

    def m_dataViewListCtrl8OnDataViewListCtrlItemValueChanged(self,event):
        print ("kkk")
        # self.norm_pekerjaan = JenisNorma(self.parent.connect_db)
        # self.datanormapekerjaan = self.norm_pekerjaan.select_data_norma_pekerjaan(2)[0]
        # self.datanormapekerjaan = [str(x) for x in self.datanormapekerjaan]
        # self.datanormapekerjaan.insert(1, "1")
        # print(self.datanormapekerjaan)
        # self.norm_usia = JenisNorma(self.parent.connect_db)
        # self.datanormausia = self.norm_usia.select_data_norma_usia(1)
        # self.re_datanormausia = []
        # for i in self.datanormausia :
        #     self.databaru = [str(x) for x in i]
        #     self.databaru.insert(1, str(self.datanormausia.index(i) + 1))
        #     self.re_datanormausia.append(self.databaru)

        # for data in self.re_datanormausia:
        #     self.m_dataViewListCtrl8.AppendItem(data)
        # self.m_dataViewListCtrl8.GetValue()
        self.value = self.m_dataViewListCtrl8.GetValue(self.m_dataViewListCtrl8.GetSelectedRow(),4)

        self.id = self.m_dataViewListCtrl8.GetValue(self.m_dataViewListCtrl8.GetSelectedRow(),0)

        self.update_norma_pendidikan = TabelNormaPendidikan(self.parent.connect_db)
        self.list_value = [self.value,self.id]
        self.update_norma_pendidikan.insert_data_keterangan(self.list_value)
        # import pdb ; pdb.set_trace()

    def m_dataViewListCtrl9OnDataViewListCtrlItemValueChanged(self,event):
        self.value = self.m_dataViewListCtrl9.GetValue(self.m_dataViewListCtrl9.GetSelectedRow(),3)
        self.id = self.m_dataViewListCtrl9.GetValue(self.m_dataViewListCtrl9.GetSelectedRow(),0)
        self.update_norma_pekerjaan = JenisNorma(self.parent.connect_db)
        self.update_norma_pekerjaan.update_data_norma_pendidikan(self.value,self.id)
        pass

class TabelNormaLihatInherited(TabelNormaLihat):

    def __init__(self, parent):
        super().__init__(parent)
        self.m_button_ok_tabel_norma.SetLabel("Tutup")
 
    def m_button_ok_tabel_norma_all(self, event):
        self.Close()


class TabelNormaInherited(TabelNorma):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.parent.edit berfungsi untuk membedakan antara buat baru dengan edit pada pilihan Tabelnya
        self.parent.edit = 0

        self.Maximize(True)
        no = 1
        for tes in range(33, 0, -1):
            self.m_dataViewListCtrl4.AppendItem([str(no), str(tes), "", "", "", "", "", "", "", "", ""])
            no += 1
        print(self.m_dataViewListCtrl4.GetValue(1, 0))

    def set_data(self):
        # self.parent.edit jika bernilai satu artinya data yang disajikan merupakan editan dari 
        # data yang sudah ada 

        self.parent.edit = 1
        if self.parent.m_dataViewListCtrl3.GetSelectedRow() == -1 :
            self.getV = 0
        else :
            self.getV = self.parent.m_dataViewListCtrl3.GetSelectedRow()
        self.getdata = []
        
        for data in range(0, 4):
            # print(self.m_dataViewListCtrl3.GetValue(self.getV,1))
            self.getdata.append(self.parent.m_dataViewListCtrl3.GetValue(self.getV, data))
        print ("kkasdk")
        print("hhh")
        print (self.getdata[0])
        print ("lewat")
        self.query_data = NormaSendiri(self.parent.parent.connect_db)
        self.data_norma_sendiri = self.query_data.query_all(self.getdata[1])

        # self.lihat_tabel_norma = TabelNormaLihatInherited(self)
        # self.lihat_tabel_norma.Maximize()
        # self.lihat_tabel_norma.Show()
        self.m_dataViewListCtrl4.DeleteAllItems()

        self.data_norma = []
        for i in range(0, len(self.data_norma_sendiri)):
            self.query_list = list(map(str, self.data_norma_sendiri[i]))
            self.query_list.insert(0, str(i+1))
            # self.query_list.insert(11, str(i+1))

            print (self.query_list)
            self.data_norma.append(self.query_list)
            self.m_dataViewListCtrl4.AppendItem(self.query_list)
        # print(self.data_norma)
   

    def m_button_ok_tabel_normaOnButtonClick(self, event):
        if self.parent.edit == 0 :
            self.buka = NamaNormaInherited(self)
            self.buka.Show()
            print ("kesini nggak")
            self.data_norma = []
            for datarow in range(0, self.m_dataViewListCtrl4.GetItemCount()):
                self.col1 = self.m_dataViewListCtrl4.GetValue(datarow, 1)
                self.col2 = self.m_dataViewListCtrl4.GetValue(datarow, 2)
                self.col3 = self.m_dataViewListCtrl4.GetValue(datarow, 3)
                self.col4 = self.m_dataViewListCtrl4.GetValue(datarow, 4)
                self.col5 = self.m_dataViewListCtrl4.GetValue(datarow, 5)
                self.col6 = self.m_dataViewListCtrl4.GetValue(datarow, 6)
                self.col7 = self.m_dataViewListCtrl4.GetValue(datarow, 7)
                self.col8 = self.m_dataViewListCtrl4.GetValue(datarow, 8)
                self.col9 = self.m_dataViewListCtrl4.GetValue(datarow, 9)
                self.col10 = self.m_dataViewListCtrl4.GetValue(datarow, 10)

                self.data_norma.append((self.col1,
                                        self.col2,
                                        self.col3,
                                        self.col4,
                                        self.col5,
                                        self.col6,
                                        self.col7,
                                        self.col8,
                                        self.col9,
                                        self.col10))
            self.data_norma
        else :
            print ("k")
            if self.parent.buat_baru_norma == 1 :
                self.buka = NamaNormaInherited(self)
                self.buka.Show()

            else :
                print("pass")   

                self.Close()    
            print ("ok")

        # self.Close()

    def m_button_batal_tabel_normaOnButtonClick(self, event):
        print ("batal")
        self.Close()

