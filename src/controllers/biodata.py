#! /usr/bin/env python
"""Subclass of Biodata, which is generated by wxFormBuilder."""

import wx
from views.istcore import Biodata

# Implementing Biodata


class BiodataPeserta(Biodata):

    def __init__(self, parent):
        super().__init__()


class Biodata(Biodata):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.tipe_biodata 
        self.parent.select_input

        self.m_textCtrl_nama.Disable()
        self.m_textCtrl_tanggal_tes.Disable()
        self.m_textCtrl_usia.Disable()
        self.m_textCtrl_jenis_kelamin.Disable()
        self.m_textCtrl_tanggal_lahir.Disable()
        self.m_textCtrl_asal_sekolah.Disable()
        self.m_textCtrl_jurusan_sekolah.Disable()
        self.m_textCtrl_asal_universitas.Disable()
        self.m_textCtrl_jurusan_universitas.Disable()
        self.m_textCtrl_kota.Disable()
        self.m_textCtrl_hobi.Disable()
        self.m_textCtrl_prestasi_akademik.Disable()
        self.m_textCtrl_prestasi_non_akademik.Disable()
        self.m_textCtrl_ekskul_yang_diikuti.Disable()		

        self.m_textCtrl_no_tes.Disable()
        self.m_textCtrl_tanggal_tes2.Disable()
        self.m_textCtrl_nama2.Disable()
        self.m_textCtrl_jenis_kelamin2.Disable()
        self.m_textCtrl_tanggal_lahir2.Disable()
        self.m_textCtrl_pendidikan_terakhir.Disable()
        self.m_textCtrl_jurusan_pendidikan2.Disable()
        self.m_textCtrl_kota2.Disable()
        self.m_textCtrl_perusahaan_instansi2.Disable()
        self.m_textCtrl_posisi_jabatan2.Disable()

        self.parent.tipe_biodata == 0
        if self.parent.select_input == 1:
            if self.parent.tipe_biodata == 0:
                self.m_textCtrl_no_tes1.SetValue(self.parent.biodata[0])
                self.m_textCtrl_tanggal_tes1.SetValue(self.parent.biodata[1])
                self.m_textCtrl_nama1.SetValue(self.parent.biodata[2])
                self.m_textCtrl_jenis_kelamin1.SetValue(self.parent.biodata[3])
                self.m_textCtrl_tanggal_lahir1.SetValue(self.parent.biodata[4])
                self.m_textCtrl_usia1.SetValue(str(self.parent.biodata[5]))
                self.m_textCtrl_asal_sekolah_universitas.SetValue(self.parent.biodata[6])
                self.m_textCtrl_pendidikan_terakhir1.SetValue(self.parent.biodata[7])
                self.m_textCtrl_jurusan.SetValue(self.parent.biodata[8])
                self.m_textCtrl_posisi_pekerjaan.SetValue(self.parent.biodata[9])
                self.m_textCtrl_perusahaan.SetValue(self.parent.biodata[10])
                self.m_textCtrl_keterangan.SetValue(self.parent.biodata[11])

            if self.parent.tipe_biodata == 1:
                self.m_panel16.Show()
                self.m_panel17.Hide()
                self.m_textCtrl_nama.SetValue(self.parent.biodata[0])
                self.m_textCtrl_tanggal_tes.SetValue(self.parent.biodata[1])
                self.m_textCtrl_usia.SetValue(str(self.parent.biodata[2]))
                self.m_textCtrl_jenis_kelamin.SetValue(self.parent.biodata[3])
                self.m_textCtrl_tanggal_lahir.SetValue(self.parent.biodata[4])
                self.m_textCtrl_asal_sekolah.SetValue(self.parent.biodata[5])
                self.m_textCtrl_jurusan_sekolah.SetValue(self.parent.biodata[6])
                self.m_textCtrl_asal_universitas.SetValue(self.parent.biodata[7])
                self.m_textCtrl_jurusan_universitas.SetValue(self.parent.biodata[8])
                self.m_textCtrl_kota.SetValue(self.parent.biodata[9])
                self.m_textCtrl_hobi.SetValue(self.parent.biodata[10])
                self.m_textCtrl_prestasi_akademik.SetValue(self.parent.biodata[11])
                self.m_textCtrl_prestasi_non_akademik.SetValue(self.parent.biodata[12])
                self.m_textCtrl_ekskul_yang_diikuti.SetValue(self.parent.biodata[13])	

                self.SetSize(wx.Size(500, 500))

            elif self.parent.tipe_biodata == 2 :
                self.m_panel17.Show()
                self.m_panel16.Hide()
                self.m_textCtrl_no_tes.SetValue(self.parent.biodata[0])
                self.m_textCtrl_tanggal_tes2.SetValue(self.parent.biodata[1])
                self.m_textCtrl_nama2.SetValue(self.parent.biodata[2])
                self.m_textCtrl_jenis_kelamin2.SetValue(self.parent.biodata[3])
                self.m_textCtrl_tanggal_lahir2.SetValue(self.parent.biodata[4])
                self.m_textCtrl_pendidikan_terakhir.SetValue(self.parent.biodata[5])
                self.m_textCtrl_jurusan_pendidikan2.SetValue(self.parent.biodata[6])
                self.m_textCtrl_kota2.SetValue(self.parent.biodata[7])
                self.m_textCtrl_perusahaan_instansi2.SetValue(self.parent.biodata[8])
                self.m_textCtrl_posisi_jabatan2.SetValue(self.parent.biodata[9])
                self.SetSize(wx.Size(500, 500))

        elif self.parent.select_input == 2 :
            pass
        self.m_panel19.Layout()	

        pass

    # Handlers for Biodata events.
    def m_textCtrl_namaOnLeftUp(self, event):
        # TODO: Implement m_textCtrl_namaOnLeftUp
        pass
