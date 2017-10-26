# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm as Form

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import InputRequired, Email, EqualTo


# Define the login forms (WTForms)

class Search(Form):
    techno = StringField('Name of a specific technology')
    interval = StringField('Interval of time')


class StackoverflowForm(Form):
    tag = StringField('Name of a specific technology')


