from istcore import ISTUtama
import wx


class Ist(ISTUtama):

    def __init__(self, parent):
        super(Ist, self).__init__(parent)
        pass


if __name__ == "__main__":
    root = wx.App()
    run = Ist(None)
    run.Show()
    root.MainLoop()
