import pygetwindow as gw
from pynput import keyboard
from pynput.keyboard import Key, Controller
import win32gui,win32process
import pywinauto
import os
import psutil
import time

SpotifyDir = "%appdata%/Spotify/Spotify.exe"
os.system('start '+SpotifyDir)
time.sleep(3)

WindowName = "Spotify Free"
hwnd=win32gui.FindWindow(None, WindowName)
pid=win32process.GetWindowThreadProcessId(hwnd)
print(pid)
o=1
while o==1:
    time.sleep(0.5)
    WindowTitle=win32gui.GetWindowText(hwnd)
    if WindowTitle != "":
        print(WindowTitle)
    if WindowTitle == 'REASON - Pop Shit':
        time.sleep(3)
        p = psutil.Process(pid[1])
        p.terminate()
        os.system('start '+SpotifyDir)
        activewindow = (win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        pywinauto.application.Application().connect(best_match=activewindow).top_window().set_focus()
        time.sleep(7)
        handle = gw.getWindowsWithTitle('Spotify Free')[0]
        try:
            pywinauto.application.Application().connect(best_match='Spotify').top_window().set_focus()
        except:
            pass
        handle.activate()
        handle.maximize()
        time.sleep(0.5)
        keyboard = Controller()
        keyboard.press(Key.space)
        handle.minimize()
        print('Closed Ad')
