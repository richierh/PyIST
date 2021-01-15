
import wx


class FrameActivator(wx.Frame):
    
    def __init__(self, *args, **kwds):
        super(FrameActivator, self).__init__(*args, **kwds)
        self.SetTitle("Activator")
        self.SetSize(200, 200)
        # self.SetWindowStyleFlag(wx.CLOSE_BOX)

        sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.panel1 = wx.Panel(self)
        sizer1.Add(self.panel1, 1, wx.ALL | wx.EXPAND, 5)

        sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.static_label = wx.StaticText(self.panel1, label="Activator Aplikasi")
        sizer2.Add(self.static_label, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(sizer3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button1 = wx.Button(self.panel1, label="tes")
        sizer3.Add(self.button1, 0, wx.ALL | wx.EXPAND, 5)

        self.button1 = wx.Button(self.panel1, label="tes")
        sizer3.Add(self.button1, 0, wx.ALL | wx.EXPAND, 5)

        self.panel1.SetSizer(sizer2)
        self.SetSizer(sizer1)

        pass


if __name__ == '__main__':
    root = wx.App()
    run = FrameActivator(None)
    run.Show()
    root.MainLoop()

    pass
