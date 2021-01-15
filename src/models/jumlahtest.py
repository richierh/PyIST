import sqlite3


class DataPeserta():

    def __init__(self):
        self.conn = sqlite3.connect('models/istcore.sqlite')
        self.cursor = self.conn.cursor()

    
    def delete_data_peserta(self,*values):
        self.values= values
        sql_cmd="""DELETE FROM [Data Peserta]
            WHERE id = ?
                """
        self.cursor.execute(sql_cmd,self.values)
        self.conn.commit()
        self.conn.close()



class JumlahTesPerUser():

    def __init__(self):
        self.conn = sqlite3.connect('models/istcore.sqlite')
        self.cursor = self.conn.cursor()

    
    def insert_test(self,*values):
        # value = no test dan nama test
        self.values = values
        print (self.values)
        sql_cmd =   """INSERT INTO JumlahTesPerUser (
                                 No_test,
                                 [Nama Test],
                                 id
                                 
                             )
                             VALUES (
                                 ?,
                                 ?,
                                 ?
                    
                             );"""
        self.cursor.execute(sql_cmd,self.values)
        self.conn.commit()
        self.conn.close()


    def __close(self):
        self.conn.close()

    def delete_data(self,*values):
        # value = no test dan nama test
        self.values = values
        print (self.values)
        sql_cmd="""DELETE FROM JumlahTesPerUser
            WHERE
            id = ?;

        """
        self.cursor.execute(sql_cmd,self.values)
        self.conn.commit()
        self.conn.close()


run = JumlahTesPerUser()
datapeserta=DataPeserta()
# datapeserta.delete_data_peserta(99)
# run.insert_test(34234,"ddd",100)
# run.delete_data(99)