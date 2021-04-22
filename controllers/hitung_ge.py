import sqlite3
import pandas as pd
import numpy as np

from models.query import KunciJawabanGE
from controllers.halaman_event import SqliteDB
import pathlib
import os
import sys

class GE():
  

  def __init__(self,parent):
    self.parent = parent
    self.connect_db = "home/cireng/Projects/pyist/models/istcore.sqlite"

    self.runGE = KunciJawabanGE(self.parent.connect_db)
    self.read_result = self.runGE.query()
    self.read_np2 = np.array(self.read_result)
    self.read_pd2 = pd.DataFrame(self.read_np2)

    self.read_result2 = self.parent.get_data
    self.read_np = np.array(self.read_result2)
    self.read_np = np.char.replace(self.read_np,' ','')
    self.read_pd = pd.DataFrame(self.read_np)
    
    self.input_jwbn = self.read_pd.filter([1,5])
    self.input_jwbn = self.input_jwbn.loc[0:15]
    self.input_jwbn = self.input_jwbn.to_records(index=False).tolist()

    self.dataku = []
    for data in self.input_jwbn:
      self.read = self.read_pd2[(self.read_pd2[2]==data[1])&(self.read_pd2[1]==data[0])]

      if self.read.empty == True:
        pass
      else :
        self.read = pd.DataFrame.to_numpy(self.read).tolist()
        self.dataku.append(self.read)

    self.dataku = [data for x in self.dataku for data in x]
    self.datanp = np.array(self.dataku)

    if not self.dataku:
      self.dataku.append(0)
      self.datanp = np.array(self.dataku).astype(int)
      pass

    else:
      self.datanp=self.datanp[:,3].astype(int)
      
  def result(self):
    self.result = np.sum(self.datanp)
    return self.result

class New():


  def __init__(self,parent):
    conn = sqlite3.connect("/home/cireng/Projects/pyist/models/istcore.sqlite")
    cursor = conn.cursor()
    sql_cmd ="""SELECT id_kunci_ge,
          [No],
          upper(replace(Jawaban,' ','')),
          Nilai
      FROM [Kunci Jawaban GE];

    """
    cursor.execute(sql_cmd)
    read_result = cursor.fetchall()
    conn.commit()
    conn.close()


    conn = sqlite3.connect("/home/cireng/Projects/pyist/models/istcore.sqlite")
    cursor = conn.cursor()

    sql_cmd2 ="""Select  upper([Input Jawaban].id_input_jawaban) ,
        upper([Input Jawaban].no) ,
        upper([Input Jawaban].se) ,
        upper([Input Jawaban].wa) ,
        upper([Input Jawaban].an) ,
        upper([Input Jawaban].ge) ,
        upper([Input Jawaban].ra) ,
        upper([Input Jawaban].zr) ,
        upper([Input Jawaban].fa) ,
        upper([Input Jawaban].wu) ,
        upper([Input Jawaban].me) ,
        upper([Input Jawaban].id_tes),
        upper([Input Jawaban].id_kunci),
        upper([Kunci Jawaban].id_kunci),
        upper([Kunci Jawaban].No),
        upper([Kunci Jawaban].se),
        upper([Kunci Jawaban].wa),
        upper([Kunci Jawaban].an),
        upper([Kunci Jawaban].ge),
        upper([Kunci Jawaban].ra),
        upper([Kunci Jawaban].zr),
        upper([Kunci Jawaban].fa),
        upper([Kunci Jawaban].wu),
        upper([Kunci Jawaban].me)
                from "Input Jawaban" 
                Left Join [Kunci Jawaban]
                On "Input Jawaban".id_kunci = "Kunci Jawaban".id_kunci
                where "Input Jawaban".id_tes = ?"""        
    values = 1
    cursor.execute(sql_cmd2,[values,])
    read_result2 = cursor.fetchall()
    conn.commit()
    conn.close()



    read_np = np.array(read_result2)
    read_np = np.char.replace(read_np,' ','')
    read_pd = pd.DataFrame(read_np)

    read_np2 = np.array(read_result)
    read_pd2 = pd.DataFrame(read_np2)

    self.input_jwbn = read_pd.filter([0,5])
    self.input_jwbn = self.input_jwbn.loc[0:15]
    self.input_jwbn = self.input_jwbn.to_records(index=False).tolist()

    read = read_pd2[(read_pd2[2]=="BUNffGA")&(read_pd2[1]==1)]
    read.empty
    print(read.empty)
    self.dataku = []
    for data in self.input_jwbn:
      read = read_pd2[(read_pd2[2]==data[1])&(read_pd2[1]==int(data[0]))]
      if read.empty == True:
        pass
      else :
        read = pd.DataFrame.to_numpy(read).tolist()

        self.dataku.append(read)

    self.dataku = [data for x in self.dataku for data in x]

    datanp = np.array(self.dataku)
    datanp=datanp[:,3].astype(int)
    print(np.sum(datanp))

if __name__ == "__main__":
  app = GE()
