#!usr/bin/env python

import wx

from views.ISTISTUtama import ISTISTUtama as I


class run(I):

	def __init__(self, *args, **kwrgs):
		super(run, self).__init__(*args, **kwrgs)

	pass


root = wx.App()
start = run(None)
start.Show()
root.MainLoop()
