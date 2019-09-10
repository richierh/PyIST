'''
Created on Feb 9, 2019

@author: binakarir
'''
import wx
import pathlib


class PropertiesTampilan():
    
    def __init__(self,parent):
        self.parent = parent

        # print ("properties diaktifkan")
        pass
    
    
    def tabel_show(self):
        self.parent.m_dataViewListColumn12 = self.parent.m_dataViewListCtrl9.AppendTextColumn( u"CAS", wx.DATAVIEW_CELL_INERT, 75, wx.ALIGN_CENTER|wx.ALIGN_LEFT, wx.DATAVIEW_COL_RESIZABLE )

        pass


    def logo_show(self):
        self.pathpict = pathlib.Path.cwd()/"resources/images/binadata.png"
        print (self.pathpict)
        self.image = wx.Image(str(self.pathpict))
        self.re_image = self.image.Rescale(300,150)
        self.parent.m_logo_binakarir.SetBitmap(wx.Bitmap(self.re_image))


    def tabel_show(self):
        
#         self.index = 0
#         self.listheaderlistCtrl1 = [
#             ["No","50",wx.LIST_FORMAT_CENTER],
#             ["Aspek Analisa Skor ist","200",wx.LIST_FORMAT_LEFT],
#             ["Kelemahan","100",wx.LIST_FORMAT_LEFT],
#             ["Keunggulan","100",wx.LIST_FORMAT_LEFT]
#             ]
      
#         self.data = [
#             [8,"Kemampuan berbahasa"],
#             [7,"Pengembalian keputusan"],
#             [6,"Daya analisis"],
#             [5,"Judgement"],
#             [4,"Ketelitian"],
#             [3,"Kreatifitas"],
#             [2,"Daya ingat dan konsentrasi"],
#             [1,"Kemampuan berhitung"],
#             ]
# #         print (self.listheaderlistCtrl1[self.index][0])
#         for listheader in self.listheaderlistCtrl1 :
#             print (listheader[0])
#             self.parent.m_listCtrl1.InsertColumn(self.index,listheader[0],format = listheader[2],width = int(listheader[1]))
#             self.index+=1
        
#         for i in self.data :
#             print (i)
#             index = self.parent.m_listCtrl1.InsertItem(0, str(i[0])) 
#             self.parent.m_listCtrl1.SetItem(index, 1, str(i[1])) 
# #             self.parent.m_listCtrl1.SetStringItem(index, 2, i[1]) 
 
 
      
#         self.listheaderlistCtrl2 = [
#             ["Flexibilitas Berpikir",300,wx.LIST_FORMAT_CENTER],
#             ["Kemantapan Berpikir",300,wx.LIST_FORMAT_CENTER],
#             ]
         
#         self.index2 = 0
        
#         for listheader in self.listheaderlistCtrl2 :
#             print (listheader[0])
#             self.parent.m_listCtrl2.InsertColumn(self.index2,listheader[0],format = listheader[2],width = int(listheader[1]))
#             self.index2+=1
        pass
    

class AddTextCtrlProperties():
    
    def __init__(self,parent):
        self.parent = parent
        
    
    def enabledisablecontrolse(self):
        if self.parent.m_textCtrl47.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl6.Enable(False)    
            self.parent.m_textCtrl8.Enable(False)    
            self.parent.m_textCtrl9.Enable(False)    
            self.parent.m_textCtrl10.Enable(False)    
            self.parent.m_textCtrl11.Enable(False)    
            self.parent.m_textCtrl12.Enable(False)    
            self.parent.m_textCtrl13.Enable(False)    
            self.parent.m_textCtrl14.Enable(False)    
            self.parent.m_textCtrl15.Enable(False)    
            self.parent.m_textCtrl16.Enable(False)    
            self.parent.m_textCtrl17.Enable(False)    
            self.parent.m_textCtrl18.Enable(False)    
            self.parent.m_textCtrl19.Enable(False)    
            self.parent.m_textCtrl20.Enable(False)    
            self.parent.m_textCtrl21.Enable(False)    
            self.parent.m_textCtrl22.Enable(False)    
            self.parent.m_textCtrl23.Enable(False)    
            self.parent.m_textCtrl24.Enable(False)    
            self.parent.m_textCtrl25.Enable(False)    
            self.parent.m_textCtrl26.Enable(False)    
        else :
            self.parent.m_textCtrl6.Enable(True)    
            self.parent.m_textCtrl8.Enable(True)    
            self.parent.m_textCtrl9.Enable(True)    
            self.parent.m_textCtrl10.Enable(True)    
            self.parent.m_textCtrl11.Enable(True)    
            self.parent.m_textCtrl12.Enable(True)    
            self.parent.m_textCtrl13.Enable(True)    
            self.parent.m_textCtrl14.Enable(True)    
            self.parent.m_textCtrl15.Enable(True)    
            self.parent.m_textCtrl16.Enable(True)    
            self.parent.m_textCtrl17.Enable(True)    
            self.parent.m_textCtrl18.Enable(True)    
            self.parent.m_textCtrl19.Enable(True)    
            self.parent.m_textCtrl20.Enable(True)    
            self.parent.m_textCtrl21.Enable(True)    
            self.parent.m_textCtrl22.Enable(True)    
            self.parent.m_textCtrl23.Enable(True)    
            self.parent.m_textCtrl24.Enable(True)    
            self.parent.m_textCtrl25.Enable(True)    
            self.parent.m_textCtrl26.Enable(True)           
     
    def enabledisablecontrolsetotal(self):
        if self.parent.m_textCtrl6.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl47.Enable(False)    
        else :
            self.parent.m_textCtrl47.Enable(True)
            
            
    def enabledisablecontrolwa(self):
        
        if self.parent.m_textCtrl48.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl7.Enable(False)    
            self.parent.m_textCtrl27.Enable(False)    
            self.parent.m_textCtrl28.Enable(False)    
            self.parent.m_textCtrl29.Enable(False)    
            self.parent.m_textCtrl30.Enable(False)    
            self.parent.m_textCtrl31.Enable(False)    
            self.parent.m_textCtrl32.Enable(False)    
            self.parent.m_textCtrl33.Enable(False)    
            self.parent.m_textCtrl34.Enable(False)    
            self.parent.m_textCtrl35.Enable(False)    
            self.parent.m_textCtrl36.Enable(False)    
            self.parent.m_textCtrl37.Enable(False)    
            self.parent.m_textCtrl38.Enable(False)    
            self.parent.m_textCtrl39.Enable(False)    
            self.parent.m_textCtrl40.Enable(False)    
            self.parent.m_textCtrl41.Enable(False)    
            self.parent.m_textCtrl42.Enable(False)    
            self.parent.m_textCtrl43.Enable(False)    
            self.parent.m_textCtrl44.Enable(False)    
            self.parent.m_textCtrl45.Enable(False)    
        else :
            self.parent.m_textCtrl7.Enable(True)    
            self.parent.m_textCtrl27.Enable(True)    
            self.parent.m_textCtrl28.Enable(True)    
            self.parent.m_textCtrl29.Enable(True)    
            self.parent.m_textCtrl30.Enable(True)    
            self.parent.m_textCtrl31.Enable(True)    
            self.parent.m_textCtrl32.Enable(True)    
            self.parent.m_textCtrl33.Enable(True)    
            self.parent.m_textCtrl34.Enable(True)    
            self.parent.m_textCtrl35.Enable(True)    
            self.parent.m_textCtrl36.Enable(True)    
            self.parent.m_textCtrl37.Enable(True)    
            self.parent.m_textCtrl38.Enable(True)    
            self.parent.m_textCtrl39.Enable(True)    
            self.parent.m_textCtrl40.Enable(True)    
            self.parent.m_textCtrl41.Enable(True)    
            self.parent.m_textCtrl42.Enable(True)    
            self.parent.m_textCtrl43.Enable(True)    
            self.parent.m_textCtrl44.Enable(True)    
            self.parent.m_textCtrl45.Enable(True)    
          
    def enabledisablecontrolwatotal(self):
        if self.parent.m_textCtrl7.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl48.Enable(False)    
        else :
            self.parent.m_textCtrl48.Enable(True)

    def enabledisablecontrolan(self):
        if self.parent.m_textCtrl481.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl71.Enable(False)    
            self.parent.m_textCtrl271.Enable(False)    
            self.parent.m_textCtrl281.Enable(False)    
            self.parent.m_textCtrl291.Enable(False)    
            self.parent.m_textCtrl301.Enable(False)    
            self.parent.m_textCtrl311.Enable(False)    
            self.parent.m_textCtrl321.Enable(False)    
            self.parent.m_textCtrl331.Enable(False)    
            self.parent.m_textCtrl341.Enable(False)    
            self.parent.m_textCtrl351.Enable(False)    
            self.parent.m_textCtrl361.Enable(False)    
            self.parent.m_textCtrl371.Enable(False)    
            self.parent.m_textCtrl381.Enable(False)    
            self.parent.m_textCtrl391.Enable(False)    
            self.parent.m_textCtrl401.Enable(False)    
            self.parent.m_textCtrl411.Enable(False)    
            self.parent.m_textCtrl421.Enable(False)    
            self.parent.m_textCtrl431.Enable(False)    
            self.parent.m_textCtrl441.Enable(False)    
            self.parent.m_textCtrl451.Enable(False)    
        else :
            self.parent.m_textCtrl71.Enable(True)    
            self.parent.m_textCtrl271.Enable(True)    
            self.parent.m_textCtrl281.Enable(True)    
            self.parent.m_textCtrl291.Enable(True)    
            self.parent.m_textCtrl301.Enable(True)    
            self.parent.m_textCtrl311.Enable(True)    
            self.parent.m_textCtrl321.Enable(True)    
            self.parent.m_textCtrl331.Enable(True)    
            self.parent.m_textCtrl341.Enable(True)    
            self.parent.m_textCtrl351.Enable(True)    
            self.parent.m_textCtrl361.Enable(True)    
            self.parent.m_textCtrl371.Enable(True)    
            self.parent.m_textCtrl381.Enable(True)    
            self.parent.m_textCtrl391.Enable(True)    
            self.parent.m_textCtrl401.Enable(True)    
            self.parent.m_textCtrl411.Enable(True)    
            self.parent.m_textCtrl421.Enable(True)    
            self.parent.m_textCtrl431.Enable(True)    
            self.parent.m_textCtrl441.Enable(True)    
            self.parent.m_textCtrl451.Enable(True)    

    def enabledisablecontrolantotal(self):
        if self.parent.m_textCtrl71.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl481.Enable(False)    
        else :
            self.parent.m_textCtrl481.Enable(True)

    def enabledisablecontrolra(self):
        
        if self.parent.m_textCtrl181.GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl303.Enable(False)    
            self.parent.m_textCtrl313.Enable(False)    
            self.parent.m_textCtrl323.Enable(False)    
            self.parent.m_textCtrl333.Enable(False)    
            self.parent.m_textCtrl343.Enable(False)    
            self.parent.m_textCtrl353.Enable(False)    
            self.parent.m_textCtrl363.Enable(False)    
            self.parent.m_textCtrl373.Enable(False)    
            self.parent.m_textCtrl383.Enable(False)    
            self.parent.m_textCtrl393.Enable(False)    
            self.parent.m_textCtrl403.Enable(False)    
            self.parent.m_textCtrl413.Enable(False)    
            self.parent.m_textCtrl423.Enable(False)    
            self.parent.m_textCtrl433.Enable(False)    
            self.parent.m_textCtrl443.Enable(False)    
            self.parent.m_textCtrl453.Enable(False)    
            self.parent.m_textCtrl463.Enable(False)    
            self.parent.m_textCtrl473.Enable(False)    
            self.parent.m_textCtrl483.Enable(False)    
            self.parent.m_textCtrl493.Enable(False)    
        else :
            self.parent.m_textCtrl303.Enable(True)    
            self.parent.m_textCtrl313.Enable(True)    
            self.parent.m_textCtrl323.Enable(True)    
            self.parent.m_textCtrl333.Enable(True)    
            self.parent.m_textCtrl343.Enable(True)    
            self.parent.m_textCtrl353.Enable(True)    
            self.parent.m_textCtrl363.Enable(True)    
            self.parent.m_textCtrl373.Enable(True)    
            self.parent.m_textCtrl383.Enable(True)    
            self.parent.m_textCtrl393.Enable(True)    
            self.parent.m_textCtrl403.Enable(True)    
            self.parent.m_textCtrl413.Enable(True)    
            self.parent.m_textCtrl423.Enable(True)    
            self.parent.m_textCtrl433.Enable(True)    
            self.parent.m_textCtrl443.Enable(True)    
            self.parent.m_textCtrl453.Enable(True)    
            self.parent.m_textCtrl463.Enable(True)    
            self.parent.m_textCtrl473.Enable(True)    
            self.parent.m_textCtrl483.Enable(True)    
            self.parent.m_textCtrl493.Enable(True)     
          
    def enabledisablecontrolratotal(self):
        if self.parent.m_textCtrl303.GetValue() != -1:
            print ("tidak nol")
            self.parent.m_textCtrl181.Enable(False)    
        else :
            self.parent.m_textCtrl181.Enable(True)      
            
    def enabledisablecontrolzr(self):       
        if self.parent.m_textCtrl196.GetValue()!= "":
            print ("tidak nol")
            self.parent.m_textCtrl10.Enable(False)
            self.parent.m_textCtrl11.Enable(False)   
            self.parent.m_textCtrl12.Enable(False)   
            self.parent.m_textCtrl13.Enable(False)   
            self.parent.m_textCtrl14.Enable(False)   
            self.parent.m_textCtrl15.Enable(False)   
            self.parent.m_textCtrl16.Enable(False)   
            self.parent.m_textCtrl17.Enable(False)   
            self.parent.m_textCtrl18.Enable(False)   
            self.parent.m_textCtrl19.Enable(False)   
            self.parent.m_textCtrl20.Enable(False)   
            self.parent.m_textCtrl211.Enable(False)   
            self.parent.m_textCtrl221.Enable(False)   
            self.parent.m_textCtrl231.Enable(False)   
            self.parent.m_textCtrl241.Enable(False)   
            self.parent.m_textCtrl251.Enable(False)   
            self.parent.m_textCtrl261.Enable(False)   
            self.parent.m_textCtrl271.Enable(False)   
            self.parent.m_textCtrl281.Enable(False)   
            self.parent.m_textCtrl291.Enable(False)   
        else :
            self.parent.m_textCtrl10.Enable(True)
            self.parent.m_textCtrl11.Enable(True)   
            self.parent.m_textCtrl12.Enable(True)   
            self.parent.m_textCtrl13.Enable(True)   
            self.parent.m_textCtrl14.Enable(True)   
            self.parent.m_textCtrl15.Enable(True)   
            self.parent.m_textCtrl16.Enable(True)   
            self.parent.m_textCtrl17.Enable(True)   
            self.parent.m_textCtrl18.Enable(True)   
            self.parent.m_textCtrl19.Enable(True)   
            self.parent.m_textCtrl20.Enable(True)   
            self.parent.m_textCtrl211.Enable(True)   
            self.parent.m_textCtrl221.Enable(True)   
            self.parent.m_textCtrl231.Enable(True)   
            self.parent.m_textCtrl241.Enable(True)   
            self.parent.m_textCtrl251.Enable(True)   
            self.parent.m_textCtrl261.Enable(True)   
            self.parent.m_textCtrl271.Enable(True)   
            self.parent.m_textCtrl281.Enable(True)   
            self.parent.m_textCtrl291.Enable(True)   
            
    def enabledisablecontrolzrtotal(self):
        if self.parent.m_textCtrl100.GetValue() != -1:
            print ("tidak nol")
            self.parent.m_textCtrl196.Enable(False)    
        else :
            self.parent.m_textCtrl196.Enable(True)      

    def enabledisablecontrolfa(self):       
        if self.parent.m_textCtrl484.GetValue()!= "":
            print ("tidak nol")
            for listfa in self.parent.properties_listcontrol.list_fa:
                listfa.Enable(False)
        else :
            for listfa in self.parent.properties_listcontrol.list_fa:
                listfa.Enable(True)

    def enabledisablecontrolfatotal(self):
        if self.parent.properties_listcontrol.list_fa[0].GetValue() != "":
            print ("tidak nol")
            self.parent.m_textCtrl484.Enable(False)    
        else :
            self.parent.m_textCtrl484.Enable(True)      

    def enabledisablecontrolwu(self):       
        if self.parent.m_textCtrl485.GetValue()!= "":
            print ("tidak nol")
            for listfa in self.parent.properties_listcontrol.list_wu:
                listfa.Enable(False)
        else :
            for listfa in self.parent.properties_listcontrol.list_wu:
                listfa.Enable(True)

    def enabledisablecontrolwutotal(self):
        if self.parent.properties_listcontrol.list_wu[0].GetValue() != "":
            print ("tidak nol gfd")
            self.parent.m_textCtrl485.Enable(False)    
        else :
            self.parent.m_textCtrl485.Enable(True)     

    def enabledisablecontrolme(self):       
        if self.parent.m_textCtrl486.GetValue()!= "":
            print ("tidak nol")
            for listfa in self.parent.properties_listcontrol.list_me:
                listfa.Enable(False)
        else :
            for listfa in self.parent.properties_listcontrol.list_me:
                listfa.Enable(True)

    def enabledisablecontrolmetotal(self):
        if self.parent.properties_listcontrol.list_me[0].GetValue() != "":
            print ("tidak nol gfd")
            self.parent.m_textCtrl486.Enable(False)    
        else :
            self.parent.m_textCtrl486.Enable(True)     