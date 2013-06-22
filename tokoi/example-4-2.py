import sys
import wx
from wx import glcanvas
from OpenGL.GL import *

class MyCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(MyCanvas, self).__init__(parent, -1, attribList=[])
        self.context = glcanvas.GLContext(self)
        self.initialized = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glClearColor(1, 1, 1, 1)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        glViewport(0, 0, w, h)
        
    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0])
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()