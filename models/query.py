#! usr/bin/env python

'''
Created on May 4, 2019

@author: cireng
'''
import sys
import pathlib
import sqlite3
import os


class SqliteDB(object):

    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.current_path = pathlib.Path.cwd() / ""
        self.path_db = pathlib.\
            Path(self.current_path.parent / f"models/{self.nama_file}")
        # # self.path_db = 
        # pathlib.Path(self.current_path/f"models/{self.nama_file}")
        # print(self.path_db)
        # self.path_db = self.nama_file
        pass

    def __repr__(self):

        return self.nama_file

    def scrub(self, table_name):
        self.table_name = table_name
        return ''.join(chr for chr in self.table_name if chr.isalnum())

    def hitung_jumlah_row(self, nama_tabel):
        self.conn = self.connect_db()
        self.values = nama_tabel
        # self.values = self.scrub(self.nama_tabel)
        # print (self.values)

        self.sql_cmd = """
        SELECT Count(*) FROM '{}'
               """.format(self.values)

        self.results = self.conn.execute(self.sql_cmd).fetchone()

        self.close_db()
        return self.results

    def connect_db(self):
        print("Connecting to {}.db".format(self.path_db))
        print("...Processing....")
        print("Database di buka")
        conne = sqlite3.connect(str(self.path_db))
        return conne

    def close_db(self):
        print("Berhasil di proses")
        print("Database ditutup")
        return self.conn.close()

    def query_tabel_data_kelompok(self) :
        self.conn = self.connect_db()
        sql_cmd = """
        SELECT TableDataKelompokUmur12.* ,
            TableDataKelompokUmur13.* ,
            TableDataKelompokUmur14.* ,
            TableDataKelompokUmur15.* ,
            TableDataKelompokUmur16.* ,
            TableDataKelompokUmur17.* ,
            TableDataKelompokUmur18.* ,
            TableDataKelompokUmur19.*

        FROM TableDataKelompokUmur12
        LEFT JOIN TableDataKelompokUmur13 ,TableDataKelompokUmur14 , TableDataKelompokUmur15 ,
                TableDataKelompokUmur16 ,TableDataKelompokUmur17 , TableDataKelompokUmur18 , 
                TableDataKelompokUmur19

        ON TableDataKelompokUmur12.RW = TableDataKelompokUmur13.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur14.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur15.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur16.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur17.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur18.RW
        AND TableDataKelompokUmur12.RW = TableDataKelompokUmur19.RW
         """
        self.results = self.conn.execute(sql_cmd).fetchall()
        self.close_db()

        return self.results

    def insert_tabel_data_kandidat(self, values):
        self.values = values
        self.conn = self.connect_db()
        self.sql_cmd = """
        INSERT INTO data_kandidat (
                              tipe_kandidat,
                              nama_kandidat,
                              tanggal_tes,
                              jenis_kelamin,
                              tanggal_lahir
                          )
                          VALUES (
                              ?,
                              ?,
                              ?,
                              ?,
                              ?
                          );

        """

        self.results = self.conn.executemany(self.sql_cmd, [self.values, ])
        self.conn.commit()
        self.close_db()

        return True

    def insert_database_kandidat_tambahan1(self, values):
            self.values = values
            self.conn = self.connect_db()
            self.sql_cmd = """
            INSERT INTO database_kandidat (
                                  id_kand,
                                  no_tes,
                                  pendidikan_terakhir,
                                  jurusan,
                                  kota,
                                  perusahaan_instansi,
                                  posisi_jabatan
                              )
                              VALUES (
                                  ?,
                                  ?,
                                  ?,
                                  ?,
                                  ?,
                                  ?,
                                  ?
                              );

            """
            self.results = self.conn.executemany(self.sql_cmd, [self.values, ])
            self.conn.commit()
            self.close_db()

            return True

    def insert_database_kandidat_tambahan2(self, values):

            self.values = values
            self.conn = self.connect_db()
            self.sql_cmd = """
            INSERT INTO database_kandidat_2 (
                                    id_kand,
                                    asal_sekolah,
                                    jurusan_sekolah,
                                    asal_universitas,
                                    jurusan_universitas,
                                    kota,
                                    hobi,
                                    prestasi_akademik,
                                    prestasi_non_akademik,
                                    ekskul_yang_diikuti
                                )
                                VALUES (
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?
                                );
            """
            self.results = self.conn.executemany(self.sql_cmd, [self.values, ])
            self.conn.commit()
            self.close_db()

            return True

    def query_data_kandidat(self):
        self.conn = self.connect_db()
        sql_cmd = """
        SELECT id_kand,
            tipe_kandidat,
            nama_kandidat,
            tanggal_tes,
            jenis_kelamin,
            tanggal_lahir
        FROM data_kandidat;

        """
        self.results = self.conn.execute(sql_cmd).fetchall()
        self.close_db()

        return self.results

    def query_data_kandidat_leftjoin(self, tipe_kandidat, filter="None"):
        self.filter = filter
        print(self.filter)
        self.conn = self.connect_db()
        self.tipe_kandidat = tipe_kandidat

        if self.tipe_kandidat == 1:
            sql_cmd = """
            SELECT *
            FROM data_kandidat
            LEFT JOIN database_kandidat
            ON data_kandidat.id_kand = database_kandidat.id_kand
            ;
            """
        elif self.tipe_kandidat == 2:
            sql_cmd = """
            SELECT *
            FROM data_kandidat
            LEFT JOIN database_kandidat_2
            ON data_kandidat.id_kand = database_kandidat_2.id_kand
            ;
    """

        self.results = self.conn.execute(sql_cmd).fetchall()
        self.close_db()

        return self.results


class NormaSarjana(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def get_score(self, value):
        self.value = [str(value), str(value)]
        # self.value = [str(2),str(2)]
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *,SUBSTR(SE,-3)
        FROM NormaSarjana
        WHERE 
        SUBSTR(SE,1,3) <= ? AND SUBSTR(SE,-3) >= ?
        """
        getdata = self.cursorexe.execute(self.sql_cmd, self.value).fetchone()
        self.close_db()
        return getdata


class DataPeserta(SqliteDB) :
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def insert_data_peserta(self, value):

        self.value = [str(value), str(value)]
        # self.value = [str(2),str(2)]
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *,SUBSTR(SE,-3)
        FROM NormaSarjana
        WHERE 
        SUBSTR(SE,1,3) <= ? AND SUBSTR(SE,-3) >= ?
        """
        getdata = self.cursorexe.execute(self.sql_cmd, self.value).fetchone()
        self.close_db()
        return getdata


class NormaSendiri(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def query_last_row(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
SELECT id_norma
FROM norma_sendiri ORDER BY id_norma DESC LIMIT 1
        """
        getdata = self.cursorexe.execute(self.sql_cmd).fetchone()
        if getdata is None:
            getdata = (1,)
            print ("hello")
        
        self.close_db()
        return getdata[0]

    def query_norma_sendiri(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM norma_sendiri;
        """
        self.cursorexe.execute(self.sql_cmd)
        getdatas = self.cursorexe.fetchall()
        # for data in getdatas:
        #     # print (data)
        #     pass
        self.close_db()
        print(getdatas)
        return getdatas

    def query_all(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        print(self.values)
        print("leeeee")
        self.sql_cmd = """
        SELECT
            rs,
            se,
            wa,
            an,
            ge,
            ra,
            zr,
            fa,
            wu,
            me
        FROM norma_sendiri_kunci
        LEFT JOIN norma_sendiri
        ON norma_sendiri.id_norma = norma_sendiri_kunci.id_norma
        WHERE norma_sendiri.id_norma = ?
                ;
        """
        self.cursorexe.execute(self.sql_cmd, [self.values, ])
        getdatas = self.cursorexe.fetchall()
        # for data in getdatas:
        #     # print (data)
        #     pass
        self.close_db()
        print(getdatas)
        return getdatas

    def insert_norma_sendiri(self, values):

        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        INSERT INTO norma_sendiri (
                                    [no],
                                    nama_norma,
                                    keterangan
                                )
                                VALUES (
                                    (SELECT [no] FROM norma_sendiri ORDER BY no DESC LIMIT 1)+1,
                                    ?,
                                    ?
                                )
        """
        self.cursorexe.execute(self.sql_cmd, self.values)
        # for data in getdatas:
        #     # print (data)
        #     pass
        self.conn.commit()
        self.close_db()
        # print(getdatas)
        return True

    def delete_norma_sendiri(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        DELETE FROM norma_sendiri
        WHERE "no" = ?
        """
        self.cursorexe.execute(self.sql_cmd, (self.values,))
        self.conn.commit()
        self.close_db()
        return True

    def insert_norma_sendiri_kunci_jaw(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        INSERT INTO norma_sendiri_kunci (
                                            [no],
                                            rs,
                                            se,
                                            wa,
                                            an,
                                            ge,
                                            ra,
                                            zr,
                                            fa,
                                            wu,
                                            me,
                                            id_norma
                                        )
                                        VALUES (
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?
                                        );
        """
        self.cursorexe.executemany(self.sql_cmd, self.values)
        self.conn.commit()
        self.close_db()
        return True


class KonversiGE(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        pass

    def query_konversi(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        SELECT idGE,No,RW,GE
        FROM 'Konversi GE'
        WHERE RW=?
        """
        self.cursorexe.execute(self.sql_cmd, [self.values, ])
        getdatas = self.cursorexe.fetchone()
        # for data in getdatas:
        #     # print (data)
        #     pass
        self.close_db()
        if self.values > 32:
            getdatas = [33, 33, 33, 20]

        elif self.values is None:
            getdatas = [33, 33, 33, 0]

        print(getdatas)
        return getdatas


class TabelJawaban(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        pass

    def __repr__(self):
        return True

    def insert_jawaban(self, values):
        self.conn = self.connect_db()

        self.values = values
        self.sql_cmd = """
        INSERT INTO jawaban_peserta (   
                                id_kand,
                                id_input_ke,
                                id_kunci_jawaban,
                                no_jawaban,
                                jawaban_peserta_se,
                                kunci_jawaban_peserta_se,
                                jawaban_peserta_wa,
                                kunci_jawaban_wa,
                                jawaban_peserta_an,
                                kunci_jawaban_peserta_an,
                                jawaban_peserta_ge,
                                jawaban_peserta_ra,
                                kunci_jawaban_ra,
                                jawaban_peserta_zr,
                                kunci_jawaban_peserta_zr,
                                jawaba_peserta_fa,
                                kunci_jawaban_peserta_fa,
                                jawaban_peserta_wu,
                                kunci_jawaban_peserta_wu,
                                jawaban_peserta_me,
                                kunci_jawaban_peserta_me
                            )
        VALUES ((SELECT id_kand FROM data_kandidat ORDER BY id_kand DESC LIMIT 1),1,
            1,(SELECT "Id Kunci Jawaban" FROM "Kunci Jawaban" WHERE No = 1),'jawaban_peserta_se','kunci_jawaban_peserta_se','jawaban_peserta_wa',
            'kunci_jawaban_wa','jawaban_peserta_an','kunci_jawaban_peserta_an','jawaban_peserta_ge',
            'jawaban_peserta_ra','kunci_jawaban_ra','jawaban_peserta_zr','kunci_jawaban_peserta_zr',
            'jawaba_peserta_fa','kunci_jawaban_peserta_fa','jawaban_peserta_wu','kunci_jawaban_peserta_wu',
            'jawaban_peserta_me','kunci_jawaban_peserta_me') ;
        """

        self.conn.execute(self.sql_cmd)
        self.conn.commit()
        self.close_db()

    def query_kunci_jawaban(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT "Id Kunci Jawaban", No, SE, WA, AN, GE, RA, ZR, FA, WU, ME 
        FROM "Kunci Jawaban";
        """
        self.cursorexe.execute(self.sql_cmd)
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()
        return self.getdatas

class InputJawaban(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
    
    def insert_data(self,values = None):
        self.conn = self.connect_db()
        self.values = values

        self.sql_cmd = """ INSERT INTO [Input Jawaban] (
                                TipeInputId,
                                id,
                                SE,
                                WA,
                                AN,
                                GE,
                                RA,
                                ZR,
                                FA,
                                WU,
                                ME,KSE,KWA,KAN,KGE,KRA,KZR,KFA,KWU,KME
                            )
                            VALUES ((SELECT TipeInputId  FROM [Tipe Input] WHERE [Jenis Input] = ?),(SELECT id FROM [Data Peserta] WHERE [no tes] = ?),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); """

        self.conn.executemany(self.sql_cmd,self.values)
        self.conn.commit()
        self.close_db()



class TableDataKelompokUmur(SqliteDB):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        pass

    def __repr__(self):
        return True

    def insert_jawaban(self, values):
        self.conn = self.connect_db()

        self.values = values
        self.sql_cmd = """ tes """

        self.conn.execute(self.sql_cmd)
        self.conn.commit()
        self.close_db()
        return True

    def query_data(self, kelompok_umur=None, parent=None):
        self.kelompok_umur = kelompok_umur
        # self.nilai = nilai_rw
        self.parent = parent
        self.parent.tipe_biodata

        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()

        if self.parent.tipe_biodata == 0:

            if self.kelompok_umur == 12:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur12;
                """

            elif self.kelompok_umur == 13:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur13;
                """

            elif self.kelompok_umur == 14:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur14;
                """

            elif self.kelompok_umur == 15:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur15;
                """

            elif self.kelompok_umur == 16:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur16;
                """

            elif self.kelompok_umur == 17:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur17;
                """

            elif self.kelompok_umur == 18:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur18;
                """

            elif self.kelompok_umur == 19:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur19;
                """

        elif self.parent.tipe_biodata == 2:
                self.sql_cmd = """
                SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
                FROM TableDataKelompokUmur19;
                """

        else:
            pass

        self.cursorexe.execute(self.sql_cmd)  # ,[(self.values,)])
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()

        return self.getdatas

    def query_data_all(self, kelompok_umur=None, parent=None):
        self.kelompok_umur = kelompok_umur
        # self.nilai = nilai_rw
        self.parent = parent

        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()

        if self.kelompok_umur == 12:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur12;
            """

        elif self.kelompok_umur == 13:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur13;
            """

        elif self.kelompok_umur == 14:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur14;
            """

        elif self.kelompok_umur == 15:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur15;
            """

        elif self.kelompok_umur == 16:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur16;
            """

        elif self.kelompok_umur == 17:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur17;
            """

        elif self.kelompok_umur == 18:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur18;
            """

        elif self.kelompok_umur == 19:
            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur19;
            """

        else :

            self.sql_cmd = """
            SELECT RW, SE, WA, AN, GE, ME, RA, ZR, FA, WU
            FROM TableDataKelompokUmur19;
            """
            pass

        self.cursorexe.execute(self.sql_cmd)  # ,[(self.values,)])
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()

        return self.getdatas

    def query_geasamt(self, nilai_total_rw=None):
        self.nilai_total_rw = nilai_total_rw
        # self.nilai = nilai_rw
        print(f"ini ada {self.nilai_total_rw}")
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """SELECT Range,
            Gesamt12,
            Gesamt13,
            Gesamt14,
            Gesamt15,
            Gesamt16,
            Gesamt17,
            Gesamt18,
            Gesamt19
        FROM TabelDataGesamt
        WHERE Range=?;
                """

        self.cursorexe.execute(self.sql_cmd, (self.nilai_total_rw,))
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()
        return self.getdatas

    def query_iq(self, nilai_geasamt=None):
        self.nilai_geasamt = nilai_geasamt
        # self.nilai = nilai_rw
        print(f"ini ada {self.nilai_geasamt}")
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """SELECT SW,
                IQ
            FROM [Nilai IQ]
            WHERE SW=?;
                    """

        self.cursorexe.execute(self.sql_cmd, (self.nilai_geasamt,))
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()

        return self.getdatas


class BidangKeilmuan(SqliteDB):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        pass
    
    def __repr__(self):
        return True
    
    def query_keilmuan(self, nilai_id):
        self.id = nilai_id
        # self.nilai = nilai_rw
        print(f"ini ada {self.id}")
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """SELECT
                fakultas.id,
                bidang_keilmuan.bidang_keilmuan,
                id_fak,
                fakultas.fakultas,
                id_jur,
                jurusan
            FROM jurusan
            LEFT JOIN fakultas
            ON jurusan.id_fak = fakultas.id_fak 
            LEFT JOIN bidang_keilmuan
            ON bidang_keilmuan.id=fakultas.id
            WHERE jurusan.id_fak=?
            ;
                    """

        self.cursorexe.execute(self.sql_cmd, (self.nilai_total_rw,))
        self.getdatas = self.cursorexe.fetchall()

        self.close_db()

        return self.getdatas



class JenisNorma(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def select_data_norma_pekerjaan(self, id):
        self.id = str(id)
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT NormaID,
        [Jenis Norma],
        [Keterangan],
        TipeNormaID
        FROM [Jenis Norma]
        WHERE NormaID = ?;
        """
        self.cursorexe.execute(self.sql_cmd, self.id)
        self.getdatas = self.cursorexe.fetchall()
        for data in self.getdatas:
            print (data)

        self.close_db()
        return self.getdatas
    
    def select_data_norma_pendidikan(self, id):
        self.id = str(id)
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT [Norma Pendidikan].NormaPendidikanID,
            [Norma Pendidikan]."Nama Norma",
            [Norma Pendidikan].Usia,
            [Norma Pendidikan].Keterangan
        FROM [Jenis Norma]
        LEFT JOIN  [Norma Pendidikan] ON [Norma Pendidikan].NormaID = [Jenis Norma].NormaID
        WHERE [Norma Pendidikan].NormaID = ?;       
        """
        self.cursorexe.execute(self.sql_cmd, self.id)
        self.getdatas = self.cursorexe.fetchall()
        for data in self.getdatas:
            print (data)

        self.close_db()
        return self.getdatas        

    def update_data_norma_pendidikan(self,value,id):
        self.value = value
        self.id = str(id)

        self.conn = self.connect_db()

        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        UPDATE [Norma Pendidikan]
        SET Keterangan = ?
        WHERE  NormaPendidikanID = ?;
        """
        self.cursorexe.execute(self.sql_cmd,[self.value,self.id])
        self.conn.commit()
        self.close_db()
        # import pdb ; pdb.set_trace()

        return True

    def update_data_norma_pendidikan(self,value,id):
        self.value = value
        self.id = str(id)

        self.conn = self.connect_db()

        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        UPDATE [Jenis Norma]
        SET Keterangan = ?
        WHERE NormaID = ? ;
        """
        self.cursorexe.execute(self.sql_cmd,[self.value,self.id])
        self.conn.commit()
        self.close_db()
        # import pdb ; pdb.set_trace()

        return True

class Peserta(SqliteDB):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        pass

    def select_data(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT id_kand,
            "nomor peserta",
            "tanggal tes",
            "nama peserta",
            "jenis kelamin",
            "tanggal lahir",
            "usia",
            "asal sekolah",
            "pendidikan terakhir",
            "jurusan",
            "posisi pekerjaan",
            "perusahaan"
        FROM data_peserta;

        """
        self.cursorexe.execute(self.sql_cmd)
        self.getdatas = self.cursorexe.fetchall()
        for data in self.getdatas:
            print (data)

        self.close_db()
        return self.getdatas

    def insert_data_peserta(self,values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values

        self.sqlcmd = """INSERT INTO [Data Peserta] (
                                [no tes],
                                nama,
                                [tanggal tes],
                                [jenis kelamin],
                                [tanggal lahir],
                                usia,
                                [asal sekolah],
                                [pendidikan terakhir],
                                jurusan,
                                [posisi pekerjaan],
                                perusahaan,
                                keterangan,
                                TipeNormaID
                            )
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?
                            );
        """

        self.cursorexe.execute(self.sqlcmd, self.values)
        self.conn.commit()
        self.close_db()


def insert_input_peserta(values):
    conne = connect_db()
    cursorexe = conne.cursor()
    sql_cmd = """
    INSERT INTO Input_Data_Jawaban_Peserta
    (NoSoal, JawabanPeserta, idTipeSoal, idpeserta, idDimensi)
    VALUES(?,?,?, (SELECT idpeserta
                    from 'Rincian Data Peserta'
                    order by idpeserta
                    DESC limit 1), ?);
    """

    cursorexe.executemany(sql_cmd, values)
    conne.commit()
    conne.close
    print("insert data done")




def cek_id_peserta_terakhir():
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """SELECT idpeserta
                from 'Rincian Data Peserta'
                order by idpeserta
                DESC limit 1"""
    cursorexe.execute(sqlcmd)
    getid = cursorexe.fetchone()
#     print (getid[0])
    conne.close()
    return getid[0]


def query_input_peserta(values):
    # Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    #     values = ["select","select by"]
    # print (values[0])
    # print (values[1])

    if values[0] == "idpeserta":
        sqlcmd = """SELECT I.idinputpeserta,I.idpeserta,RDP."Nama Kandidat",I.NoSoal,I.JawabanPeserta,T.NamaSoal
            FROM Input_Data_Jawaban_Peserta AS I
            LEFT JOIN TipeSoal as T ON I.idTipeSoal = T.idTipeSoal
            LEFT JOIN "Rincian Data Peserta" as RDP ON RDP.idpeserta = I.idpeserta
            WHERE I.idpeserta = ?
            """

        cursorexe.execute(sqlcmd, (values[1],))
    getdatas = cursorexe.fetchall()
    datas = []
    for data in getdatas:
        datas.append(data)

    conne.close
    return datas

    # SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
    # FROM "Rincian Data Peserta"
    # WHERE idpeserta = 2 ;


def query_data_peserta():
    #     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """SELECT I.idinputpeserta ,
                I.NoSoal,I.JawabanPeserta,T.NamaSoal 
                FROM Input_data_Jawaban_Peserta AS I
                LEFT JOIN TipeSoal as T ON I.idTipeSoal \
                =T.idTipeSoal"""
    cursorexe.execute(sqlcmd)
    getdatas = cursorexe.fetchall()
    for data in getdatas:
        # print (data)
        pass

    conne.close


def query_referensi_dimensi():
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """SELECT* FROM 'Referensi Dimensi'
    """
    cursorexe.execute(sqlcmd)
    getdatas = cursorexe.fetchall()
    #     for data in getdatas:
    #         print (data)

    conne.close
    return getdatas


def query_kamus(nilai):
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """
    SELECT [No], Dimensi, Referensi
    FROM Kamus
    WHERE Dimensi = ? ;
    """
    cursorexe.execute(sqlcmd, (nilai,))
    getdatas = cursorexe.fetchone()
    #     for data in getdatas:
    #         print (data)

    conne.close
    return getdatas


def query_data_jawaban(values):
    #     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    #     values = ["select","select by"]
    # print (values[0])
    # print (values[1])

    if values[0] == "idpeserta":
        sqlcmd = """SELECT I.idinputpeserta,I.idpeserta,I.NoSoal,I.JawabanPeserta,
            T.NamaSoal,
            RDP."No Tes",RDP."Tanggal Tes",RDP."Nama Kandidat",
            RDP."Jenis Kelamin",
            RDP."Tanggal Lahir",RDP."Pendidikan Terakhir",RDP."
            Jurusan Pendidikan",
            RDP."Kota",RDP."Perusahaan / Instansi",RDP."Posisi / Jabatan"

            FROM Input_Data_Jawaban_Peserta AS I
            LEFT JOIN TipeSoal as T ON I.idTipeSoal = T.idTipeSoal
            LEFT JOIN "Rincian Data Peserta" as
            RDP ON RDP.idpeserta = I.idpeserta
            WHERE I.idpeserta = ?
            """

        cursorexe.execute(sqlcmd, (values[1],))
    getdatas = cursorexe.fetchall()
    datas = []
    for data in getdatas:
        datas.append(data)

    conne.close
    return datas


def query_tabel_data_peserta(value):
    conne = connect_db()

    # print (value[0],value[1],value[2],value[3])
    # print ("ini value {},{},{},{}".format(value[0],value[1],value[2],value[3]))
    cursorexe = conne.cursor()

    if value[4] == "nama orang":
        sql_cmd = """
        SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes",
         "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan 
         Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi",
          "Posisi / Jabatan"
        FROM "Rincian Data Peserta"
        WHERE "Nama Kandidat" LIKE ?;
        """
        cursorexe.execute(sql_cmd, (("{}%".format(value[0]),)))

    elif value[4] == "no tes":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta"
                    WHERE "No Tes" = ?;
                """
        cursorexe.execute(sql_cmd, ((value[1],)))

    elif value[4] == "tanggal":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "Tanggal Tes" BETWEEN ? AND ?;
                """
        cursorexe.execute(sql_cmd, ((value[2], value[3])))

    elif value[4] == "idpeserta":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "idpeserta" = ?;
                """
        cursorexe.execute(sql_cmd, ((value[0],)))

    getdatas = cursorexe.fetchall()
    data_list = []
    for data in getdatas:
        data_list.append(data)
    conne.close

    return data_list


def hapus_data_rincian_peserta(values):
    conne = connect_db()

    cursorexe = conne.cursor()
    sql_cmd = """DELETE FROM "Rincian Data Peserta"
    WHERE idpeserta=?;
        """
    cursorexe.execute(sql_cmd, (values),)
    conne.commit()
    conne.close


def hapus_data_input_peserta(values):
    conne = connect_db()

    cursorexe = conne.cursor()
    sql_cmd = """DELETE FROM "Input_Data_Jawaban_Peserta"
        WHERE idpeserta=?;
     """
    cursorexe.execute(sql_cmd, (values),)
    conne.commit()
    conne.close


def update_jawaban(values, id_pes):
    #     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    #     values = ["select","select by"]
    # print (values[0])
    # print (values[1])
    # print (values[2])

    sql_cmd = """
    UPDATE Input_Data_Jawaban_Peserta
    SET JawabanPeserta = ?
    WHERE NoSoal = ? AND IdPeserta=?;
    """
    cursorexe.execute(sql_cmd, (values[2], values[1], id_pes))
    conne.commit()
    conne.close


def update_rincian_data_peserta(values, id_pes):
    #     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    #     values = ["select","select by"]
    # print(values[0])
    # print(values[1])
    # print(values[2])

    sql_cmd = """
    UPDATE [Rincian Data Peserta]
    SET [No Tes] = ? ,
        [Tanggal Tes] = ?,
        [Nama Kandidat] = ?,
        [Jenis Kelamin] = ?,
        [Tanggal Lahir] = ?,
        [Pendidikan Terakhir] = ?,
        [Jurusan Pendidikan] = ?,
        Kota = ?,
        [Perusahaan / Instansi] = ?,
        [Posisi / Jabatan] = ?
    WHERE idpeserta = ?    
    """
    cursorexe.execute(sql_cmd, (*values,
                                id_pes))
    conne.commit()
    conne.close

# if __name__ == "__main__":

#     path = pathlib.Path.cwd() / "hexacodb"
#     print (path)
#     connect_db(path)
#     values = [(1,1,1,2,1),(1,1,1,1,1)]
#     insert_input_peserta(values)
#     query_tabel_data_peserta("OFI SUNASTRI")
#     print(query_tabel_data_peserta("OFI SUNASTRI"))


if __name__ == "__main__":
    file_db = "istcore"
    connect_db = SqliteDB(file_db)
    # connect_db.query_tabel_data_kelompok()[1]
    # rw = 19
    # ceks = connect_db.query_tabel_data_kelompok()
    # for cek in ceks:
    #     if rw == cek[0]:
    #         # print(f"berhasil : {cek[2]}")
    #         pass
    tes = NormaSarjana(connect_db)
    print (tes.get_score(150))
