import time
from pygame import mixer
mixer.init()
mixer.music.load('C:/Users/reactzin/Desktop/workspace/python-curso-em-video/xablau.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(0.1)