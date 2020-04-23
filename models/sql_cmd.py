#! /usr/bin/env python

from query import SqliteDB

import numpy as np

class KunciJawaban(SqliteDB):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.path_db='/home/cireng/Projects/pyist/models/istcore.sqlite'
        print(self.path_db)

        print(self.hitung_jumlah_row("Data Peserta"))

    def ambil_data(self,values=None):
        self.conn = self.connect_db()
        self.cursorexe = self.conn.cursor()
        self.values = values
        self.sql_cmd = """ SELECT *  FROM "Kunci Jawaban" """
        self.get_data = self.cursorexe.execute(self.sql_cmd).fetchall()
        self.close_db()       
        data1 = self.get_data[0]
        data2 = self.get_data[1]
        data3 = self.get_data[2]
        data4 = self.get_data[3]
        data5 = self.get_data[4]
        data6 = self.get_data[5]
        data7 = self.get_data[6]
        data8 = self.get_data[7]
        data9 = self.get_data[8]
        data10 = self.get_data[9]
        data11 = self.get_data[10]
        data12 = self.get_data[11]
        data13 = self.get_data[12]
        data14 = self.get_data[13]
        data15 = self.get_data[14]
        data16 = self.get_data[15]
        data17 = self.get_data[16]
        data18 = self.get_data[17]
        data19 = self.get_data[18]
        data20 = self.get_data[19]

        list_np = [np.array(data1),
        np.array(data2),
        np.array(data3),
        np.array(data4),
        np.array(data5),
        np.array(data6),
        np.array(data7),
        np.array(data8),
        np.array(data9),
        np.array(data10),
        np.array(data11),
        np.array(data12),
        np.array(data13),
        np.array(data14),
        np.array(data15),
        np.array(data16),
        np.array(data17),
        np.array(data18),
        np.array(data19),
        np.array(data20)]
        self.get_data = np.column_stack((list_np)).tolist()
        
        

        return self.get_data

if __name__=="__main__":
    jawaban_peserta = np.array(['B' ,'C', 'D', 'D', 'D', 'B','C', 'A', 'E', 'B', 'C', 'D', 'D', 'E' ,'C' ,'A', 'B', 'B','C', 'D'])
    run = KunciJawaban("istcore.sqlite")
    print (run.ambil_data(None)[1])
    j = np.array(run.ambil_data(None)[1])

    print(jawaban_peserta == j)
    data_akhir = (jawaban_peserta==j)
    data_akhir = np.array(data_akhir).tolist()

    print (data_akhir)
