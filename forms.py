from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField,SubmitField, SelectField, RadioField, DecimalField, validators, ValidationError, BooleanField, PasswordField, TextAreaField, SelectMultipleField, widgets, SelectMultipleField, widgets
from wtforms.validators import DataRequired, NumberRange, Email, Length, EqualTo, Optional, InputRequired


class userForm(Form):
    matricula = StringField('Matricula')
    edad = IntegerField('Edad')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('correo')