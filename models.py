from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from random import randint

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    num = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name.lower()
        self.email = email.lower()
        self.password = password
        self.num = randint(2,58)
