import numpy as np
import pandas as pd
import sqlite3


class InputJawaban():

    def __init__(self,parent=None):
        self.parent = parent
    
    def join_table(self,values):
        self.conn = sqlite3.connect("/home/cireng/Projects/pyist/models/istcore.sqlite")
        # import pdb
        # pdb.set_trace()
        self.values = str(values)
        # self.values = 1
        self.nama_tabel = "Kunci Jawaban"
        self.cursorexe = self.conn.cursor()
        self.sql_cmd ="""
        Select * from "Input Jawaban" 
        Left Join "{}"
        On "Input Jawaban".id_kunci = "Kunci Jawaban".id_kunci
        where "Input Jawaban".id_tes = ?        
        """.format(self.nama_tabel)
        # print (self.sql_cmd)
        self.cursorexe.execute(self.sql_cmd,self.values)
        self.result = self.cursorexe.fetchall()
        self.conn.close()
        return self.result

    def insert_data(self,values = None):
        self.conn = self.connect_db()
        self.values = values
        self.cursorexe = self.conn.cursor()

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

        self.result = self.cursorexe.executemany(self.sql_cmd,self.values)
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

data_input = InputJawaban()
data_input = data_input.join_table(1)
np_data = np.array(data_input)
np_first = np_data[:,2:11]
np_second = np_data[:,15:24]
pengurangan = np.array([0,0,0,4,0,0,0,0,0])
data_hitung = np_first==np_second
jumlah = np.sum(data_hitung,axis=0)
total = np.subtract(jumlah,pengurangan)

column = [1]
new = np.append(total,column,axis=0)
id = [12]
new = np.insert(total,0,id,axis=0)
print(new)
new[4]=900
print (new)
get=new[4]
print (get)

# import pdb 
# pdb.set_trace()

print ("hello")