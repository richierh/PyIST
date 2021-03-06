#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.0 on Thu Mar 21 19:53:17 2019
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx

from controllers.ISTISTUtama import ISTISTUtama


class MyApp(wx.App):

    def OnInit(self):
        self.frame = ISTISTUtama(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    import gettext
    import os
    import pathlib

    pathwd = pathlib.Path.cwd() / ".."
    os.chdir(pathwd)  
    gettext.install("app")  # replace with the appropriate catalog name
    app = MyApp(0)
    app.MainLoop()
