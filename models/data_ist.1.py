
class DataIST():

    def __init__(self,usia):
        self.datafunc()

    def datafunc(self):
        self.datase = {
                "20" : 134,
                "19" : 134,
                "18" : 134,
                "17" : 134,
                "16" : 134,
                "15" : 134,
                "14" : 130,
                "13" : 126,
                "12" : 122,
                "11" : 118,
                "10" : 114,
                "9" : 110,
                "8" : 106,
                "7" : 102,
                "6" : 98,
                "5" : 94,
                "4" : 90,
                "3" : 86, 
                "2" : 82, 
                "1" : 78,
                "0" : 74
            }

        self.datawa = {
                "20" : 133,
                "19" : 133,
                "18" : 133,
                "17" : 133,
                "16" : 133,
                "15" : 133,
                "14" : 129,
                "13" : 125,
                "12" : 120,
                "11" : 116,
                "10" : 112,
                "9" : 108,
                "8" : 104,
                "7" : 100,
                "6" : 95,
                "5" : 91,
                "4" : 87,
                "3" : 83, 
                "2" : 79, 
                "1" : 75,
                "0" : 70
            }
 
        self.dataan = {
                "20" : 135,
                "19" : 135,
                "18" : 135,
                "17" : 135,
                "16" : 135,
                "15" : 135,
                "14" : 132,
                "13" : 128,
                "12" : 124,
                "11" : 120,
                "10" : 116,
                "9" : 112,
                "8" : 108,
                "7" : 105,
                "6" : 101,
                "5" : 97,
                "4" : 93,
                "3" : 89, 
                "2" : 85, 
                "1" : 82,
                "0" : 78
            }

        self.datame = {
                "20" : 133,
                "19" : 133,
                "18" : 133,
                "17" : 130,
                "16" : 127,
                "15" : 124,
                "14" : 121,
                "13" : 119,
                "12" : 116,
                "11" : 113,
                "10" : 110,
                "9" : 107,
                "8" : 104,
                "7" : 101,
                "6" :  98,
                "5" : 95,
                "4" : 92,
                "3" : 89, 
                "2" : 86, 
                "1" : 83,
                "0" : 80
            }
        self.datage = {
                "20" : 132,
                "19" : 132,
                "18" : 132,
                "17" : 132,
                "16" : 132,
                "15" : 132,
                "14" : 129,
                "13" : 125,
                "12" : 121,
                "11" : 117,
                "10" : 114,
                "9" : 100,
                "8" : 106,
                "7" : 103,
                "6" :  99,
                "5" : 95,
                "4" : 91,
                "3" : 88, 
                "2" : 84, 
                "1" : 80,
                "0" : 77
            }

        self.datara = {
                "20" : 133,
                "19" : 133,
                "18" : 133,
                "17" : 133,
                "16" : 133,
                "15" : 133,
                "14" : 129,
                "13" : 126,
                "12" : 122,
                "11" : 118,
                "10" : 114,
                "9" : 111,
                "8" : 107,
                "7" : 103,
                "6" : 100,
                "5" : 96,
                "4" : 92,
                "3" : 89, 
                "2" : 85, 
                "1" : 81,
                "0" : 77
            }

        self.datazr = {
                "20" : 133,
                "19" : 133,
                "18" : 133,
                "17" : 133,
                "16" : 133,
                "15" : 130,
                "14" : 127,
                "13" : 123,
                "12" : 120,
                "11" : 117,
                "10" : 113,
                "9" : 110,
                "8" : 107,
                "7" : 103,
                "6" : 100,
                "5" : 97,
                "4" : 93,
                "3" : 90, 
                "2" : 87, 
                "1" : 83,
                "0" : 80
            }
        self.datafa = {
                "20" : 134,
                "19" : 134,
                "18" : 134,
                "17" : 134,
                "16" : 130,
                "15" : 127,
                "14" : 123,
                "13" : 120,
                "12" : 116,
                "11" : 113,
                "10" : 109,
                "9" : 105,
                "8" : 102,
                "7" :  98,
                "6" :  95,
                "5" :  91,
                "4" :  88,
                "3" :  84, 
                "2" :  80, 
                "1" :  77,
                "0" :  74
            }


class ISTCore(object):

    def __init__(self,**kwds):
        self.data = kwds
        print (self.data)

        self.data.get("20")
        # print (self.data.get("20"))
        self.nilaise()
    def nilaise(self):

        return self.data.get("20")

    def __str__(self):

        return str(self.data.get("20"))





if __name__ == "__main__":
    data = {
        "20" : 134,
        "19" : 134,
        "18" : 134,
        "17" : 134,
        "16" : 134,
        "15" : 134,
        "14" : 130,
        "13" : 126,
        "12" : 122,
        "11" : 118,
        "10" : 114,
        "9" : 110,
        "8" : 106,
        "7" : 102,
        "6" : 98,
        "5" : 94,
        "4" : 90,
        "3" : 86, 
        "2" : 82, 
        "1" : 78,
        "0" : 74
    }
    a = DataIST()
    print (a.datase)
    run = ISTCore(**data)
    # run.nilaise()
    # print (run.nilaise())
    # print ("sukses")
    print (run)
    if run == "134" :
        print ("true")

