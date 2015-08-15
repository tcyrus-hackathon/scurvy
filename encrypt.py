from PIL import Image
import stepic
import sys
import os

from moviepy.editor import *
import moviepy.editor as mpy
from moviepy.editor import VideoFileClip

os.chdir("videos")

def encrypt_video(filename, userinfo):
	# Orignal Video
	original = VideoFileClip(filename+".mp4")
	t0 = 56

	first_half = VideoFileClip(filename+".mp4").subclip(0, t0)
	second_half = VideoFileClip(filename+".mp4").subclip(t0+1, original.duration)

	original.save_frame("frame.png", t=t0)

	img = Image.open("frame.png").convert(mode='RGB')
	stepic.encode_inplace(img, userinfo)
	msg = stepic.decode(img)
	print(msg)

	"""os.system("cp frame.png fame2.png")
	encoded_clip = ImageClip('frame2.png', duration=1)

	new_mov = CompositeVideoClip([first_half.set_start(0),
								  encoded_clip.set_start(t0),
								  second_half.set_start(t0+1)])

	# Write the result to a file (many options available !)
	new_mov.write_videofile("modified_"+filename+".mp4")
	"""

	img = Image.open("frame.png").convert(mode='RGB')
	msg = stepic.decode(img)
	print(msg)


encrypt_video("gangnam_style", "ayylmaoo")
