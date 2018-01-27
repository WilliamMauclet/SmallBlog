from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from blog_config import MAX_POST_TITLE_LENGTH, MAX_USERNAME_LENGTH, MAX_PASSWORD_LENGTH

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_USERNAME_LENGTH), unique=True, nullable=False)
    hashed_pw = db.Column(db.String(MAX_PASSWORD_LENGTH), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.hashed_pw = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_pw, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(MAX_POST_TITLE_LENGTH), unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    # Standard value = time of creation
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, unique=True, nullable=False)
    # Standard value = time of creation
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<About %r' % self.date.strftime('%Y-%m-%d %H:%M:%S')