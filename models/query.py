#! usr/bin/env python

'''
Created on May 4, 2019

@author: cireng
'''

import pathlib
import sqlite3

global path

def connect_db():
    
    path = pathlib.Path.cwd() / "models/ist"
#     path = pathlib.Path.cwd() / "hexacodb"
    print (path)

    print ("Connecting to {}".format(path))
    print("...Processing....")
    conne = sqlite3.connect(str(path))
    return conne

def path():
    pathl = pathlib.Path.cwd() / "models/hexacodb"
    return pathl

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

    

if __name__ == "__main__":
    
    path = pathlib.Path.cwd() / "hexacodb"
#     print (path)
#     connect_db(path)
#     values = [(1,1,1,2,1),(1,1,1,1,1)]
#     insert_input_peserta(values)
    query_tabel_data_peserta("OFI SUNASTRI")
    print(query_tabel_data_peserta("OFI SUNASTRI"))
    
    
    