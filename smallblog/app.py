from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from getpass import getpass


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
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
    return render_template('list_users.html', users=User.query.all())

@app.route("/home")
def get_home():
    return render_template('empty_template.html')

app.run(port=8000)
