'''
Created on Feb 15, 2019

@author: binakarir
'''
import wx
import pathlib
from shutil import copyfile

from controllers.grafik_tabel import *
from controllers.halaman_event import HalamanEventControl
from views.menubar_tentang import TentangAplikasiInherited
from views.buka_filter_db import FrameFilterDatabase
from views.dialog_save import DialogSavePDF
from views.istcore import TabelDataPeserta,Biodata,TipeNorma,PilihInput
from controllers.halaman_event import PilihTabelInherited
from models.query import Peserta,TabelTipeNorma,JenisNorma


class BukaFilter(FrameFilterDatabase):
    "this is class inherited from buka_filter_db.py"

    def __init__(self, parent):
        super().__init__(parent)
    
    def m_buttonFilterBatalOnButtonClick(self, event):
        print ("klik batal")
        self.Close()
    
    def m_buttonKlikFilterNoTesOnButtonClick(self, event):
        print ("click by no test")
    
    def m_buttonKlikFilterOrangOnButtonClick(self, event):
        print("click by person name")

    def m_buttonKlikFilterTanggalOnButtonClick(self, event):
        print ("click by tanggal")

class BuatBiodata(Biodata):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        self.Tpendidikan_terakhir.AppendItems(["SD","SMP","SMA","D3","S1","S2","S3"])    
        self.Tpendidikan_terakhir.SetSelection(4)


        self.tanggal_tes.Show()
        self.tanggal_lahir.Show()
        self.usia.Show()
        self.jenis_kelamin.Show()
        self.Tpendidikan_terakhir.Show()

        
        self.m_textCtrl_tanggal_tes1.Hide()
        self.m_textCtrl_tanggal_lahir1.Hide()
        self.m_textCtrl_usia1.Hide()
        self.m_textCtrl_jenis_kelamin1.Hide()
        self.m_textCtrl_pendidikan_terakhir1.Hide()
        


    def m_lanjut_biodataOnClick(self,event):

        self.datapeserta = [self.m_textCtrl_no_tes1.GetValue(),
        self.tanggal_tes.GetValue().Format("%d/%m/%Y"),
        self.m_textCtrl_nama1.GetValue(),
        self.jenis_kelamin.GetStringSelection(),
        self.tanggal_lahir.GetValue().Format("%d/%m/%Y"),
        self.m_textCtrl_usia1.GetValue(),
        self.m_textCtrl_asal_sekolah_universitas.GetValue(),
        self.Tpendidikan_terakhir.GetStringSelection(),
        self.m_textCtrl_jurusan.GetValue(),
        self.m_textCtrl_posisi_pekerjaan.GetValue(),
        self.m_textCtrl_perusahaan.GetValue(),
        self.m_textCtrl_keterangan.GetValue(),
        1]

        self.bio = self.parent.data_peserta.insert_data_peserta(self.datapeserta)
        self.data_peserta = Peserta(self.parent.parent.connect_db)
        self.data_list =[]
        self.parent.m_dataViewListCtrl3.DeleteAllItems()
        for data in self.parent.data_peserta.query_data_peserta():
            index =  self.parent.data_peserta.query_data_peserta().index(data)+1
            self.data_list.append([str(index),str(data[0]),str(data[3]),str(data[12])])
        for data in self.data_list:
            self.parent.m_dataViewListCtrl3.AppendItem(data)
        # Buka jendela input kunci jawaban 
        self.buka_input = PilihInputInherited(self)
        self.buka_input.Show()
        pass

    def m_tutup_biodata(self,event):
        self.Close()
        pass

class PilihInputInherited(PilihInput):


    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.Hide()
    
    def pilih_input_manual(self, event):


        pass

    def pilih_input_total(self, event):
        pass

class EditBiodata(Biodata):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        self.Tpendidikan_terakhir.AppendItems(["SD","SMP","SMA","D3","S1","S2","S3"])    
        self.Tpendidikan_terakhir.SetSelection(4)

        self.tanggal_tes.Show()
        self.tanggal_lahir.Show()
        self.usia.Show()
        self.jenis_kelamin.Show()
        self.Tpendidikan_terakhir.Show()

        self.m_textCtrl_tanggal_tes1.Hide()
        self.m_textCtrl_tanggal_lahir1.Hide()
        self.m_textCtrl_usia1.Hide()
        self.m_textCtrl_jenis_kelamin1.Hide()
        self.m_textCtrl_pendidikan_terakhir1.Hide()

        self.m_textCtrl_no_tes1.SetValue(str(self.parent.bio[1]))
        self.tanggal_tes.SetValue(self.parent.date)
        self.m_textCtrl_nama1.SetValue(str(self.parent.bio[3]))
        self.jenis_kelamin.SetStringSelection(str(self.parent.bio[4]))
        self.tanggal_lahir.SetValue(self.parent.date2)
        self.m_textCtrl_usia1.SetValue(str(self.parent.bio[6]))
        self.m_textCtrl_asal_sekolah_universitas.SetValue(str(self.parent.bio[7]))
        self.Tpendidikan_terakhir.SetStringSelection(str(self.parent.bio[8]))
        self.m_textCtrl_jurusan.SetValue(str(self.parent.bio[9]))
        self.m_textCtrl_posisi_pekerjaan.SetValue(str(self.parent.bio[10]))
        self.m_textCtrl_perusahaan.SetValue(str(self.parent.bio[11]))
        self.m_textCtrl_keterangan.SetValue(str(self.parent.bio[12]))

    def m_lanjut_biodataOnClick(self,event):
        self.Hide()

        self.m_textCtrl_no_tes1.GetValue()
        self.tanggal_tes.GetValue().Format("%d/%m/%Y")
        self.m_textCtrl_nama1.GetValue()
        self.jenis_kelamin.GetStringSelection()
        self.tanggal_lahir.GetValue().Format("%d/%m/%Y")
        self.m_textCtrl_usia1.GetValue()
        self.m_textCtrl_asal_sekolah_universitas.GetValue()
        self.Tpendidikan_terakhir.GetStringSelection()
        self.m_textCtrl_jurusan.GetValue()
        self.m_textCtrl_posisi_pekerjaan.GetValue()
        self.m_textCtrl_perusahaan.GetValue()
        self.m_textCtrl_keterangan.GetValue()

        self.window_editnorma = TipeNormaInherited(self)
        self.window_editnorma.Show()

 
        pass

    def m_tutup_biodata(self,event):
        self.Close()
        pass


class TipeNormaInherited(TipeNorma):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.connect_db = self.parent.parent.parent.connect_db
        self.tabledb_tipenorma=TabelTipeNorma(self.connect_db)
        self.tabledb_jenisnorma = JenisNorma(self.connect_db)
        self.m_choice4.Disable()
        self.m_choice5.Disable()


        # Setting data di m_choice default
        self.tipenorma = []
        for data in self.tabledb_tipenorma.query_all():
            self.tipenorma.append(data[1])
        self.m_choice3.AppendItems(self.tipenorma)

        self.jenisnorma = []
        for data in self.tabledb_jenisnorma.select_all_jenis_norma():
            self.jenisnorma.append(data[1])
        self.m_choice4.AppendItems(self.jenisnorma)
        self.m_choice5.AppendItems(["",""])
        self.__edit_data()


    def __edit_data(self):
        self.id_peserta = self.parent.parent.bio[0]
        print (self.parent.parent.bio)
        self.data_peserta_q =self.parent.parent.data_peserta.query_select_lj_datapeserta_tipenorma(self.id_peserta)
        print (self.data_peserta_q)
        self.data_norma = []
        self.data_norma.append([self.data_peserta_q[15],self.data_peserta_q[17]])
        print(self.data_norma)


    def m_tipe_norma_event(self,event):
        self.tipenorma = self.m_choice3.GetStringSelection()
        self.tabledb_tipenorma.query_all_cond(self.tipenorma)
        self.m_choice4.Enable()

        print ("hello")
        self.indexdata = []
        self.indexdata.append(self.m_choice4.GetCount())
        for data in reversed(range(self.indexdata[0])):
            self.m_choice4.Delete(data)

        self.jenisnorma = []
        for data in self.tabledb_tipenorma.query_all_cond(self.tipenorma):
            self.jenisnorma.append(data[3])
        self.m_choice4.AppendItems(self.jenisnorma)
        self.m_choice5.Disable()
        pass

    def m_jenisnorma_event(self,event):
        self.jenisnorma = self.m_choice4.GetStringSelection()
        self.tabledb_jenisnorma.querytb_jenisnorma(self.jenisnorma)
        self.m_choice5.Enable()
        print ("hello")
        self.indexdata = []
        self.indexdata.append(self.m_choice5.GetCount())
        for data in reversed(range(self.indexdata[0])):
            # self.m_choice4.SetSelection(data)
            self.m_choice5.Delete(data)
        self.jenis_norma = []
        for data in self.tabledb_jenisnorma.querytb_jenisnorma(self.jenisnorma):
            self.jenis_norma.append(data[8])
        self.m_choice5.AppendItems(self.jenis_norma)
        pass
    
    def m_batal_tipe_normaOnButtonClick(self,event):
        self.Close()
        self.parent.Close()
        pass

    def m_simpan_tipe_normaOnButtonClick(self,event):
        self.Close()
        self.parent.Close()
        pass

class TabelDataPesertaIn(TabelDataPeserta):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        
        self.data_peserta = Peserta(self.parent.connect_db)
        self.data_list =[]
        for data in self.data_peserta.query_data_peserta():
            index =  self.data_peserta.query_data_peserta().index(data)+1
            self.data_list.append([str(index),str(data[0]),str(data[3]),str(data[12])])
        for data in self.data_list:
            self.m_dataViewListCtrl3.AppendItem(data)
        pass    


    def tutup_data_peserta(self, event):
        self.Close()
        pass

    def buat_data_peserta(self, event):
        print ("hello")
        self.biodata = BuatBiodata(self)
        self.biodata.Show()


    def hapus_data_peserta(self, event):
        print ("hello")
        if self.m_dataViewListCtrl3.GetSelectedRow() != -1:
            self.data = self.m_dataViewListCtrl3.GetValue(self.m_dataViewListCtrl3.GetSelectedRow(),1)

            self.m_dataViewListCtrl3.DeleteItem(self.m_dataViewListCtrl3.GetSelectedRow())
            # print(self.data)
            self.data_peserta.hapus_peserta(self.data)
        pass

    def edit_data_peserta(self, event) :
        if self.m_dataViewListCtrl3.GetSelectedRow() != -1:
            
            self.data = self.m_dataViewListCtrl3.GetValue(self.m_dataViewListCtrl3.GetSelectedRow(),1)
            self.bio = self.data_peserta.query_select_data_peserta(self.data)
            self.day,self.month,self.year = self.bio[2].split("/")
            self.day2,self.month2,self.year2 = self.bio[5].split("/")

            self.date = wx.DateTimeFromDMY(int(self.day),int(self.month)-1,int(self.year))  
            self.date2 = wx.DateTimeFromDMY(int(self.day2),int(self.month2)-1,int(self.year2))  

            self.biodata = EditBiodata(self)
            self.biodata.Show()

            # self.data =[]
            # for i in range(9):
            #     self.data.append(self.m_dataViewListCtrl3.GetValue(self.m_dataViewListCtrl3.GetSelectedRow(),i))

            # print(self.data)
            # self.data_peserta.(self.data)
       
        
        # self.Close()
        pass

class MenuBarInherited(HalamanEventControl):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def m_menu_keluarOnMenuSelection(self, event):
        self.Close()
        event.Skip()

    def m_menu_bantuanOnMenuSelection(self, event):
        self.TentangAplikasi = TentangAplikasiInherited(self)
        self.TentangAplikasi.Show()
        event.Skip()

    def m_menuItem_daftar_tabel_normaOnMenuSelection(self, event):
        print('buka menu item')

        self.pilih_tabel = PilihTabelInherited(self)
        self.pilih_tabel.Show()

        # jangan dihapus 
        # self.buka_tabel_norma = NormaInherited(self)
        # self.buka_tabel_norma.Show() 

    # def m_menuItem_lihat_tabel_normaOnMenuSelection(self, event):
    #     # self.buka_tabel_norma = NormaInherited(self)
    #     # self.buka_tabel_norma.Show()
    #     # self.buka_jendela_norma.Close()
    #     self.buka_jendela_norma = NormaInherited(self)
    #     self.buka_jendela_norma.Show()

    #     print('buka lihat tabel')

    def menubar_lihat_data_peserta(self, event):
        self.lihat_data_peserta = TabelDataPesertaIn(self)
        self.lihat_data_peserta.Show()
        self.lihat_data_peserta.Maximize()

class PropertiesInput(MenuBarInherited):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def get_biodata(self):
        # menentukan tipe_biodata yang dipilih , apakah pendidikan ataukah pekerjaan
        # self.tipe_biodata = 1 adalah tipe pendidikan , self.tipe_biodata =2 adalah tipe pekerjaan
        self.tipe_biodata = 0
        print("tes")

        self.biodata = [self.parent.m_textCtrl_no_tes.GetValue(),
        self.parent.m_datePicker_tanggal_tes1.GetValue().Format("%d/%m/%Y"),
        self.parent.m_textCtrl_nama.GetValue(),
        self.parent.m_choice_jenis_kelamin.GetString(self.parent.m_choice_jenis_kelamin.GetSelection()),
        self.parent.m_datePicker_tanggal_lahir.GetValue().Format("%d/%m/%Y"),
        self.parent.m_spinCtrl_usia.GetValue(),
        self.parent.m_textCtrl_asal_sekolah_universitas.GetValue(),
        self.parent.m_choice_pendidikan_terakhir1.GetString(self.parent.m_choice_pendidikan_terakhir1.GetSelection()),
        self.parent.m_textCtrl_jurusan.GetValue(),
        self.parent.m_textCtrl_posisi_pekerjaan.GetValue(),
        self.parent.m_textCtrl_perusahaan.GetValue(),
        self.parent.m_textCtrl_keterangan.GetValue()
        ]
        self.biodata_dict = {"No Tes":self.biodata[0],
        "Tanggal Tes":self.biodata[1],
        "Nama":self.biodata[2],
        "Jenis Kelamin":self.biodata[3],
        "Tanggal Lahir" : self.biodata[4],
        "Usia":self.biodata[5],
        "Asal Sekolah" : self.biodata[6],
        "Pendidikan Terakhir":self.biodata[7],
        "Jurusan":self.biodata[8],
        "Posisi Pekerjaan":self.biodata[9],
        "Perusahaan":self.biodata[10],
        "Keterangan":self.biodata[11]
        }
        # import pdb
        # pdb.set_trace()
        return self.biodata,self.biodata_dict

    def set_biodata_to_panel(self):
        
        pass

class BukaDialogSimpanPDF(DialogSavePDF):

    def __init__(self, parent):
        super().__init__(parent)

    def m_button_simpanPDFFile(self, event):
        print ("simpan pdf")
        # path = pathlib.Path()
        self.src = pathlib.Path.cwd()  # /"controllers/reporting/tuto1d.pdf"
        self.src = self.src.parents[0] / "controllers/reporting/tuto1d.pdf"
        print (self.src)
        self.simpan_file_pdf = str(pathlib.Path(self.m_direktori_pdf.GetPath() + "/" + self.m_filepdf.GetValue() + ".pdf"))
        copyfile(self.src, self.simpan_file_pdf)
        self.Close()

        event.Skip()

    def m_button_batal_simpanPDF(self, event):
        print ("close")
        self.Close()
        event.Skip()
    
    def m_button_cek_validitas_input(self, event):
        print("cek validitas")
        print (self.panggilgrid.getdata())

        event.Skip()

class ISTInheritedProperties(PropertiesInput):
    
    def __init__(self, parent, *args, **kwds):
        super().__init__(parent, *args, **kwds)
        self.parent = parent

    def totalse(self):
        self.se = []
        for se in self.list_se:
            self.se.append(se.GetValue())
        return self.se

    def totalwa(self):
        self.wa = []
        for wa in self.list_wa:
            self.wa.append(wa.GetValue())
        return self.wa

    def totalan(self):
        self.an = []
        for an in self.list_an:
            self.an.append(an.GetValue())
        return self.an

    def totalge(self):
        self.ge = []
        for ge in self.list_ge:
            self.ge.append(ge.GetValue())
        return self.an

    def totalra(self):
        self.ra = []
        for ra in self.list_ra:
            self.ra.append(ra.GetValue())
        return self.ra

    def totalzr(self):
        self.zr = []
        for zr in self.list_zr:
            self.zr.append(zr.GetValue())
        return self.zr

    def totalfa(self):
        self.fa = []
        for fa in self.list_fa:
            self.fa.append(fa.GetValue())
        return self.fa

    def totalwu(self):
        self.wu = []
        for wu in self.list_wu:
            self.wu.append(wu.GetValue())
        return self.wu

    def totalme(self):
        self.me = []
        for me in self.list_me:
            self.me.append(me.GetValue())
        return self.me

    def totalinputse(self):
        
        return self.m_textCtrl47.GetValue()

    def totalinputwa(self):

       return self.m_textCtrl48.GetValue()

    def totalinputan(self):
 
       return self.m_textCtrl481.GetValue()

    def totalinputge(self):

        return self.m_textCtrl73.GetValue()

    def totalinputra(self):
        return self.m_textCtrl181.GetValue()

    def totalinputzr(self):
 
        return self.m_textCtrl196.GetValue()

    def totalinputfa(self):

        return self.m_textCtrl484.GetValue()

    def totalinputwu(self):
 
        return self.m_textCtrl484.GetValue()

    def totalinputme(self):
        
        return self.m_textCtrl486.GetValue()

    # def biodata(self):
    #     # Ini adalah object untuk tarik data
    #     print ("lewat sini tak")
    #     return self.m_textCtrl_nama, self.m_textCtrlNomor, \
    #         self.m_textCtrlUsia, self.m_textCtrlKelas, \
    #         self.m_textCtrlAsalSekolah

    def m_textCtrl_namaOnLeftUp(self, event):
        event.Skip()

    def m_buttonInput_JawabanOnButtonClick(self, event):
        event.Skip()

    def m_textCtrl6OnText(self, event):
        event.Skip()

    def m_textCtrl47OnText(self, event):
        event.Skip()

    def m_textCtrl7OnText(self, event):
        event.Skip()

    def m_textCtrl48OnText(self, event):
        event.Skip()

    def m_textCtrl71OnText(self, event):
        event.Skip()

    def m_textCtrl481OnText(self, event):
        event.Skip()

    def m_textCtrl303OnText(self, event):
        event.Skip()

    def m_textCtrl181OnText(self, event):
        event.Skip()

    def m_textCtrl100OnText(self, event):
        event.Skip()

    def m_textCtrl196OnText(self, event):
        event.Skip()

    def m_textCtrl74OnText(self, event):
        event.Skip()

    def m_textCtrl484OnText(self, event):
        event.Skip()

    def m_textCtrl75OnText(self, event):
        event.Skip()

    def m_textCtrl485OnText(self, event):
        event.Skip()

    def m_textCtrl76OnText(self, event):
        event.Skip()

    def m_textCtrl486OnText(self, event):
        event.Skip()

    def m_button6OnButtonClick(self, event):
        event.Skip()

    def m_button_hapus_onclick(self, event):
        print ("hapus data")
        event.Skip()

    def m_button_filter_onclick(self, event):
        print ("you have click 'Filter'")
        self.openfilter = BukaFilter(self)
        self.openfilter.Show()
        event.Skip()

    def m_button_lihat_dari_database_onclick(self, event):
        print ("lihat dari database")

        self.run = DatabaseBioData(self.connect_db)
        print (self.run.lihat_data_kandidat_baru())

    def m_button_reset_onclick(self, event):
        print ("bersihkan data")
        event.Skip()

    def m_button_save_as_pdfOnButtonClick(self, event):
        print("save to pdf file")
        self.a = BukaDialogSimpanPDF(self)
        self.a.Show()

    def m_button_print_pdfOnButtonClick(self, event):
        print("print pdf file")
    
    def m_button_simpanOnButtonClick(self, event):
        print ("simpan hasil")

    def m_button_reset_1OnButtonClick(self, event):
        print ("reset halaman 4 ")


if __name__ == '__main__':
    run = ListControlProperties(None)
    # print (run.list_an)