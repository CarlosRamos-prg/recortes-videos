from moviepy.editor import *

video = VideoFileClip("video.mp4")

for i in range(i):
    cortado = video.subclip(i*30, (i+1)*30)
    cortado.write_videofile("parte"+str(i)+".mp4")