from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug.security import check_password_hash
from booknetwork import db
from booknetwork.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=24)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db.execute(
            "SELECT * FROM user WHERE username = :username",
            {"username": username.data}).fetchone()
        if user:
            return ValidationError('Username Taken')
    def validate_email(self, email):
        result = db.execute(
            "SELECT * FROM user WHERE username = :username",
            {"username": email.data}).fetchone()
        if result:
            return ValidationError('Email Taken')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    searchText = StringField('', validators=[DataRequired()])
        