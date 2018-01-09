from flask import Flask, render_template, url_for   
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from getpass import getpass
from blog_config import *
from forms import *


app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_USERNAME_LENGTH), unique=True, nullable=False)
    password = db.Column(db.String(MAX_PASSWORD_LENGTH), unique=False, nullable=False)
    email = db.Column(db.String(MAX_EMAIL_LENGTH), unique=True, nullable=False)

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

def create_admin():
    username = input("Admin username: ")
    password = getpass("Admin password: ")
    email = input("Admin email: ")
    admin = User(username=username, password=password, email=email)
    db.session.add(admin)
    db.session.commit()

db.create_all()
create_admin()

@app.route("/users")
def get_users():
    return render_template('list_users.html', users=User.query.all()) #.all()

@app.route("/home")
def get_home():
    return render_template('empty_template.html')

@app.route("/login")
def get_login_page():
    return render_template('login.html')

@app.route("/verify_login")
def login():
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        # Check the password and log the user in
        # [...]
        User.query.filter_by(username=form.username).first()

        return redirect(url_for('/home'))
    return render_template('login.html', form=form)

print(User.query.filter_by(username='a').first())
app.run(port=8000)
