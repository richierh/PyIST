import wx
from views.warning_data import WarningFrame


class WarningFrameInherited(WarningFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.SetTitle("WARNING !!")
        self.SetSize((300, 100))
        self.m_button_ok_warning.SetLabel("Ok")
        self.m_staticText1.SetLabel("Data ini tidak bisa di hapus")
        self.Centre()
        self.Layout()

    def m_button_ok_warningOnButtonClick(self, event):
        self.Close()
        pass
