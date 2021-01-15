

import keygen
# global lisensi


class AkLisen():

    def __init__(self, parent):
        self.parent = parent
        self.__method__()

        pass
    
    def __method__(self):
        global lisensi
        lisensi = 1778

        self.cek = keygen.Key()
        # print (lisensi)
        # lisensi = self.parent.m_textCtrl1.GetValue()

        self.cek.verify()
        print (self.parent.m_textCtrl1.GetValue())

        if  self.cek.verify() == True and self.parent.m_textCtrl1.GetValue() != "":
            self.valid = "Valid"
            self.parent.m_staticText4.SetLabel("Valid")
        else :
            self.valid = "Invalid"
            self.parent.m_staticText4.SetLabel("Invalid")
        
        return self.valid

    def __str__(self):

        return self.valid
