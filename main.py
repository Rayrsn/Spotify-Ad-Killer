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
emptyspace="                                                                 "
WindowName = "Spotify Free"
hwnd=win32gui.FindWindow(None, WindowName)
pid=win32process.GetWindowThreadProcessId(hwnd)
print(pid)
if pid[0] == 0:
    os.system('cls')
    print('\nNot hooked, please pause the music.\n')
    print('Exiting now.')
    time.sleep(5)
    exit()
o=1

def AdKiller():
    global hwnd
    global pid
    truefalse = 1
    time.sleep(0.5)
    WindowTitle=win32gui.GetWindowText(hwnd)
    if WindowTitle != "":
        print(WindowTitle+emptyspace,end="\r")
    if WindowTitle != "Spotify Free":
        truefalse = WindowTitle.find('-')
    if truefalse == -1:
        time.sleep(3)
        p = psutil.Process(pid[1])
        p.terminate()
        os.system('start '+SpotifyDir)
        activewindow = (win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        try:
            pywinauto.application.Application().connect(best_match=activewindow).top_window().set_focus()
        except:
            pass
        time.sleep(7)
        WindowName = "Spotify Free"
        hwnd=win32gui.FindWindow(None, WindowName)
        pid=win32process.GetWindowThreadProcessId(hwnd)
        print(pid)
        try:
            handle = gw.getWindowsWithTitle('Spotify Free')[0]
        except:
            pass
        try:
            pywinauto.application.Application().connect(best_match='Spotify').top_window().set_focus()
        except:
            pass
        try:
            handle.activate()
            handle.maximize()
            time.sleep(0.5)
            keyboard = Controller()
            keyboard.press(Key.space)
            handle.minimize()
            print('Closed Ad')
        except:
            pass
        return
while o==1:
    AdKiller()
