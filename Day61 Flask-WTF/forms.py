from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(message = "Invalid email address")])
    password = PasswordField('password', validators=[DataRequired(), Length(min=7)])
    submit =SubmitField("Log In")