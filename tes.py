

class Pesertaku():

    def __init__(self,parent = None):
        nama_file = "istcore"
        self.tes = PesertaData("/home/cireng/Projects/pyist/models/istcore")

    def get_data(self):
        self.tes.get_data_peserta()

        return True

run = Pesertaku()
run.get_data()
class DatabaseKandidat():

    def __init__(self,parent = None):
        nama_file = "istcore"
        tes = DatabaseConnect(nama_file)
        data = [2,"Alif","2019/10/23","Laki-Laki","2002/12/04"]
        data2 = ["22343","S1","PSIKOLOGI","BANDUNG","PT JARINGAN INTERNASIONAL","SENIOR IT MANAGER"]
                                            # id_kand,
                                            # asal_sekolah,
                                            # jurusan_sekolah,
                                            # asal_universitas,
                                            # jurusan_universitas,
                                            # kota,
                                            # hobi,
                                            # prestasi_akademik,
                                            # prestasi_non_akademik,
                                            # ekskul_yang_diikuti
        data3 = ["SMA NUSANTARA","IPA","INSTITUT ANTAH BERANTAH","TEKNIK SIPIL","JAMBI","MEMASAK",\
                "JUARA MAIN KELERENG","JUARA BALAP KARUNG","TAE KWON DO","12"]
        tabel = DatabaseBioData(tes)
        tabel.insert_biodata(data,data2,data3)
        # print (tabel.lihat_data_kandidat_baru())
        insert_jawaban = DataBaseInput(tes)
        # print(insert_jawaban.insert_data_jawaban("jj"))
        # print (insert_jawaban.get_jumlah_baris("jawaban_peserta"))