from flask import Flask, render_template
from flask_login import LoginManager, current_user

from admin import admin
from models import db, User, Post, About, ContactInfo

app = Flask(__name__)
# config
app.config.from_object('config')
app.config.from_pyfile('config.py')
# admin screen
admin.init_app(app)
# database
db.init_app(app)
# login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route("/")
def home():
    posts = Post.query.order_by(Post.date.desc())
    return render_template('home.html', posts=posts, context='home')


@app.route("/about")
def about():
    about = About.query.order_by(About.date.desc()).first()
    return render_template('about.html', about=about, context='about')


@app.route("/contact")
def contact():
    contact_infos = ContactInfo.query.all()
    return render_template('contact.html', contact_infos=contact_infos, context='contact')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post, context='home')


if __name__ == "__main__":
    app.run(port=80)
