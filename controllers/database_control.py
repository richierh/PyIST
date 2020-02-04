import sys
import os
import pathlib
# parent_folder = pathlib.Path.cwd().parent
# chg_folder  = str(pathlib.Path(parent_folder))
# sys.path.append(chg_folder)
# # nama_file = str(pathlib.Path(chg_folder+"/models/istcore"))
from models.query import SqliteDB
from numpy import arange, sin, pi


class DatabaseConnect():

    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.db = SqliteDB(self.nama_file)

        pass

    def get_jumlah_baris(self, nama_tabel):
        self.nama_tabel = nama_tabel
        self.jumlah_baris = self.db.hitung_jumlah_row(self.nama_tabel)
        return self.jumlah_baris

    def __repr__(self):
        return self.nama_file


class DatabaseBioData(DatabaseConnect):

    def __init__(self, parent):
        super().__init__(parent)

        # print (self.db.query_tabel_data_kelompok())
        # print ("berhasil")
        pass
    
    def __repr__(self):
        return self.nama_file

    def insert_biodata(self, args):
        # list args[0] = [id_kand,tipe_kandidat,nama_kandidat,tanggal_tes,jenis_kelamin,tanggal_lahir]
        self.data = args
        # print (self.data)
        self.db.insert_tabel_data_kandidat(self.data[0])
        self.get_last_id = self.db.query_data_kandidat()[-1][0]
        self.tipe_kandidat = self.db.query_data_kandidat()[-1][1]
        # print (self.get_last_id)
        # print (self.tipe_kandidat)
        if self.tipe_kandidat == 1:
            self.data2 = args[1]
            self.data2.insert(0, self.get_last_id)
            # id_kand,no_tes, pendidikan_terakhir,
            # jurusan, kota, perusahaan_instansi,posisi_jabatan
            # print (self.data2)
            self.db.insert_database_kandidat_tambahan1(self.data2)
        elif self.tipe_kandidat == 2 :
            self.data3 = args[2]
            self.data3.insert(0, self.get_last_id)
            # id_kand,asal_sekolah,jurusan,asal_universitas,jurusan,kota,hoby,prestasi_akademik,prestasi_non_akademik,
            # ekskul yang pernah diikuti
            self.db.insert_database_kandidat_tambahan2(self.data3)     
        pass

    def lihat_data_kandidat_baru(self):
        self.tipe_kandidat = self.db.query_data_kandidat()[-1][1]

        self.lihat_data = \
            self.db.query_data_kandidat_leftjoin(self.tipe_kandidat)[-1]
        print("hello")

        return self.lihat_data


class PesertaData(DatabaseConnect):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = Peserta(self.nama_file)
        
        pass

    def get_data_peserta(self):
        self.getdata = self.db.select_data()
        return self.getdata


class DataBaseInput(DatabaseConnect):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = TabelJawaban(self.nama_file)
        pass

    def insert_data_jawaban(self, values):
        self.values = values
        self.db.insert_jawaban(self.values)
        return True

    def query_data_jawaban(self, values=None):
        self.query_kunci_jawaban = self.db.query_kunci_jawaban()
        return self.query_kunci_jawaban


class DataKonversiGE(DataBaseInput):

    def __init__(self, parent):
        super().__init__(parent)
        print(f"ini {self.nama_file}")
        self.db = KonversiGE(self.nama_file)

    def konversi_ge(self, values):
        self.values = values
        # print (f"ini nilai GE {self.values}")
        self.nilai_ge = self.db.query_konversi(self.values)

        return self.nilai_ge


class TableDataKelompokUmurConnect(DataKonversiGE):

    def __init__(self, parent, parentarg=None):
        super().__init__(parent)
        self.parent = parent
        self.parent2 = parentarg

        print(f"ini nama {self.nama_file}")
        self.db = TableDataKelompokUmur(self.nama_file)
        # if self.parent
        # self.parent.kelompok_umur

    def query_all(self, kelompok_umur=None):
        self.query = self.db.query_data_all(kelompok_umur)

        return self.query

    def __query_sw(self, kelompok_umur=None):
        self.nilai_sw = \
            self.db.query_data(self.parent2.kelompok_usia, self.parent2)
        return self.nilai_sw

    def get_value_sw(self, input_peserta):
        self.__query_sw()
        print(self.nilai_sw)
        self.inputs = input_peserta
        print(self.inputs)
        c = []
        for input in self.inputs:
            for nilai_sw in self.nilai_sw:
                if input == nilai_sw[0]:
                    print("okay")
                    c.append([input, nilai_sw[self.inputs.index(input) + 1]])
        print(c)
        data_sum_rw = []
        for data in c:
            data_sum_rw.append(data[0])
        data_sum_rw = sum(data_sum_rw)

        return c, data_sum_rw

    def get_geasamt(self, nilai_sum_rw=None):
        self.nilai_sum_rw = nilai_sum_rw
        print(self.nilai_sum_rw)
        data = self.db.query_geasamt(self.nilai_sum_rw)
        data = data[0]
        print(data)
        data_geasamt = []
        if self.parent2.kelompok_usia == 12:
            data_geasamt.append([data[0], data[1]])
        elif self.parent2.kelompok_usia == 13:
            data_geasamt.append([data[0], data[2]])
        elif self.parent2.kelompok_usia == 14:
            data_geasamt.append([data[0], data[3]])
        elif self.parent2.kelompok_usia == 15:
            data_geasamt.append([data[0], data[4]])
        elif self.parent2.kelompok_usia == 16:
            data_geasamt.append([data[0], data[5]])
        elif self.parent2.kelompok_usia == 17:
            data_geasamt.append([data[0], data[6]])
        elif self.parent2.kelompok_usia == 18:
            data_geasamt.append([data[0], data[7]])
        elif self.parent2.kelompok_usia == 19:
            data_geasamt.append([data[0], data[8]])
        return data_geasamt[0][1]

    def get_iq(self, nilai_sw=None):
        self.nilai_sw = nilai_sw
        print(self.nilai_sw)
        data = self.db.query_iq(self.nilai_sw)
        return data[0][1]


class TabelNormaSendiriConnect(TableDataKelompokUmurConnect):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.db = NormaSendiri(self.nama_file)

    def query_norma_sendiri(self):
        self.query = self.db.query_norma_sendiri()
        return self.query

    def query_all(self, values=None):
        print(values)
        self.values = values
        self.query = self.db.query_all(self.values)
        return self.query

    def insert_nama_norma(self, values):
        self.values = values
        self.insert = self.db.insert_norma_sendiri(self.values)

    def delete_nama_norma(self, values):
        self.values = int(values) - 11
        self.delete = self.db.delete_norma_sendiri(self.values)

    def insert_kunci_jawaban_norma(self, values):
        self.values = values
        self.insert = self.db.insert_norma_sendiri_kunci_jaw(self.values)

    def query_last_row(self):
        self.query_last_row = self.db.query_last_row()
        return self.query_last_row


if __name__ == "__main__":
    print(pathlib.Path.cwd())
    nama_file = "istcore.sqlite"
    # print (nama_file)
    run = DatabaseControl(nama_file)
    # [tipe_kandidat,nama_kandidat,tgl tes, jenis kelamin, tanggal lahir]
    data = [2, "Alif", "2019/10/23", "Laki-Laki", "2002/12/04"]
    data2 = [2, 3, 4, 6]
    run.insert_biodata(data, data2)
