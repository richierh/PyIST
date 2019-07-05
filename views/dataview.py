# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul  4 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview 


###########################################################################
## Class MyFrame1
###########################################################################
class PanggilGrid():


    def __init__(self,parent):
        self.parent = parent
        self.parent.m_grid2.SetColLabelValue(0,"")
        self.parent.m_grid2.SetColLabelValue(1,"SE")
        self.parent.m_grid2.SetColLabelValue(2,"")
        self.parent.m_grid2.SetColLabelValue(3,"WA")
        self.parent.m_grid2.SetColLabelValue(4,"")
        self.parent.m_grid2.SetColLabelValue(5,"AN")
        self.parent.m_grid2.SetColLabelValue(6,"")
        self.parent.m_grid2.SetColLabelValue(7,"GE")
        self.parent.m_grid2.SetColLabelValue(8,"")
        self.parent.m_grid2.SetColLabelValue(9,"RA")
        self.parent.m_grid2.SetColLabelValue(10,"")
        self.parent.m_grid2.SetColLabelValue(11,"ZR")
        self.parent.m_grid2.SetColLabelValue(12,"")
        self.parent.m_grid2.SetColLabelValue(13,"FA")
        self.parent.m_grid2.SetColLabelValue(14,"")
        self.parent.m_grid2.SetColLabelValue(15,"WU")
        self.parent.m_grid2.SetColLabelValue(16,"")
        self.parent.m_grid2.SetColLabelValue(17,"ME")
        self.parent.m_grid2.SetColLabelValue(18,"")
        for l in range(0,18):
            if not(l%2):
                for i in range(0,20):
                    stringval = i+1

                    if l == 6 and i >=1 :
                        self.parent.m_grid2.SetCellValue(i,l,"")
                        self.parent.m_grid2.SetCellBackgroundColour(i,l, "grey")

                    else :
                        self.parent.m_grid2.SetCellValue(i,l,str(stringval))
            elif l == 7 and i >=1 :
                for i in range(0,20):
                    stringval = i+1

                    self.parent.m_grid2.SetCellValue(i,l,"")
                    self.parent.m_grid2.SetCellBackgroundColour(i,l, "grey")


class PanggilDataView ():

    def __init__(self,parent):
        self.parent = parent
        bsizerdataview = wx.BoxSizer(wx.VERTICAL)
        
        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.parent.m_panel_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"SE", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"WA", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"DD", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT )
        self.m_dataViewListColumn6 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT )

        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn7 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn8 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn8 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

        self.m_dataViewListColumn9 = self.m_dataViewListCtrl1.AppendTextColumn( u"NO", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn9 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_EDITABLE, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )

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
        self.m_dataViewListCtrl1.InsertItem(0,self.data)
        bsizerdataview.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


        
        self.parent.m_panel_input.SetSizer( bsizerdataview )
        self.parent.Layout()

        self.parent.Centre( wx.BOTH )

    def __del__( self ):
        pass


if __name__ == "__main__":
    root = wx.App()
    runwind = MyFrame1(None)
    runwind.Show()
    root.MainLoop()