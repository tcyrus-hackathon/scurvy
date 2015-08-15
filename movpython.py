# Import everything needed to edit video clips
from moviepy.editor import *
import moviepy.editor as mpy 
from moviepy.editor import VideoFileClip

# Orignal Video
orignal = VideoFileClip("Her.mp4")

# Grabs clip at 00:00:55.99 to 00:00:56.05
clip = VideoFileClip("Her.mp4").subclip(55.99,56.05)

# New Clip, ready to be modified
frame = clip.save_frame("frame.png")




newMov = CompositeVideoClip([orignal, frame])
# Write the result to a file (many options available !)
newMov.write_videofile("NewVideo.mp4")
