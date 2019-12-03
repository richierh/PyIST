"""Subclass of NamaNorma, which is generated by wxFormBuilder."""

import wx
from views.nama_norma import NamaNorma


# Implementing NamaNorma
class NamaNormaInherited(NamaNorma):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.databasekon = self.parent.parent.parent.databasekon

        self.SetSize((500, 200))

    # Handlers for NamaNorma events.
    def m_button_okOnButtonClick(self, event):
        # TODO: Implement m_button_okOnButtonClick
        self.nama_norma = self.m_textCtrl_nama_norma.GetValue()
        self.keterangan_norma = self.m_textCtrl_keterangan.GetValue()
        print(self.nama_norma)
        # if self.parent.parent.buat_baru_norma == 1:
        # 	print("harus buat baru")
        # else :
        # 	print("nggak harus buat baru")
        self.parent.m_dataViewListCtrl4.GetValue(0, 0)
        self.parent.parent.m_dataViewListCtrl3.GetItemCount()
        self.GetLastRow = int(self.parent.parent.m_dataViewListCtrl3.GetValue(\
            self.parent.parent.m_dataViewListCtrl3.GetItemCount() - 1, 0))

        self.parent.parent.m_dataViewListCtrl3.AppendItem(\
            [str(self.GetLastRow + 1), \
            str(self.parent.parent.m_dataViewListCtrl3.GetItemCount() + 1), \
            self.nama_norma, \
            self.keterangan_norma])

        self.tabel_norma_sendiri = TabelNormaSendiriConnect(self.databasekon)
        self.tabel_norma_sendiri.insert_nama_norma([self.nama_norma, self.keterangan_norma])
        
        self.data_norma = []
        for datarow in range(0, self.parent.m_dataViewListCtrl4.GetItemCount()):
            self.col0 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 0)
            self.col1 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 1)
            self.col2 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 2)
            self.col3 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 3)
            self.col4 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 4)
            self.col5 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 5)
            self.col6 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 6)
            self.col7 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 7)
            self.col8 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 8)
            self.col9 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 9)
            self.col10 = self.parent.m_dataViewListCtrl4.GetValue(datarow, 10)
            self.tabel_norma_sendiri = TabelNormaSendiriConnect(self.databasekon)

            self.data_norma.append((self.col0,
                                    self.col1,
                                    self.col2,
                                    self.col3,
                                    self.col4,
                                    self.col5,
                                    self.col6,
                                    self.col7,
                                    self.col8,
                                    self.col9,
                                    self.col10,
                                    # 15
                                    self.tabel_norma_sendiri.query_last_row()
                                    ))
        self.data_norma
        self.tabel_norma_sendiri = TabelNormaSendiriConnect(self.databasekon)

        self.tabel_norma_sendiri.insert_kunci_jawaban_norma(self.data_norma)

        """
        Ini code untuk menginput data norma ke tabel
        """

        self.Close()
        self.parent.Close()
        pass

    def m_button_batalOnButtonClick(self, event):
        # TODO: Implement m_button_batalOnButtonClick
        self.Close()
        pass


if __name__ == "__main__" :
    root = wx.App()
    main = NamaNormaInherited(None)
    main.Show()
    root.MainLoop()
