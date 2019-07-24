import sys
import os
import pathlib
# parent_folder = pathlib.Path.cwd().parent
# chg_folder  = str(pathlib.Path(parent_folder))
# sys.path.append(chg_folder)
# # nama_file = str(pathlib.Path(chg_folder+"/models/ist"))
from models.query import SqliteDB,TabelJawaban

class DatabaseConnect():

    def __init__(self,nama_file):
        self.nama_file = nama_file
        self.db = SqliteDB(self.nama_file)

        pass

    def get_jumlah_baris(self,nama_tabel):
        self.nama_tabel = nama_tabel
        self.jumlah_baris = self.db.hitung_jumlah_row(self.nama_tabel)
        return self.jumlah_baris

    def __repr__(self):
        return self.nama_file

    

class DatabaseBioData(DatabaseConnect):

    def __init__(self,parent):
        super().__init__(parent)


        # print (self.db.query_tabel_data_kelompok())

        # print ("berhasil")
        pass
    
    def __repr__(self):
        return self.nama_file

    def insert_biodata(self,*args):
        # list args[0] = [id_kand,tipe_kandidat,nama_kandidat,tanggal_tes,jenis_kelamin,tanggal_lahir]
        self.data = args
        # print (self.data)
        self.db.insert_tabel_data_kandidat(self.data[0])
        self.get_last_id = self.db.query_data_kandidat()[-1][0]
        self.tipe_kandidat = self.db.query_data_kandidat()[-1][1]
        # print (self.get_last_id)
        # print (self.tipe_kandidat)
        if self.tipe_kandidat == 1 :
            self.data2 = args[1]
            self.data2.insert(0,self.get_last_id)
            # id_kand,no_tes, pendidikan_terakhir,jurusan, kota, perusahaan_instansi,posisi_jabatan       

            # print (self.data2)
            self.db.insert_database_kandidat_tambahan1(self.data2)
        elif self.tipe_kandidat == 2 :
            self.data3 = args[2]
            self.data3.insert(0,self.get_last_id)
            # id_kand,asal_sekolah,jurusan,asal_universitas,jurusan,kota,hoby,prestasi_akademik,prestasi_non_akademik,
            # ekskul yang pernah diikuti
            self.db.insert_database_kandidat_tambahan2(self.data3)
            
        pass

    def lihat_data_kandidat_baru(self):
        self.lihat_data = self.db.query_data_kandidat_leftjoin(self.tipe_kandidat)[-1]

        return self.lihat_data


class DataBaseInput(DatabaseConnect):

    def __init__(self,parent):
        super().__init__(parent)

        self.db = TabelJawaban(self.nama_file)
        pass

    def insert_data_jawaban(self,values):
        self.values = values
        self.db.insert_jawaban(self.values)
        return True
    
    def query_data_jawaban(self,values):

        return True


if __name__ == "__main__":
    # print (pathlib.Path.cwd())
    from models.query import SqliteDB
    nama_file ="ist"
    # print (nama_file)
    run = DatabaseControl(nama_file)
    # [tipe_kandidat,nama_kandidat,tgl tes, jenis kelamin, tanggal lahir]
    data = [2,"Alif","2019/10/23","Laki-Laki","2002/12/04"]
    data2 = [2,3,4,6]
    run.insert_biodata(data,data2)