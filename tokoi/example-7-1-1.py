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
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_MIDDLE_DOWN, self.OnMouseMiddleDown)
        self.Bind(wx.EVT_MIDDLE_UP, self.OnMouseMiddleUp)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)

    def InitGL(self):
        glClearColor(1, 1, 1, 1)

    def OnSize(self, event):
        w, h = self.GetClientSize()
        glViewport(0, 0, w, h)
        glLoadIdentity()
        
    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

    def OnMouseLeftDown(self, event):
        print "left down"

    def OnMouseLeftUp(self, event):
        print "left up"

    def OnMouseMiddleDown(self, event):
        print "middle down"

    def OnMouseMiddleUp(self, event):
        print "middle up"

    def OnMouseRightDown(self, event):
        print "right down"

    def OnMouseRightUp(self, event):
        print "right up"

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, sys.argv[0])
    canvas = MyCanvas(frame)
    frame.Show()
    app.MainLoop()
    app.Destroy()