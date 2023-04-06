import glob
import os
import random

import ctypes

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
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

def reset_background():
    try:
        wallpaper = get_fake_wallpaper()

    except EmptyWallpaperFile:
        print("./assest/fake 파일안에 fake배경화면을 넣어주세요.")

    setup_wallpaper(wallpaper)

def show_real_background():
    try:
        wallpaper = get_real_wallpaper()

    except EmptyWallpaperFile:
        print("./assest/real 파일안에 real배경화면을 넣어주세요.")

    setup_wallpaper(wallpaper)

if __name__ == '__main__':
    reset_background()