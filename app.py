import logging, os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
from models import db
from forms import *

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# Login required decorator.
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'name' in session:
            return test(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/videos')
@login_required
def videos():
    return render_template('pages/videos.html')

@app.route('/watch')
@login_required
def watch():
    return render_template('pages/watch.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('forms/login.html', form=form)
        else:
            newuser = User(form.name.data, form.email.data, form.password.data)
            session['name'] = newuser.name
            db.session.add(newuser)
            db.session.commit()
            flash(u'Successfully Logged In')
            return redirect(url_for('videos'))
    elif request.method == 'GET':
        return render_template('forms/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('forms/register.html', form=form)
        else:
            newuser = User(form.name.data, form.email.data, form.password.data)
            session['name'] = newuser.name
            db.session.add(newuser)
            db.session.commit()
            flash(u'Successfully Registered')
            return redirect(url_for('videos'))
    elif request.method == 'GET':
        return render_template('forms/register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
