import wx


class MainWindow(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))

        self.panel = wx.Panel(self, -1)

        button = wx.Button(self.panel, -1, "Button")

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(button)

        add_btn = wx.Button(self.panel, -1, "Add")
        add_btn.Bind(wx.EVT_BUTTON, self.add)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(add_btn)

        main_vbox = wx.BoxSizer(wx.VERTICAL)
        main_vbox.Add(self.vbox)
        main_vbox.Add(hbox)

        self.panel.SetSizer(main_vbox)

        self.Centre()
        self.Show(True)
        self.Layout()

    def add(self, event):
        self.vbox.Add((wx.Button(self.panel, -1, "Button")))
        self.panel.Layout()


if __name__ == "__main__":
    app = wx.App()
    MainWindow(None, -1, 'Add a Button')
    app.MainLoop()
