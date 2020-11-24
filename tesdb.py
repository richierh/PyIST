import sqlite3
import pandas as pd
import numpy as np

from models.query import KunciJawabanGE
from controllers.halaman_event import SqliteDB
import pathlib
import os
import sys

class GE():
  

  def __init__(self):
    self.connect_db = "home/cireng/Projects/pyist/models/istcore.sqlite"

    self.runGE = KunciJawabanGE(self.connect_db)
    import pdb
    pdb.set_trace()
  
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
    # print(read_pd[[0,5]].head(10))

    read_np2 = np.array(read_result)
    read_pd2 = pd.DataFrame(read_np2)

    # print (read_np[:16,[1][5]])
    # print (read_pd.head(20))
    # print(read_pd2.head(20))
    # read_pd2.set_index(2,inplace=True)
    input_jwbn = read_pd.filter([0,5])
    input_jwbn = input_jwbn.loc[0:15]
    input_jwbn = input_jwbn.to_records(index=False).tolist()
    # print(input_jwbn)
    # print(read_pd2)
    read = read_pd2[(read_pd2[2]=="BUNffGA")&(read_pd2[1]==1)]
    read.empty
    print(read.empty)


    # print (read_pd2.loc['ALATINDERA',:])

    dataku = []
    for data in input_jwbn:
      read = read_pd2[(read_pd2[2]==data[1])&(read_pd2[1]==int(data[0]))]
      if read.empty == True:
        pass
      else :
        read = pd.DataFrame.to_numpy(read).tolist()
        # print(read)
    #   print(kk)
        dataku.append(read)
    # print(dataku)
    dataku = [data for x in dataku for data in x]

    datanp = np.array(dataku)
    datanp=datanp[:,3].astype(int)
    print(np.sum(datanp))






if __name__ == "__main__":
  app = GE()
