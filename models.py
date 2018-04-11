from datetime import datetime

import markdown
from flask import url_for
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
from mdx_gfm import GithubFlavoredMarkdownExtension
from sqlalchemy import PickleType
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from blog_config import MAX_POST_TITLE_LENGTH, MAX_USERNAME_LENGTH
from blog_config import MAX_PASSWORD_LENGTH, MAX_POST_INTRO_LENGTH

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_USERNAME_LENGTH),
                         unique=True, nullable=False)
    hashed_pw = db.Column(db.String(MAX_PASSWORD_LENGTH),
                          unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.hashed_pw = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_pw, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(MAX_POST_TITLE_LENGTH),
                      unique=True, nullable=False)
    intro = db.Column(db.String(MAX_POST_INTRO_LENGTH), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    image = db.Column(db.String, default=None)  # TODO default=None ????
    # Standard value = time of creation
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title='', intro='', text='', image=''):
        self.title = title
        self.intro = intro
        self.text = text
        self.image = image

    def get_intro(self):
        return from_markdown(self.intro)

    def get_text(self):
        return from_markdown(self.text)

    def get_url(self):
        return redirect('/post/{}'.format(self.id))

    def has_image(self):
        return self.image != None

    def get_image(self):
        return url_for('static', filename='added/'+self.image)

    def get_date(self):
        return pretty_print_date(self.date)

    def __repr__(self):
        return '<Post %r>' % self.title


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, unique=True, nullable=False)
    image = db.Column(db.String)
    # Standard value = time of creation
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, text='', image=''):
        self.text = text
        self.image = image

    def get_text(self):
        return from_markdown(self.text)

    def has_image(self):
        return self.image != None

    def get_image(self):
        return url_for('static', filename='added/'+self.image)

    def get_date(self):
        return pretty_print_date(self.date)

    def __repr__(self):
        return '<About %r' % self.date.strftime('%Y-%m-%d %H:%M:%S')


class ContactInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, unique=True, nullable=False)
    value = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, key='', value=''):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<ContactInfo>'


def from_markdown(text):
    return Markup(markdown.markdown(text, extensions=[GithubFlavoredMarkdownExtension()]))


def pretty_print_date(datetime):
    return datetime.strftime('%Y-%m-%d %H:%M')
