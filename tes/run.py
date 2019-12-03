from belajar import MyFrame8
import wx


class RunProgram(MyFrame8):

    def __init__(self, parent):
        super().__init__(parent)
        # self.m_menuItem6.SetBitmap( wx.Bitmap( u"/home/cireng/Projects/pyist/tes/man.png", wx.BITMAP_TYPE_ANY ) )


if __name__ == "__main__":
    root = wx.App()
    run = RunProgram(None).Show()
    root.MainLoop()
