import wx
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit

import matplotlib as mpl
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)


class GrafikRWSW(wx.Panel):
    import wx
    import matplotlib as mpl
    from matplotlib.backends.backend_wxagg import (
        FigureCanvasWxAgg as FigureCanvas,
        NavigationToolbar2WxAgg as NavigationToolbar)
    import numpy as np
    import matplotlib.pyplot as plt
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.parent=parent
        from matplotlib.backends.backend_wx import _load_bitmap

        import pathlib

        self.figure = mpl.figure.Figure(dpi=None, figsize=(2, 2))
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.axes = self.figure.add_subplot(111)

        
        """disini untuk menentukan nilai sumbu x dan sumbu y"""
        self.x = [1,2,3,4,5,6]
        self.y = [1,2,3,4,5,6]


        self.axes.plot(self.x,self.y)

        self.toolbar = NavigationToolbar(self.canvas)
        self.pathimage = pathlib.Path.cwd() / "resources/images/binadata.png"
        self.newpathimage= pathlib.Path.cwd() / "resources/images/bila.png"
        self.ON_CUSTOM  = wx.NewIdRef()
        self.image1 = wx.Image(str(self.pathimage))
        self.re_image3 = self.image1.Rescale(20, 20)
        self.re_image3.SaveFile(self.newpathimage.as_posix())
        self.newpathimage

        print(self.re_image3)
        self.toolbar.AddSimpleTool(self.ON_CUSTOM, _load_bitmap(self.newpathimage),\
                           'Pan to the left', 'Pan graph to the left')
       

        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)

















# Below is the example of making matplotlib grafik inside wx

class Plot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)

class PlotNotebook(wx.Panel):
    def __init__(self, parent, id=-1):
        wx.Panel.__init__(self, parent, id=id)
        self.nb = aui.AuiNotebook(self)
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def add(self, name="plot"):
        page = Plot(self.nb)
        self.nb.AddPage(page, name)
        return page.figure


def demo():
    # alternatively you could use
    #app = wx.App()
    # InspectableApp is a great debug tool, see:
    # http://wiki.wxpython.org/Widget%20Inspection%20Tool
    app = wx.App()
    frame = wx.Frame(None, -1, 'Plotter')
    plotter = PlotNotebook(frame)
    axes1 = plotter.add('figure 1').gca()
    axes1.plot([1, 2, 3], [2, 1, 4])
    axes2 = plotter.add('figure 2').gca()
    axes2.plot([1, 2, 3, 4, 5], [2, 1, 4, 2, 3])
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    demo()