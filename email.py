import sendgrid

def sendEmail(email):
	sg = sendgrid.SendGridClient('JLDevOps', 'apples1!')
	message = sendgrid.Mail(to= email, subject='I KNOW WHAT YOU HAVE DONE', html='Body', text='I KNOW WHAT YOU HAVE DONE', from_email='destinesavior@gmail.com')status, msg = sg.send(message)