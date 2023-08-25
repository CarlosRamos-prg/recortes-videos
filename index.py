from moviepy.editor import *

video = VideoFileClip("video.mp4")

for i in range(60):
    cortado = video.subclip(1, 2)
    cortado.write_videofile("parte"+i+".mp4")