# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Jul  4 2019)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview 
from views.istcore import ISTUtama

###########################################################################
# # Class MyFrame1
###########################################################################


class Tes(ISTUtama):

    def __init__(self, parent):
        super().__init__(parent)
        self.tes = PanggilInputTotal(self)
        self.tes2 = RWSWScore(self)


class RWSWScore(ISTUtama):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent   
        # self.parent.kelompok_usia
        
        self.parent.m_textCtrl_nilai_rw_se.SetValue(str(self.parent.input_peserta_rw_sw[0][0]))
        self.parent.m_textCtrl_nilai_rw_wa.SetValue(str(self.parent.input_peserta_rw_sw[1][0]))
        self.parent.m_textCtrl_nilai_rw_an.SetValue(str(self.parent.input_peserta_rw_sw[2][0]))
        self.parent.m_textCtrl_nilai_rw_ge.SetValue(str(self.parent.input_peserta_rw_sw[3][0]))
        self.parent.m_textCtrl_nilai_rw_me.SetValue(str(self.parent.input_peserta_rw_sw[4][0]))
        self.parent.m_textCtrl_nilai_rw_ra.SetValue(str(self.parent.input_peserta_rw_sw[5][0]))
        self.parent.m_textCtrl_nilai_rw_zr.SetValue(str(self.parent.input_peserta_rw_sw[6][0]))
        self.parent.m_textCtrl_nilai_rw_fa.SetValue(str(self.parent.input_peserta_rw_sw[7][0]))
        self.parent.m_textCtrl_nilai_rw_wu.SetValue(str(self.parent.input_peserta_rw_sw[8][0]))
        self.parent.sum = []

        for data in self.parent.input_peserta_rw_sw:
            self.parent.sum.append(data[0])

        self.parent.m_textCtrl_nilai_rw_jumlah.SetValue(str(sum(self.parent.sum)))

        self.parent.m_textCtrl_nilai_sw_se.SetValue(str(self.parent.input_peserta_rw_sw[0][1]))
        self.parent.m_textCtrl_nilai_sw_wa.SetValue(str(self.parent.input_peserta_rw_sw[1][1]))
        self.parent.m_textCtrl_nilai_sw_an.SetValue(str(self.parent.input_peserta_rw_sw[2][1]))
        self.parent.m_textCtrl_nilai_sw_ge.SetValue(str(self.parent.input_peserta_rw_sw[3][1]))
        self.parent.m_textCtrl_nilai_sw_me.SetValue(str(self.parent.input_peserta_rw_sw[4][1]))
        self.parent.m_textCtrl_nilai_sw_ra.SetValue(str(self.parent.input_peserta_rw_sw[5][1]))
        self.parent.m_textCtrl_nilai_sw_zr.SetValue(str(self.parent.input_peserta_rw_sw[6][1]))
        self.parent.m_textCtrl_nilai_sw_fa.SetValue(str(self.parent.input_peserta_rw_sw[7][1]))
        self.parent.m_textCtrl_nilai_sw_wu.SetValue(str(self.parent.input_peserta_rw_sw[8][1]))

        self.parent.m_textCtrl_nilai_total_sw.SetValue(str(self.parent.geasamt))
        self.parent.m_textCtrl_nilai_IQ.SetValue(str(self.parent.iq))

        print ("tes")


class PanggilInputTotal(ISTUtama):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def getdata(self):
        self.value = [self.parent.m_spinCtrl_se.GetValue(),
        self.parent.m_spinCtrl_wa.GetValue(),
        self.parent.m_spinCtrl_an.GetValue(),
        self.parent.m_spinCtrl_ge.GetValue(),
        self.parent.m_spinCtrl_ra.GetValue(),
        self.parent.m_spinCtrl_zr.GetValue(),
        self.parent.m_spinCtrl_fa.GetValue(),
        self.parent.m_spinCtrl_wu.GetValue(),
        self.parent.m_spinCtrl_me.GetValue()
        ]
        return self.value

    def getdata_arrange(self):
        self.value = [self.parent.m_spinCtrl_se.GetValue(),
        self.parent.m_spinCtrl_wa.GetValue(),
        self.parent.m_spinCtrl_an.GetValue(),
        self.parent.nilai_ge,
        self.parent.m_spinCtrl_ra.GetValue(),
        self.parent.m_spinCtrl_zr.GetValue(),
        self.parent.m_spinCtrl_fa.GetValue(),
        self.parent.m_spinCtrl_wu.GetValue(),
        self.parent.m_spinCtrl_me.GetValue()
        ]
        return self.value

        
class PanggilGrid():

    def __init__(self, parent):

        self.parent = parent
        self.parent.m_grid2.SetColLabelValue(0, "")
        self.parent.m_grid2.SetColLabelValue(1, "SE")
        self.parent.m_grid2.SetColLabelValue(2, "")
        self.parent.m_grid2.SetColLabelValue(3, "WA")
        self.parent.m_grid2.SetColLabelValue(4, "")
        self.parent.m_grid2.SetColLabelValue(5, "AN")
        self.parent.m_grid2.SetColLabelValue(6, "")
        self.parent.m_grid2.SetColLabelValue(7, "GE")
        self.parent.m_grid2.SetColLabelValue(8, "")
        self.parent.m_grid2.SetColLabelValue(9, "RA")
        self.parent.m_grid2.SetColLabelValue(10, "")
        self.parent.m_grid2.SetColLabelValue(11, "ZR")
        self.parent.m_grid2.SetColLabelValue(12, "")
        self.parent.m_grid2.SetColLabelValue(13, "FA")
        self.parent.m_grid2.SetColLabelValue(14, "")
        self.parent.m_grid2.SetColLabelValue(15, "WU")
        self.parent.m_grid2.SetColLabelValue(16, "")
        self.parent.m_grid2.SetColLabelValue(17, "ME")
        self.parent.m_grid2.SetColLabelValue(18, "")

        for l in range(0, 18):
            if not(l % 2):
                for i in range(0, 20):
                    stringval = i + 1

                    if l == 6 and i >= 1 :
                        self.parent.m_grid2.SetCellValue(i, l, "")
                        self.parent.m_grid2.SetCellBackgroundColour(i, l, "grey")
                        self.parent.m_grid2.SetReadOnly(i, l)

                    else :
                        self.parent.m_grid2.SetCellValue(i, l, str(stringval))
                        self.parent.m_grid2.SetCellAlignment(i, l, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                        self.parent.m_grid2.SetReadOnly(i, l)

            elif l == 7 and i >= 1 :
                for i in range(1, 20):
                    stringval = i + 1

                    self.parent.m_grid2.SetCellValue(i, l, "")
                    self.parent.m_grid2.SetCellBackgroundColour(i, l, "grey")
                    self.parent.m_grid2.SetReadOnly(i, l)

    def getdata2(self):
        self.data = []

        for l in range(0, 18):

            if l % 2:
                self.datapertama = []

                for i in range(0, 20):
                    stringval = i + 1

                    if l == 6 and i >= 1 :
                        # self.parent.m_grid2.GetCellValue(i,l)
                        pass

                    else :
                        self.a = self.parent.m_grid2.GetCellValue(i, l)
                        if self.a == "":
                            self.a = 0
                        else :
                            self.a = int(self.a)
                        self.datapertama.append(self.a)
            # elif l == 7 and i >=1 :
            #     for i in range(1,20):
            #         stringval = i+1

            #         self.parent.m_grid2.GetCell(i,l,"")
            #         self.parent.m_grid2.SetCellBackgroundColour(i,l, "grey")
            #         self.parent.m_grid2.SetReadOnly(i,l)
 
                self.data.append(self.datapertama)
                
        return self.data

    def getdata(self):
        self.data = []

        for i in range (0,20):
            self.datapertama = []
            for l in range(0,18):
                if l % 2:
                    self.a = self.parent.m_grid2.GetCellValue(i, l)
                    self.datapertama.append(self.a)

            self.data.append(self.datapertama)

        return self.data

    def getdata_arrange(self):
        self.data_sum = []
        i = 0
        for data in self.data:
            print (f"ini adalah total {sum(self.data[0])}")
            if i == 3 :
                self.sum = int(self.parent.nilai_ge)
                self.data_sum.append(self.sum)

            else :
                self.sum = sum(data)
                self.data_sum.append(self.sum)
            i += 1

        return self.data_sum


class PanggilDataView ():

    def __init__(self, parent):
        self.parent = parent
        bsizerdataview = wx.BoxSizer(wx.VERTICAL)
        
        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.parent.m_panel_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"SE", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"WA", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn(u"DD", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT)
        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT)

        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn8 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn9 = self.m_dataViewListCtrl1.AppendTextColumn(u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn9 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.data = [   "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        "1",
                        "",
                        
        ]
        self.m_dataViewListCtrl1.InsertItem(0, self.data)
        bsizerdataview.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)
        
        self.parent.m_panel_input.SetSizer(bsizerdataview)
        self.parent.Layout()

        self.parent.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    root = wx.App()
    runwind = MyFrame1(None)
    runwind.Show()
    root.MainLoop()
