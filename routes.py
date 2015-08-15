from flask import Flask, render_template, flash


SECRET_KEY = 'ayylmao'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	return render_template('home.html')


if __name__ == "__main__": 
	app.run(debug=True)