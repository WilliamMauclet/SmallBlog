from flask import Flask, render_template, url_for, request

from flask_admin import Admin, AdminIndexView, expose, helpers
from flask_admin.contrib.sqla import ModelView

from flask_login import current_user, login_user, logout_user, LoginManager
from werkzeug.utils import redirect

from flask_wtf import validators
from wtforms import StringField, PasswordField, form
from wtforms.validators import DataRequired

from models import db, User, Post

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db.init_app(app)


# Define login and registration forms (for flask-login)
class AdminLoginForm(form.Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    # all functions with the name "validate_<something>" are tested by wtforms/form.py
    def validate_password(self, field):
        user = self.get_user()

        if user is None or not user.check_password(self.password.data):
            raise validators.ValidationError('Invalid user or password')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()


class PostModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = AdminLoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


@app.route("/")
def home():
    return render_template('posts.html', posts=Post.query.all())


@app.route("/users")
def users():
    return render_template('list_users.html', users=User.query.all())  # .all()


@app.route("/contact")
def contact():
    raise NotImplementedError("TODO")


@app.route("/about")
def about():
    raise NotImplementedError("TODO")


@app.route("/test")
def test():
    return render_template('test_responsive.html')


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
    # password = getpass("Admin password: ") PYCHARM PROBLEM
    password = input("Admin password: ")
    administrator = User(username=username, password=password)
    db.session.add(administrator)
    db.session.commit()


init_login()

# create admin
admin = Admin(app,
              name='smallblog',
              index_view=MyAdminIndexView(),
              template_mode='bootstrap3',
              base_template='admin/master.html')

# add view for posts
admin.add_view(ModelView(Post, db.session))

# init db
with app.app_context():
    db.create_all()
    create_admin()

app.run(port=8000)
