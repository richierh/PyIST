#!usr/bin/env python
"""
from oscheck import *
import wx
"""

import os
import sys
import pathlib

import wx


# path = "{}{}".format(os.getcwd(), "/AppsSDS")
# print (type(path))
path= pathlib.Path.cwd()/'views'
# print (type(path))

sys.path.append(str(path))
sys.path
# print (sys.path)
# os.getcwd()
# cd = "{}{}".format(os.getcwd(), "/AppsSDS")
cd = pathlib.Path.cwd()/"views"
os.chdir(str(cd))

from views.main import run
