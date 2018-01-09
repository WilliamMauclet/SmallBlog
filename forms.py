from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from blog_config import *

class UsernamePasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class NewPostForm(Form):
    title = StringField('Title', validators=Length(min=5, max=MAX_POST_TITLE_LENGTH))
    text = StringField('Text', validators=[Length(min=20, max=MAX_POST_TITLE_LENGTH)])