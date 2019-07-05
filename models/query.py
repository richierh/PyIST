#! usr/bin/env python

'''
Created on May 4, 2019

@author: cireng
'''
import sys
import pathlib
import sqlite3


class SqliteDB(object):


    def __init__(self,nama_file):
        self.nama_file = nama_file
        self.current_path = pathlib.Path.cwd()/""
        # self.path_db = pathlib.Path(self.current_path.parent/f"models/{self.nama_file}")
        self.path_db = pathlib.Path(self.current_path/f"models/{self.nama_file}")
        print (self.path_db)
        pass
    
    def __repr__(self):

        return self.nama_file
    
    def scrub(self,table_name):
        self.table_name = table_name
        return ''.join( chr for chr in self.table_name if chr.isalnum() )


    def hitung_jumlah_row(self,nama_tabel):
        self.conn = self.connect_db()
        self.values = nama_tabel
        # self.values = self.scrub(self.nama_tabel)
        print (self.values)

        self.sql_cmd =  f"""
        SELECT Count(*) FROM {self.values} 
               """

        self.results = self.conn.execute(self.sql_cmd).fetchone()

        self.close_db()
        return self.results        


    def connect_db(self):
        print ("Connecting to {}.db".format(self.path_db))
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

    def insert_tabel_data_kandidat(self,values):
        self.values=values
        self.conn = self.connect_db()
        self.sql_cmd ="""
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

        self.results = self.conn.executemany(self.sql_cmd,[self.values,])
        self.conn.commit()
        self.close_db()

        return True

    def insert_database_kandidat_tambahan1(self,values):

            self.values=values
            self.conn = self.connect_db()
            self.sql_cmd ="""
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
            self.results = self.conn.executemany(self.sql_cmd,[self.values,])
            self.conn.commit()
            self.close_db()

            return True


    def insert_database_kandidat_tambahan2(self,values):

            self.values=values
            self.conn = self.connect_db()
            self.sql_cmd ="""
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
            self.results = self.conn.executemany(self.sql_cmd,[self.values,])
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

    def query_data_kandidat_leftjoin(self,tipe_kandidat):
        self.conn = self.connect_db()
        self.tipe_kandidat = tipe_kandidat

        if self.tipe_kandidat == 1 :
            sql_cmd = """
            SELECT * 
            FROM data_kandidat
            LEFT JOIN database_kandidat
            ON data_kandidat.id_kand = database_kandidat.id_kand
            ;
    """
        elif self.tipe_kandidat == 2 :
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

class TabelJawaban(SqliteDB):

    def __init__(self,parent):
        super().__init__(parent)
        pass 
    
    def __repr__(self):


        return True

    def insert_jawaban(self,values):
        self.conn = self.connect_db()

        self.values=  values
        self.sql_cmd ="""
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

        self.conn.execute(self.sql_cmd)#,[(self.values,)])
        self.conn.commit()
        self.close_db()
        return True

        



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

    cursorexe.executemany(sql_cmd,values)
    conne.commit()
    conne.close
    print ("insert data done")

def insert_data_peserta(values):
    conne = connect_db()
    cursorexe = conne.cursor()
    
    sqlcmd = """INSERT INTO "Rincian Data Peserta"
(idtipesoal,"No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan")
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);    """
    
    cursorexe.execute(sqlcmd, values)
    conne.commit()
    conne.close()



    
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
#     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
#     values = ["select","select by"]
    print (values[0])
    print (values[1])
    
    if values[0]=="idpeserta":
        sqlcmd = """SELECT I.idinputpeserta,I.idpeserta,RDP."Nama Kandidat",I.NoSoal,I.JawabanPeserta,T.NamaSoal
            FROM Input_Data_Jawaban_Peserta AS I
            LEFT JOIN TipeSoal as T ON I.idTipeSoal = T.idTipeSoal
            LEFT JOIN "Rincian Data Peserta" as RDP ON RDP.idpeserta = I.idpeserta
            WHERE I.idpeserta = ?
            """
    
        cursorexe.execute(sqlcmd,(values[1],))
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
        print (data)
    
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
    cursorexe.execute(sqlcmd,(nilai,))
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
    print (values[0])
    print (values[1])
    
    if values[0]=="idpeserta":
        sqlcmd = """SELECT I.idinputpeserta,I.idpeserta,I.NoSoal,I.JawabanPeserta,
            T.NamaSoal,
            RDP."No Tes",RDP."Tanggal Tes",RDP."Nama Kandidat",RDP."Jenis Kelamin",
            RDP."Tanggal Lahir",RDP."Pendidikan Terakhir",RDP."Jurusan Pendidikan",
            RDP."Kota",RDP."Perusahaan / Instansi",RDP."Posisi / Jabatan"
            
            FROM Input_Data_Jawaban_Peserta AS I
            LEFT JOIN TipeSoal as T ON I.idTipeSoal = T.idTipeSoal
            LEFT JOIN "Rincian Data Peserta" as RDP ON RDP.idpeserta = I.idpeserta
            WHERE I.idpeserta = ?
            """
    
        cursorexe.execute(sqlcmd,(values[1],))
    getdatas = cursorexe.fetchall()
    datas = []
    for data in getdatas:
        datas.append(data)
    
    conne.close
    return datas    
    


def query_tabel_data_peserta(value):
    conne = connect_db()
    
    print (value[0],value[1],value[2],value[3])
    print ("ini value {},{},{},{}".format(value[0],value[1],value[2],value[3]))
    cursorexe = conne.cursor()
    
    if value[4]=="nama orang":
        sql_cmd = """
    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
    FROM "Rincian Data Peserta" 
    WHERE "Nama Kandidat" LIKE ?;
    """
        cursorexe.execute(sql_cmd,(("{}%".format(value[0]),)))

    elif value[4] == "no tes":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "No Tes" = ?;
                """
        cursorexe.execute(sql_cmd,((value[1],)))
    
    elif value[4]=="tanggal":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "Tanggal Tes" BETWEEN ? AND ?;
                """
        cursorexe.execute(sql_cmd,((value[2],value[3])))

    elif value[4] == "idpeserta":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "idpeserta" = ?;
                """
        cursorexe.execute(sql_cmd,((value[0 ],)))


    getdatas = cursorexe.fetchall()
    data_list = []
    for data in getdatas:
        data_list.append(data)
    conne.close
    
    return data_list

def hapus_data_rincian_peserta(values):
    conne = connect_db()
    
    cursorexe= conne.cursor()
    sql_cmd ="""DELETE FROM "Rincian Data Peserta"
WHERE idpeserta=?;
    """
    cursorexe.execute(sql_cmd,(values),)
    conne.commit()
    conne.close
    
def hapus_data_input_peserta(values):
    conne = connect_db()
    
    cursorexe= conne.cursor()
    sql_cmd ="""DELETE FROM "Input_Data_Jawaban_Peserta"
WHERE idpeserta=?;
    """
    cursorexe.execute(sql_cmd,(values),)
    conne.commit()
    conne.close


def update_jawaban(values,id_pes):
#     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
#     values = ["select","select by"]
    print (values[0])
    print (values[1])
    print (values[2])

    sql_cmd = """
    UPDATE Input_Data_Jawaban_Peserta 
    SET JawabanPeserta = ?
    WHERE NoSoal = ? AND IdPeserta=?;
    """
    cursorexe.execute(sql_cmd,(values[2],values[1],id_pes))
    conne.commit()
    conne.close


def update_rincian_data_peserta(values,id_pes):
#     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
#     values = ["select","select by"]
    print(values[0])
    print(values[1])
    print(values[2])

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
# #     print (path)
# #     connect_db(path)
# #     values = [(1,1,1,2,1),(1,1,1,1,1)]
# #     insert_input_peserta(values)
#     query_tabel_data_peserta("OFI SUNASTRI")
#     print(query_tabel_data_peserta("OFI SUNASTRI"))
    
if __name__=="__main__" :
    file_db = "ist"
    connect_db = SqliteDB(file_db)
    # connect_db.query_tabel_data_kelompok()[1]
    rw = 19
    ceks = connect_db.query_tabel_data_kelompok()
    for cek in ceks:
        if rw == cek[0]:
            print(f"berhasil : {cek[2]}")