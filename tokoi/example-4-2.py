import sys
import wx
from wx import glcanvas
from OpenGL.GL import *

class GLFrame(wx.Frame):
    """A simple class for using OpenGL with wxPython.
    """
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        super(GLFrame, self).__init__(parent, id, title, pos, size, style, name)
        self.canvas = glcanvas.GLCanvas(self)
        self.initialized = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        self.context = glcanvas.GLContext(self.canvas)
        self.canvas.SetCurrent(self.context)
        glClearColor(1, 1, 1, 1)
        width, height = self.GetClientSize()
        glViewport(0, 0, width, height)

    def OnPaint(self, event):
        if not self.initialized:
            self.InitGL()
            self.initialized = True
        self.OnDraw()
        
    def OnDraw(self):
        self.canvas.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()
        self.canvas.SwapBuffers()

if __name__ == '__main__':
    app = wx.App()
    frame = GLFrame(None, -1, sys.argv[0])
    frame.Show()
    app.MainLoop()
    app.Destroy()
