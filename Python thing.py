Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import wx
>>> 
>>> app = wx.App()
>>> frame = wx.Frame(parent=none, title = 'Project')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    frame = wx.Frame(parent=none, title = 'Project')
NameError: name 'none' is not defined
>>> frame.Show()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    frame.Show()
NameError: name 'frame' is not defined
>>>  frame = wx.Frame(parent=None, title = 'Project')
 
SyntaxError: unexpected indent
>>> frame = wx.Frame(parent=None, title = 'Project')
>>> frame.Show()
True
>>> app.MainLoop()
