from controllers.database_control import DatabaseBioData,DataBaseInput,DatabaseConnect

nama_file = "ist"
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
        "JUARA MAIN KELERENG","JUARA BALAP KARUNG","TAE KWON DO"]
tabel = DatabaseBioData(tes)
tabel.insert_biodata(data,data2,data3)
print (tabel.lihat_data_kandidat_baru())
insert_jawaban = DataBaseInput(tes)
print(insert_jawaban.insert_data_jawaban("jj"))
print (insert_jawaban.get_jumlah_baris("jawaban_peserta"))