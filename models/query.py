#! usr/bin/env python

'''
Created on May 4, 2019

@author: ciren
'''
import sys
import pathlib
import sqlite3
import os


class SqliteDB(object):

    def __init__(self, nama_file):
        self.nama_file = nama_file
        print (self.nama_file)
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
        print("Connecting to {}".format(str(self.path_db)))
        print("...Processing....")
        print("Database di buka")
        # import pdb
        # pdb.set_trace()
        conne = sqlite3.connect(str(self.path_db))
        return conne

    def close_db(self):
        print("Berhasil di proses")
        print("Database ditutup")
        return self.conn.close()


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
            # print ("hello")
        
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
            no,
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
        FROM NormaSendiri
        WHERE IdNorma = ?
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

    def delete(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        DELETE FROM NormaSendiri
        WHERE IdNorma = ?;
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
class BidangKeilmuan(SqliteDB):

    def __init__(self,parent):
        super().__init__(parent)

    def query_bidang_keilmuan(self,value=None):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.value = value

        self.sql_cmd = """
        SELECT * FROM [Bidang Keilmuan];        
        """
        self.cursorexe.execute(self.sql_cmd)
        self.data = self.cursorexe.fetchall()
        return self.data

class KonversiGE(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        pass

    def convert_ge(self, values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = str(values)
        # import pdb
        # pdb.set_trace()
        self.sql_cmd = """
        SELECT idGE,
            [No],
            RW,
            GE
        FROM [Konversi GE]
        WHERE RW=?
        """
        self.cursorexe.execute(self.sql_cmd, [self.values, ])
        getdatas = self.cursorexe.fetchone()
        # for data in getdatas:
        #     # print (data)
        #     pass
        self.values = int(self.values)
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

class TabelJawabanNormaSendiri(SqliteDB):


    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

    
    def insert_data(self,values = None):
        self.conn = self.connect_db()
        self.values = values
        self.sql_cmd = """
        INSERT INTO NormaSendiri ([No],RS,SE,WA,AN,GE,RA, zr, FA, WU, ME )
                         VALUES (
                             'No',
                             'RS',
                             'SE',
                             'WA',
                             'AN',
                             'GE',
                             'RA',
                             'ZR',
                             'FA',
                             'WU',
                             'ME',
                             'IdNorma'
                         );
INSERT INTO NormaSendiri (
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
                         )
                         VALUES (
                             'No',
                             'RS',
                             'SE',
                             'WA',
                             'AN',
                             'GE',
                             'RA',
                             'ZR',
                             'FA',
                             'WU',
                             'ME'
                         );


        """
        self.cursorexe.execute(self.sql_cmd,self.values)
        self.conn.commit()
        self.close_db()

class NoTes(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent

    def get_id_test(self,nomor_test):
        self.conn = self.connect_db()

        self.nomor_test = str(nomor_test)

        # self.values = 1
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""Select * from [No Tes] Where [id] = ?"""
        self.cursorexe.execute(self.sql_cmd,[self.nomor_test,])
        self.id_tes = self.cursorexe.fetchone()
        self.conn.close()

        return self.id_tes
    def get_id(self,id_tes):
        self.conn = self.connect_db()

        self.id_tes = str(id_tes)

        # self.values = 1
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""Select * from [No Tes] Where [id_tes] = ?"""
        self.cursorexe.execute(self.sql_cmd,[self.id_tes,])
        self.id = self.cursorexe.fetchone()
        self.conn.close()

        return self.id


    def insert(self,no_tes, id):
        self.conn = self.connect_db()
        self.id = [str(no_tes),int(id)]
        # import pdb
        # pdb.set_trace()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        Insert Into [No Tes] ([No tes],id)
        Values (?,?);
        """
        self.cursorexe.execute(self.sql_cmd,self.id)

        self.conn.commit()
        self.close_db()

class Usia(SqliteDB):

    def __init__(self,parent = None):
        super().__init__(parent)
        self.parent = parent

    def query(self,usia):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.usia=str(usia)
        self.sql_cmd ="""
        SELECT *
        FROM [Usia]
        where usia=?;
        """
        self.cursorexe.execute(self.sql_cmd,[self.usia,])
        self.result = self.cursorexe.fetchone()
        self.close_db()
        return self.result

class NilaiNorma(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent

    def query_by_norma_id(self,values):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values=values

        self.sql_cmd ="""
        SELECT *
        FROM [Nilai Norma]
        where NormaID=?;
        """
        self.cursorexe.execute(self.sql_cmd,[self.values,])
        self.result = self.cursorexe.fetchall()
        self.close_db()
        return self.result

    def update_nilai_norma(self,nilainorma,normaid=None):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.nilainorma = nilainorma
        self.normaid = normaid
        # import pdb
        # pdb.set_trace()
        self.sql_cmd ="""
             UPDATE [Nilai Norma]
               SET 
                   [No] = ?,
                   RS = ?,
                   SE = ?,
                   WA = ?,
                   AN = ?,
                   GE = ?,
                   ME = ?,
                   RA = ?,
                   ZR = ?,
                   FA = ?,
                   WU = ?
             WHERE 
                   NormaID = ? And No = ?;

        """
        for data in self.nilainorma:
            # print (i)
            # import pdb
            # pdb.set_trace()
            data.append(int(data[0]))
            self.cursorexe.execute(self.sql_cmd,data)

        self.lastrowid = self.cursorexe.lastrowid
        self.conn.commit()
        self.close_db()
        return True
        

    def insert_nilai_norma(self,nilainorma):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.nilainorma = nilainorma
        self.sql_cmd ="""
        INSERT INTO [Nilai Norma] (
                              [No],
                              RS,
                              SE,
                              WA,
                              AN,
                              GE,
                              ME,
                              RA,
                              ZR,
                              FA,
                              WU,
                              NormaID
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
        self.cursorexe.executemany(self.sql_cmd,self.nilainorma)
        self.lastrowid = self.cursorexe.lastrowid
        self.conn.commit()
        self.close_db()
        return True

class HasilJawaban(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent

    def insert(self,values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values

        self.sql_cmd = """
        INSERT INTO [Hasil Jawaban] (
                                se,
                                wa,
                                an,
                                ge,
                                ra,
                                zr,
                                fa,
                                wu,
                                me,
                                id_tes
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

        self.conn.execute(self.sql_cmd,self.values)
        self.conn.commit()
        self.close_db()

    def query(self,values=None):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values=values
        self.sql_cmd ="""
        SELECT *
        FROM [Hasil Jawaban]
        where id_tes=?;
        """
        self.cursorexe.execute(self.sql_cmd,self.values)
        self.result = self.cursorexe.fetchone()
        self.close_db()
        return self.result

class InputJawaban(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
    
    def join_table(self,values):
        self.conn = self.connect_db()

        self.values = values
    
        # self.values = 1
        self.nama_tabel = "Kunci Jawaban"
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""
        Select * from "Input Jawaban" 
        Left Join "{}"
        On "Input Jawaban".id_kunci = "Kunci Jawaban".id_kunci
        where "Input Jawaban".id_tes = ?        
        """.format(self.nama_tabel)

        self.sql_cmd ="""Select  
            upper([Input Jawaban].id_input_jawaban),
            upper([Input Jawaban].no),
            upper(replace([Input Jawaban].se,' ','')),
            upper(replace([Input Jawaban].wa,' ','')),
            upper(replace([Input Jawaban].an,' ','')),
            upper(replace([Input Jawaban].ge,' ','')),
            upper(replace([Input Jawaban].ra,' ','')),
            upper(replace([Input Jawaban].zr,' ','')),
            upper(replace([Input Jawaban].fa,' ','')),
            upper(replace([Input Jawaban].wu,' ','')),
            upper(replace([Input Jawaban].me,' ','')),
            upper([Input Jawaban].id_tes),
            upper([Input Jawaban].id_kunci),
            upper([Kunci Jawaban].id_kunci),
            upper([Kunci Jawaban].No),
            upper(replace([Kunci Jawaban].se,' ','')),
            upper(replace([Kunci Jawaban].wa,' ','')),
            upper(replace([Kunci Jawaban].an,' ','')),
            upper(replace([Kunci Jawaban].ge,' ','')),
            upper(replace([Kunci Jawaban].ra,' ','')),
            upper(replace([Kunci Jawaban].zr,' ','')),
            upper(replace([Kunci Jawaban].fa,' ','')),
            upper(replace([Kunci Jawaban].wu,' ','')),
            upper(replace([Kunci Jawaban].me,' ',''))
                    from "Input Jawaban" 
                    Left Join [Kunci Jawaban]
                    On "Input Jawaban".id_kunci = "Kunci Jawaban".id_kunci
                    where "Input Jawaban".id_tes = ?"""        
        # print (self.sql_cmd)

        self.cursorexe.execute(self.sql_cmd,[self.values,])
        self.result = self.cursorexe.fetchall()
        self.close_db()
        return self.result

    def insert_data(self,values = None):
        self.conn = self.connect_db()
        self.values = values
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """ 
        INSERT INTO [Input Jawaban] (
                                [no],
                                se,
                                wa,
                                an,
                                ge,
                                ra,
                                zr,
                                fa,
                                wu,
                                me,
                                id_tes,
                                id_kunci
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
        self.cursorexe.executemany(self.sql_cmd,self.values)
        self.conn.commit()
        self.close_db()


    def show_data(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """SELECT * FROM 'Input Jawaban'"""
        self.result = self.cursorexe.execute(self.sql_cmd).fetchall()
        self.close_db()
        return self.result

    def get_data_by_id(self,values):
        self.values  = values
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """ SELECT * FROM 'Input Jawaban' WHERE id = ?"""
        self.result = self.cursorexe.execute(self.sql_cmd,[self.values,]).fetchall()
        self.close_db()
        return self.result

class KunciJawabanGE(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
        pass

    def query(self , values = None) :
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""
        SELECT id_kunci_ge,
       [No],
       upper(replace(Jawaban,' ','')),
       Nilai
        FROM [Kunci Jawaban GE];"""

        self.getdatas = self.cursorexe.execute(self.sql_cmd).fetchall() #, [self.values,]).fetchall()
        self.close_db()
        return self.getdatas

class TabelNormaPendidikan(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
        pass

    def query(self , values = None) :
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values

        self.sql_cmd ="""
        SELECT *
        FROM NormaPendidikanUSIA
        WHERE NormaPendidikanID = ?
        """

        self.getdatas = self.cursorexe.execute(self.sql_cmd, [self.values,]).fetchall()
        self.close_db()
        return self.getdatas

    def insert_data_keterangan(self,values=None):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        UPDATE [Norma Pendidikan]
        SET Keterangan = ?
        WHERE NormaPendidikanID = ?
        """
        self.cursorexe.execute(self.sql_cmd,(self.values))
        self.conn.commit()        
        self.close_db()

class JumlahTesPerUser(SqliteDB):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
    
    def insert_test(self,*values):
        # value = no test dan nama test
        self.values = values

class TabelNormaSendiri(SqliteDB):

    def __init__(self,parent = None):
        super().__init__(parent)
        self.parent = parent
        pass

    def select_from(self,values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values  = values

        self.sql_cmd = """SELECT IdNorma
        FROM [Norma] 
        WHERE [Nama Norma] = ? ;        """
        self.result = self.cursorexe.execute(self.sql_cmd,(self.values,)).fetchone()
        self.close_db()
        return self.result

    def hapus_data(self,values):
        self.values = values
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        DELETE FROM Norma
        WHERE IdNorma = ?
        
        """
        self.cursorexe.execute(self.sql_cmd,(self.values,))
        self.conn.commit()
        self.close_db()
        

    def select_data(self,values = None):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values  = values

        self.sql_cmd = """SELECT *
        FROM [Norma];        """
        self.result = self.cursorexe.execute(self.sql_cmd).fetchall()
        self.close_db()
        return self.result

    def insert_data(self,values = None):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        INSERT INTO Norma (
                      [Nama Norma],
                      Keterangan,
                      NormaID
                  )
                  VALUES (                      
                      ?,
                      ?,
                      3);
            """
        self.cursorexe.execute(self.sql_cmd,(self.values))
        self.conn.commit()
        self.close_db()

    def insert_data_sendiri_tabel(self,values = None):
        self.conn=self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
            INSERT INTO NormaSendiri (
                             [No],
                             RS,
                             SE,
                             WA,
                             AN,
                             GE,
                             RA,
                             ZR,
                             FA,
                             WU,
                             ME,
                             IdNorma
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
        self.cursorexe.executemany(self.sql_cmd,self.values)
        self.conn.commit()
        self.close_db()


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


# class BidangKeilmuan(SqliteDB):

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         pass
    
#     def __repr__(self):
#         return True
    
#     def query_keilmuan(self, nilai_id):
#         self.id = nilai_id
#         # self.nilai = nilai_rw
#         print(f"ini ada {self.id}")
#         self.conn = self.connect_db()
#         self.cursorexe = self.conn.cursor()
#         self.sql_cmd = """SELECT
#                 fakultas.id,
#                 bidang_keilmuan.bidang_keilmuan,
#                 id_fak,
#                 fakultas.fakultas,
#                 id_jur,
#                 jurusan
#             FROM jurusan
#             LEFT JOIN fakultas
#             ON jurusan.id_fak = fakultas.id_fak 
#             LEFT JOIN bidang_keilmuan
#             ON bidang_keilmuan.id=fakultas.id
#             WHERE jurusan.id_fak=?
#             ;
#                     """

#         self.cursorexe.execute(self.sql_cmd, (self.nilai_total_rw,))
#         self.getdatas = self.cursorexe.fetchall()

#         self.close_db()

#         return self.getdatas


class TabelNormaPekerjaan(SqliteDB) :


    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
    
    def query(self,values = None):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """
        SELECT *
        FROM TabelNormaPekerjaan
        WHERE NormaPekerjaanID = ?
        """
        self.getdatas = self.cursorexe.execute(self.sql_cmd,[self.values,]).fetchall()
        self.close_db()

        return self.getdatas


class JenisNorma(SqliteDB):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def select_all_jenis_norma(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM [Jenis Norma]
        """
        self.cursorexe.execute(self.sql_cmd)
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()
        return self.getdatas
    
    def insert_norma_sendiri(self,norma_sendiri):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.norma_sendiri = norma_sendiri
        
        self.sql_cmd = """
        INSERT INTO [Jenis Norma] (
                              [Jenis Norma],
                              Keterangan,
                              TipeNormaID
                          )
                          VALUES (
                              ?,
                              ?,
                              ?
                          );

        """
        self.cursorexe.execute(self.sql_cmd,self.norma_sendiri)
        self.get_lastrowid = self.cursorexe.lastrowid
        self.conn.commit()
        self.conn.close()
        return 

    def hapus_norma_sendiri(self,norma_id):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.norma_id = int(norma_id)
        
        self.sql_cmd = """
        DELETE FROM [Jenis Norma]
            WHERE NormaID = ?
        """

        self.sql_cmd2 = """
        DELETE FROM [Nilai Norma]
            WHERE NormaID = ?
        """

        self.cursorexe.execute(self.sql_cmd,[self.norma_id,])
        self.cursorexe.execute(self.sql_cmd2,[self.norma_id,])

        self.conn.commit()
        self.close_db()
        return 

    def lastrowid(self):
        return self.get_lastrowid


    def get_data_by_tipenormaid(self,tipenormaid):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.tipenormaid = int(tipenormaid)
        # import pdb
        # pdb.set_trace()
        self.sql_cmd = """
        SELECT *
        FROM [Jenis Norma]
        WHERE [TipeNormaID] = ? ;
        """
        self.cursorexe.execute(self.sql_cmd,[self.tipenormaid,])
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()
        return self.getdatas

    # def get_data_by_lastrowid(self,lastrowid):
    #     self.conn = self.connect_db()
    #     self.cursorexe = self.conn.cursor()
    #     self.tipenormaid = int(tipenormaid)
    #     # import pdb
    #     # pdb.set_trace()
    #     self.sql_cmd = """
    #     SELECT *
    #     FROM [Jenis Norma]
    #     WHERE [NormaID] = ? ;
    #     """
    #     self.cursorexe.execute(self.sql_cmd,[self.tipenormaid,])
    #     self.getdatas = self.cursorexe.fetchall()
    #     self.close_db()


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
            # print (data)
            pass

        self.close_db()
        return self.getdatas
    
    def query_norma_pendidikan(self):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
          FROM [Jenis Norma]
          WHERE NormaID <> 2 And NormaID <=11
          ORDER BY [Jenis Norma] ASC
        ;
        """
        self.cursorexe.execute(self.sql_cmd)
        self.getdatas = self.cursorexe.fetchall()
        self.close_db()
        return self.getdatas


    def querytb_jenisnorma(self, value = None):
        self.nama_norma = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *,
                CASE  
                WHEN [Jenis Norma].[Jenis Norma] = "Norma Pendidikan"
                THEN "Norma Pendidikan"
                WHEN [Jenis Norma].[Jenis Norma] = "Norma Pekerjaan"
                THEN "Norma Pekerjaan"
                ELSE [Norma].[Nama Norma]
                END 
        FROM [Jenis Norma]
        LEFT JOIN 'Norma' ON 'Jenis Norma'.NormaID =  'Norma'.NormaID
        WHERE [Jenis Norma].[Jenis Norma] = '{}'      
        """.format(self.nama_norma)
        self.getdatas = self.cursorexe.execute(self.sql_cmd).fetchall()
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
            # print (data)
            pass

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

class TabelTipeNorma(SqliteDB):

    def __init__(self,parent =None):
        super().__init__(parent)
        self.parent = parent
    
    def query_all(self,value=None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""
        SELECT *
        FROM [Tipe Norma]
        LEFT JOIN 'Jenis Norma' ON 'Jenis Norma'.TipeNormaID =  'Tipe Norma'.TipeNormaID
        """
        getdata = self.cursorexe.execute(self.sql_cmd).fetchall()
        self.close_db()
        return getdata

    def query_all_cond(self,value=None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""
        SELECT *
        FROM [Tipe Norma]
        LEFT JOIN 'Jenis Norma' ON 'Jenis Norma'.TipeNormaID =  'Tipe Norma'.TipeNormaID
        WHERE [Tipe Norma].[Jenis Norma] = ? 
        """
        getdata = self.cursorexe.execute(self.sql_cmd,(self.value,)).fetchall()
        self.close_db()
        return getdata

class Peserta(SqliteDB):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        pass


    def query_select_lj_datapeserta_tipenorma(self,value=None):
        self.value = value
        
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM [Data Peserta]
        LEFT JOIN [Tipe Norma] ON  [Tipe Norma].TipeNormaID=[Data Peserta].TipeNormaID 
        LEFT JOIN [Jenis Norma] ON  [Tipe Norma].TipeNormaID=[Jenis Norma].TipeNormaID
        WHERE id = ?
        """

        getdata = self.cursorexe.execute(self.sql_cmd,(self.value,)).fetchone()
        self.close_db()
        return getdata

    def query_data_peserta(self,value=None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM [Data Peserta];
        """
        getdata = self.cursorexe.execute(self.sql_cmd).fetchall()
        self.close_db()
        return getdata

    def query_data_peserta_byid(self,value=None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM [Data Peserta]
        WHERE id = ?;
        """
        getdata = self.cursorexe.execute(self.sql_cmd,self.value).fetchone()
        self.close_db()
        return getdata


    def query_select_data_peserta(self,value=None):
        self.value = value
        self.conn = self.connect_db()
        self.conn.isolation_level = None
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM [Data Peserta]
        WHERE id =?;
        """
        getdata = self.cursorexe.execute(self.sql_cmd,(self.value,)).fetchone()
        self.close_db()
        return getdata

    def hapus_peserta(self,value = None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()

        self.sql_cmd  = """PRAGMA foreign_keys = ON"""
        self.sql_cmd2 = """
                        DELETE FROM [Data Peserta]
                        WHERE id = ? 
                        """
        self.cursorexe.execute(self.sql_cmd)
        self.cursorexe.execute(self.sql_cmd2,(self.value,))
        self.conn.commit()
        self.close_db()
        return True
    # def hapus_peserta(self,value=None):
    #     self.value = value
    #     self.conn = self.connect_db()
    #     self.cursorexe = self.conn.cursor()

    #     self.sql_cmd = """
    #     SELECT id_tes
    #     FROM [No Tes]
    #     WHERE id = ? ;
    #     """

    #     self.sql_cmd2 ="""
    #     DELETE FROM [Input Jawaban]
    #     WHERE id_tes = ?
    #     """

    #     self.sql_cmd3 = """
    #     DELETE FROM [Hasil Jawaban]
    #     WHERE id_tes = ?;
    #     """

    #     self.sql_cmd4 = """
    #     DELETE FROM [No Tes]
    #     WHERE id = ?;
    #     """

    #     self.sql_cmd5 = """
    #         DELETE FROM [Data Peserta]
    #         WHERE id = ? 
    #     """

    #     self.cursorexe.execute(self.sql_cmd,(self.value,))
    #     self.idtes = self.cursorexe.fetchall()
    #     import itertools
    #     self.idtes = list(itertools.chain.from_iterable(self.idtes))
    #     for idtes in self.idtes:
    #         self.cursorexe.execute(self.sql_cmd2,(idtes,))
    #         self.cursorexe.execute(self.sql_cmd3,(idtes,))

    #     self.cursorexe.execute(self.sql_cmd4,(self.value,))
    #     self.cursorexe.execute(self.sql_cmd5,(self.value,))

    #     self.conn.commit()
    #     self.close_db()
    #     return True

    def edit_peserta(self,value =None):
        self.value = value
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        UPDATE [Data Peserta]
        SET [no tes] = ?,
       [tanggal tes] = ?,
       nama = ?,
       [jenis kelamin] = ?,
       [tanggal lahir] = ?,
       usia = ?,
       [asal sekolah] = ?,
       [pendidikan terakhir] = ?,
       jurusan = ?,
       [posisi pekerjaan] = ?,
       perusahaan = ?,
       keterangan = ?,
       TipeNormaID = ?
        WHERE id = 'id'
        """
        self.cursorexe.execute(self.sql_cmd,self.value)
        self.conn.commit()
        self.close_db()
        return True
       

    def insert_data_peserta(self,**values):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        # dictionary data peserta
        self.key_dict = values
        self.values =[]
        for key,values in self.key_dict.items():
            self.values.append(values)
        # import pdb
        # pdb.set_trace()
        self.sqlcmd = """INSERT INTO [Data Peserta] (
                                [no tes],
                                [tanggal tes],
                                nama,
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
        self.rowid = self.cursorexe.lastrowid
        self.conn.commit()
        self.close_db()
        return self.rowid

    def last_row(self):
        return self.rowid

class Geasamt(SqliteDB):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        pass
    
    def query_by_rts(self,trs,usia):
        self.trs = int(trs)
        self.usia = int(usia)
        if self.trs == 0 :
            self.trs = 1

        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.sql_cmd = """
        SELECT *
        FROM Geasamt
        WHERE "Nilai Total RS" = ? AND id_usia = ?;
        """
        self.cursorexe.execute(self.sql_cmd,[self.trs,self.usia,])
        self.getdata = self.cursorexe.fetchone()
        self.close_db()
        return self.getdata

class Iq(SqliteDB):

    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent
    
    def query_by_geasamt(self,geasamt):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.geasamt = geasamt
        self.sql_cmd = """
        SELECT *
        FROM [NORMA IST IQ]
        WHERE [SW] = ?;
        """
        self.cursorexe.execute(self.sql_cmd,[self.geasamt,])
        self.getdata = self.cursorexe.fetchone()
        self.close_db()
        return self.getdata

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
    # print (tes.get_score(150))
