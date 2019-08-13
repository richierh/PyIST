


class KalkulasiNilai():


    def __init__(self,parent):
        self.parent = parent
        # print (self.parent.panggilgrid.getdata())
        # print (self.parent.get_biodata())
        self.getdata_hasil_input = self.parent.panggilgrid.getdata()
        self.getdata_biodata = self.parent.get_biodata()
        self.select_input = self.parent.select_input
        

        pass

    def method_hitung(self):


        pass



    def konversi_nilai_ge(self,values):
        self.value = values
        print (f"ini nilai GE {self.value}")
        pass

    