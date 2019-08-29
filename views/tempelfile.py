# /usr/bin/python
import platform
import pathlib


class TempelFile():

    def __init__(self, parent):
        self.parent = parent
        print (self.parent)
        
        pass

    def compilefile(self):

        if self.parent == True :
            print (True)
            if platform.system() == "Windows":
                print("te")
                print(platform.system())
                self.write = pathlib.Path("C:\\ProgramData\\3351.txt")
                f = open(self.write, "w+")
                f.close()
            
            elif platform.system() == "Linux":
                print ("tess ini adalah linux")
                print(platform.system())
                self.write = pathlib.Path.home() / ".3351"
                f = open(self.write, "w+")
                f.close()

            elif platform.system() == "Mac OS" :
                print ("tessss")
            
            else :
                print ("System Operasi tidak dikenali")
        
        else :
            print ("False gagal")

        pass


if __name__ == "__main__":
    verify = True
    datainput = "tes aja"
    cekfile = TempelFile(verify)
    cekfile.compilefile()
    
    pass
