from PIL import Image
import stepic
import sys

from moviepy.editor import *
import moviepy.editor as mpy
from moviepy.editor import VideoFileClip

def encrypt_video(filename, username):
	# Orignal Video
	original = VideoFileClip("videos/"+filename+".mp4")
	t0 = 56

	first_half = VideoFileClip("videos/"+filename+".mp4").subclip(0, t0)
	second_half = VideoFileClip("videos/"+filename+".mp4").subclip(t0+1, original.duration)

	original.save_frame("videos/frame.png", t=t0)

	img = Image.open("videos/frame.png").convert(mode='RGB')
	stepic.encode_inplace(img, username)
	msg = stepic.decode(img)
	print(msg)
	img.save("videos/frame.png")

	encoded_clip = ImageClip('videos/frame.png', duration=1)

	new_mov = CompositeVideoClip([first_half.set_start(0),
								  encoded_clip.set_start(t0),
								  second_half.set_start(t0+1)])

	# Write the result to a file (many options available !)
	new_mov.write_videofile("static/"+username+"_"+filename+".avi", codec='png')
