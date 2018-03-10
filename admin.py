from flask import url_for, request, flash, get_flashed_messages

from flask_admin import Admin, AdminIndexView, expose, helpers
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from flask_wtf import validators
from wtforms import StringField, PasswordField, form
from wtforms.validators import DataRequired

from models import db, User, Post, ContactInfo, About

import os.path as op


# Define login and registration forms (for flask-login)
class AdminLoginForm(form.Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    # all functions with the name "validate_<something>" are tested by wtforms/form.py
    def validate_password(self, field):
        user = self.get_user()

        if user is None or not user.check_password(self.password.data):
            flash('Invalid user or password')
            raise validators.ValidationError()

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()


class AuthenticatedModelView(ModelView):

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


# create admin
admin = Admin(name='smallblog',
              index_view=MyAdminIndexView(),
              template_mode='bootstrap3',
              base_template='admin/master.html')

# add view for posts
admin.add_view(AuthenticatedModelView(Post, db.session))
admin.add_view(AuthenticatedModelView(About, db.session))
admin.add_view(AuthenticatedModelView(ContactInfo, db.session))

# add static path
path = op.join(op.dirname(__file__), 'static/added')
admin.add_view(FileAdmin(path, '/static/added', name='Static Files'))
