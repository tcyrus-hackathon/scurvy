from PIL import Image
import stepic
import sys
import os

from moviepy.editor import *
import moviepy.editor as mpy 
from moviepy.editor import VideoFileClip


os.system("cp ../webapp/videos/modified_gangnam_style.avi videos")
os.chdir("videos")

def decrypt_video(filename, t0):
	vid = VideoFileClip(filename+".avi")

	vid.save_frame("frame.png", t=t0+0.2)

	img = Image.open("frame.png").convert(mode='RGB')
	msg = stepic.decode(img)
	print(msg)



decrypt_video('modified_gangnam_style', 56)