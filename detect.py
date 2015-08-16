from PIL import Image
import stepic
import sys
import os

from moviepy.editor import *
import moviepy.editor as mpy 
from moviepy.editor import VideoFileClip
import sendgrid

def main():
	os.chdir("../detect-pirates/test_videos")
	print('\n')

	for filename in os.listdir(os.getcwd()):
		if filename.endswith(".avi") or filename.endswith(".mp4"):
			secret = decrypt_video(filename)
			print("DECODED MESSAGE from %s: "%filename, secret)

			if secret in USERS.keys():
				email = USERS[secret]
				print("Sending 'friendly' email to ", email, "\n")
				sendEmail(email, filename)
			else:
				print("\n")



############ LOADING FROM DB ################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

os.chdir("../webapp")
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref

class User(Base):
    __table__ = Base.metadata.tables['users']



from sqlalchemy.orm import scoped_session, sessionmaker, Query
db_session = scoped_session(sessionmaker(bind=engine))

USERS = {item[0]:item[1] for item in db_session.query(User.name, User.email)}

print("USERS LIST: ", USERS)



def decrypt_video(filename, t0=56):
	vid = VideoFileClip(filename)

	vid.save_frame("frame.png", t=t0+0.05)

	img = Image.open("frame.png").convert(mode='RGB')
	msg = stepic.decode(img)

	return msg 

def sendEmail(email, filename):
	sg = sendgrid.SendGridClient('JLDevOps', 'apples1!')
	message = sendgrid.Mail(to= email, 
							subject='PIRACY NOTICE',
						 	html='You pirated the file %s. Piracy is illegal. \
						 		  Cease immediatly or face legal action. \
						 		  <br>-Scurvy'%filename, 
						 	from_email='destinesavior@gmail.com')
	msg = sg.send(message)

if __name__ == "__main__": main()
