class EmptyWallpaperFile(Exception):
    def __init__(self):
        super().__init__("/assets 파일 안에 real배경화면과 fake배경화면을 넣어주세요.")
