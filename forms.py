from flask import flash
from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, PasswordField
from wtforms.validators import Required, Length, EqualTo
from models import db, User

# Set your classes here.
class RegisterForm(Form):
    name = TextField(
        'Username', validators=[Required(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[Required(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[Required(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [Required(),
        EqualTo('password', message='Passwords Must Match')]
    )

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if Form.validate(self):
            user = User.query.filter_by(name = self.name.data.lower()).first()
            if user:
                flash("That username is already taken.")
                return False
            return True
        return False

class LoginForm(Form):
    name = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if Form.validate(self):
            user = User.query.filter_by(name = self.name.data.lower()).first()
            if user and user.password == self.password.data: return True
            else:
                flash("Invalid username or password.")
                return False
        return False
