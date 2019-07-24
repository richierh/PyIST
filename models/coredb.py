'''
Created on Feb 15, 2019

@author: binakarir
'''

import sqlite3
import pathlib
import os


class Table():
    
    # pathloc  = []
    
    def __init__(self,parent):
        # print (pathloc)
        self.pathloc = parent
        self.parent     = parent
        self.conn       = sqlite3.connect(self.pathloc)
        self.cur        = self.conn.cursor()
        self.sql_create_table1 =  """
            CREATE TABLE IF NOT EXISTS [Jawaban Peserta] (
                [Id Jawaban Peserta] INTEGER PRIMARY KEY AUTOINCREMENT
                                             NOT NULL,
                [id Peserta]         INTEGER NOT NULL
                                             REFERENCES Peserta ([Id Peserta]) ON UPDATE SET NULL,
                [Id Kunci Jawaban]   INTEGER REFERENCES [Kunci Jawaban] ([Id Kunci Jawaban]) ON UPDATE SET NULL,
                [Nomor Peserta]      INT,
                [No Jawaban]         INT     NOT NULL,
                [Jawaban Peserta SE] TEXT,
                [Kunci Jawaban SE]   TEXT,
                [Jawaban Peserta WA] TEXT,
                [Kunci Jawaban WA]   TEXT,
                [Jawaban Peserta AN] TEXT,
                [Kunci Jawaban AN]   TEXT,
                [Jawaban Peserta GE] TEXT,
                [Jawaban Peserta RA] TEXT,
                [Kunci Jawaban RA]   TEXT,
                [Jawaban Peserta ZR] TEXT,
                [Kunci Jawaban ZR]   TEXT,
                [Jawaban Peserta FA] TEXT,
                [Kunci Jawaban FA]   TEXT,
                [Jawaban Peserta WU] TEXT,
                [Kunci Jawaban WU]   TEXT,
                [Jawaban Peserta ME] TEXT,
                [Kunci Jawaban ME]   TEXT
            );
          """
        self.sql_create_table2 = """
        CREATE TABLE IF NOT EXISTS [Kunci Jawaban] (
            [Id Kunci Jawaban] INTEGER PRIMARY KEY,
            [No]               INTEGER,
            SE                 TEXT,
            WA                 TEXT,
            AN                 TEXT,
            GE                 TEXT,
            RA                 TEXT,
            ZR                 TEXT,
            FA                 TEXT,
            WU                 TEXT,
            ME                 TEXT
        );
        """
        self.sql_create_table3 = """
        CREATE TABLE IF NOT EXISTS Peserta (
            [Id Peserta]    INTEGER PRIMARY KEY AUTOINCREMENT
                                    NOT NULL,
            [Nama Peserta]  TEXT,
            [Nomor Peserta] INT,
            Usia            INT,
            Kelas           TEXT,
            [Asal Sekolah]  TEXT
        );
        """
    
    def connect_table(self):
        pass
    
    def create_table(self):
        self.cur.execute(self.sql_create_table1)
        self.cur.execute(self.sql_create_table2)
        self.cur.execute(self.sql_create_table3)
        self.conn.close()

    def delete_file(self):
        return os.remove(pathloc)

    def insert_name(self):
        self.sqlinsertname ="""
        
        
        """
        pass
    
class QueryTabel():

    # pathloc  = []
    
    def __init__(self,parent):
        self.pathloc = parent
        # print (pathloc)
        self.parent     = parent
        self.conn       = sqlite3.connect(self.pathloc)
        self.cur        = self.conn.cursor()
   
    def connect_table(self):
        pass
    
    
    def create_table(self):
        # self.cur.execute(self.sql_create_table1)
        # self.cur.execute(self.sql_create_table2)
        # self.cur.execute(self.sql_create_table3)
        self.conn.close()

    def delete_file(self):
        return os.remove(pathloc)

    def insert_name(self):
        self.sqlinsertname ="""
       
        """
        pass

    def __kelompokusia(self):

        if self.kelompokusia == 12 :
            self.tableumur = "TableDataKelompokUmur12"
        
        elif self.kelompokusia == 13 :
            self.tableumur = "TableDataKelompokUmur13"

        elif self.kelompokusia == 14 :
            self.tableumur = "TableDataKelompokUmur14"

        elif self.kelompokusia == 15 :
            self.tableumur = "TableDataKelompokUmur15"

        elif self.kelompokusia == 16 :
            self.tableumur = "TableDataKelompokUmur16"

        elif self.kelompokusia == 17 :
            self.tableumur = "TableDataKelompokUmur17"

        elif self.kelompokusia == 18 :
            self.tableumur = "TableDataKelompokUmur18"

        elif self.kelompokusia == 19 :
            self.tableumur = "TableDataKelompokUmur19"        
        return self.tableumur


    def query_option(self,column,rawscore,kelompokusia):

        self.column         = column
        self.rawscore       = rawscore
        self.kelompokusia   = kelompokusia

        self.tableumur = self.__kelompokusia()
        self.column = column

        self.sql_query_table =  """
        SELECT {}
        FROM {} 
        WHERE RW = ?        
        """.format(self.column,self.tableumur)

        if self.kelompokusia == 12 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        elif self.kelompokusia == 13 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()
        
        elif self.kelompokusia == 14 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()
 
        elif self.kelompokusia == 15 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        elif self.kelompokusia == 16 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        elif self.kelompokusia == 17 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        elif self.kelompokusia == 18 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        elif self.kelompokusia == 19 :
            self.cur.execute(self.sql_query_table,(self.rawscore,))
            self.getdata = self.cur.fetchone()

        # self.datascore = self.getdata
        # datascores = []
        # for datascore in self.getdata:
        #     datascores.append(datascore)
        
        self.nilaiScore = self.getdata[0]
        
        self.conn.close()
        
        return self.nilaiScore




if __name__ == '__main__':

    # d =os.chdir("..")
    pathloc = pathlib.Path.cwd()/"models/ist"
    # print (pathloc)
    run = QueryTabel(pathloc)
#     Table.pathloc = pathloc
#     ist.delete_file()
    # object.query_option("nama kolom","nilai mentah","kelompokusia")
    # print (run.query_option("SE","4",12))