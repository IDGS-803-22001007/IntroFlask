from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField, SelectField, RadioField, DecimalField, validators, ValidationError, BooleanField, PasswordField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, NumberRange, Email, Length, EqualTo, Optional, InputRequired

class userForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired("Este campo es requerido"),
    ])
    
    edad = IntegerField('Edad', [
        validators.DataRequired("Este campo es requerido")
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired("Este campo es requerido")
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired("Este campo es requerido")
    ])

    email = EmailField('correo', [
        validators.Email("Ingrese un correo valido")
    ])