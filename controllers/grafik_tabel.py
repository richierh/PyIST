import wx
from numpy import arange, sin, pi

from views.grafik_ist import GrafikLayout, GrafikHasil, GrafikProfesi
from views.istcore import Norma, TabelNorma, FrameRow, NormaAll, TabelNormaLihat
from controllers.nama_norma_inherited import NamaNormaInherited
from controllers.warning_inherited import WarningFrameInherited
from models.query import JenisNorma


class GrafikLayoutInherited(GrafikLayout):

    def __init__(self, parent):
        super().__init__(parent)

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
        self.m_button_buat_tabel_norma.Bind(wx.EVT_BUTTON, self.m_button_buat_tabel_normaOnButtonClick)
        self.m_button22.Bind(wx.EVT_BUTTON, self.m_button_pilih_tabel_normaOnButtonClick)
        self.m_button24.Bind(wx.EVT_BUTTON, self.m_button_edit_tabel_normaOnButtonClick)
        self.m_button25.Bind(wx.EVT_BUTTON, self.m_button_hapus_tabel_normaOnButtonClick)
        pass

    def m_button_buat_tabel_normaOnButtonClick(self, event):
        # self.buka_row = FrameRowInherited(self)
        # self.buka_row.Show()
        # self.buat_baru_norma = 1
        self.buka_tabel_norma = TabelNormaInherited(self)
        self.buka_tabel_norma.Show()
        pass

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

        self.buka_tabel_norma = TabelNormaInherited(self)
        # method set_data() adalah menyajikan tabel yang sudah ada kedalam gui tabel
        self.buka_tabel_norma.set_data()
        self.buka_tabel_norma.Show()

    def m_button_hapus_tabel_normaOnButtonClick(self, event):
        # self.m_dataViewListCtrl3.GetSelectedRow() == -1 apabila tidak ada yang dipilih
        if self.m_dataViewListCtrl3.GetSelectedRow() == -1:
            print ("lewat sini")
            self.getV = 0
        else :
            self.getV = self.m_dataViewListCtrl3.GetSelectedRow()
        self.getdata = []
        
        for data in range(0, 3):
            # print(self.m_dataViewListCtrl3.GetValue(self.getV,1))
            self.getdata.append(self.m_dataViewListCtrl3.GetValue(self.getV, data))

        if self.m_dataViewListCtrl3.GetSelectedRow() == -1:
            pass
        elif int(self.getdata[0]) <= 11 :
            # data tidak bisa dihapus
            self.warning = WarningFrameInherited(self)
            self.warning.Show()
        else :
            # Menghapus data di tabel GUI
            self.m_dataViewListCtrl3.DeleteItem(self.getV)
            self.tabel_norma_sendiri = TabelNormaSendiriConnect(self.parent.databasekon)
            self.tabel_norma_sendiri.delete_nama_norma(self.getdata[0])
            pass

    def m_button_pilih_tabel_normaOnButtonClick(self, event):
        self.parent.pilih = 1
        if self.m_dataViewListCtrl3.GetSelectedRow() == -1:
            print ("lewat sini")
            self.getV = int(self.m_dataViewListCtrl3.GetSelectedRow()) + 1
        else :
            self.getV = self.m_dataViewListCtrl3.GetSelectedRow()
        self.getdata = []
        
        for data in range(0, 3):
            # print(self.m_dataViewListCtrl3.GetValue(self.getV,1))
            self.getdata.append(self.m_dataViewListCtrl3.GetValue(self.getV, data))
        # print (self.getdata)
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
            self.tabelumur = 3
            print ("kkasdk")
            self.query_data.query_all(self.tabelumur)
            print (self.tabelumur)

        # self.lihat_tabel_norma = TabelNormaLihatInherited(self)
        # self.lihat_tabel_norma.Maximize()
        # self.lihat_tabel_norma.Show()
        self.data_norma = []
        for i in range(0, len(self.query_data.query_all(self.tabelumur))):
            self.query_list = list(map(str, self.query_data.query_all(self.tabelumur)[i]))
            self.query_list.insert(0, str(i))
            print (self.query_list)
            self.data_norma.append(self.query_list)
            # self.lihat_tabel_norma.m_dataViewListCtrl4.InsertItem(i,self.query_list)
        # print(self.data_norma)
        self.parent.m_staticText_pilih_norma_sendir.SetLabel(self.getdata[2])
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

        self.update_norma_pendidikan = JenisNorma(self.parent.connect_db)
        self.update_norma_pendidikan.update_data_norma_pendidikan(self.value,self.id)
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
        for tes in range(20, 0, -1):
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

        # print (self.getdata)
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
        print("hhh")
        if int(self.getdata[0]) <= 11:
            print (self.getdata[0])
            print ("lewat")
            self.query_data = TableDataKelompokUmurConnect(self.parent.parent.databasekon)
            self.query_data.query_all(self.tabelumur)

        else :
            print ("kkasdk")

            self.query_data = TabelNormaSendiriConnect(self.parent.parent.databasekon)
            # print (self.query_data)
            self.tabelumur = '0'
            self.query_data.query_all(self.tabelumur)
            print (self.tabelumur)

        # self.lihat_tabel_norma = TabelNormaLihatInherited(self)
        # self.lihat_tabel_norma.Maximize()
        # self.lihat_tabel_norma.Show()
        self.m_dataViewListCtrl4.DeleteAllItems()

        self.data_norma = []
        for i in range(0, len(self.query_data.query_all(self.tabelumur))):
            self.query_list = list(map(str, self.query_data.query_all(self.tabelumur)[i]))
            self.query_list.insert(0, str(i))
            print (self.query_list)
            self.data_norma.append(self.query_list)
            self.m_dataViewListCtrl4.AppendItem(self.query_list)
        # print(self.data_norma)
   
        print(self.m_dataViewListCtrl4.GetValue(1, 0))        

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
