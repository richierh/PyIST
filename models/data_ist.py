
class DataIST():

    def __init__(self,usia):
        self.datafunc()


class ISTCore(object):

    def __init__(self,**kwds):
        self.data = kwds
        # print (self.data)

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
    # print (a.datase)
    run = ISTCore(**data)
    # istcore.nilaise()
    # print (istcore.nilaise())
    # print ("sukses")
    # print (run)
    if run == "134" :
        # print ("true")

