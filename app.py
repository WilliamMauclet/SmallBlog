from flask import Flask, render_template
from flask_login import LoginManager, current_user

from admin import admin
from models import db, User, Post, About, ContactInfo
from prefiller import prefill

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
admin.init_app(app)
db.init_app(app)


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


# TODO remove
@app.route("/users")
def users():
    if not current_user.is_authenticated:
        return home()
    return render_template('list_users.html', users=User.query.all())


# Initialize flask-login
def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


def create_admin():
    username = input("Admin username: ")
    password = getpass("Admin password: ")
    administrator = User(username=username, password=password)
    db.session.add(administrator)
    db.session.commit()


if __name__ == "__main__":
    # init db
    with app.app_context():
        db.create_all()
        if input('Prefill blog? [y/n] ') == 'y':
            prefill(db)

    # init login stuff
    init_login()
    app.run(port=80)
