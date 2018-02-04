from flask import Flask, render_template
from flask_login import LoginManager, current_user

from models import db, User, Post, About, ContactInfo
from admin import admin

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
admin.init_app(app)
db.init_app(app)


@app.route("/")
def home():
    return render_template('home.html', posts=Post.query.order_by(Post.date.desc()))


@app.route("/about")
def about():
    return render_template('about.html', about=About.query.order_by(About.date.desc()).first())


@app.route("/contact")
def contact():
    return render_template('contact.html', contact_infos=ContactInfo.query.all())


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template('post.html', post=Post.query.get(post_id))


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
    # password = getpass("Admin password: ") # TODO PYCHARM PROBLEM
    password = input("Admin password: ")
    administrator = User(username=username, password=password)
    db.session.add(administrator)
    db.session.commit()


# init db
with app.app_context():
    db.create_all()
    if input('Create a new admin? [y/n] ') == 'y':
        create_admin()

# init login stuff
init_login()

app.run(port=5000)
