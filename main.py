import glob
import os
import random

import win32api
import win32con
import win32gui

from EmptyWallpaperFile import EmptyWallpaperFile

def relative_path_to_absolute_path(relative_path):
    return os.path.abspath(relative_path)

def get_fake_wallpaper():
    fake_wallpapers = glob.glob("./assets/fake/*")

    if (len(fake_wallpapers) == 0):
        raise EmptyWallpaperFile()

    wallpaper = random.choice(fake_wallpapers)

    return wallpaper


def get_real_wallpaper():
    real_wallpapers = glob.glob("./assets/real/*")

    if (len(real_wallpapers) == 0):
        raise EmptyWallpaperFile()

    wallpaper = random.choice(real_wallpapers)

    return wallpaper


def setup_wallpaper(wallpaper_path):
    abs_path = relative_path_to_absolute_path(wallpaper_path)

    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "Wallpaper", 0, win32con.REG_SZ, abs_path)
    win32api.RegCloseKey(key)

    print(abs_path)

    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, abs_path, win32con.SPIF_SENDWININICHANGE)


def reset_background():
    try:
        wallpaper = get_fake_wallpaper()

    except EmptyWallpaperFile:
        print("./assest/real 파일안에 real배경화면을 넣어주세요.")

    setup_wallpaper(wallpaper)


if __name__ == '__main__':
    reset_background()
