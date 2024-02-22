from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import Form, StringField, IntegerField, validators


class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa un nombre válido')
    ])
    email = StringField('email', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Email(message='Ingresa un email válido')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=30, message='Ingresa un apellido válido')
    ])
    amaterno = StringField('amaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa un apellido válido')
    ])
    edad = IntegerField('edad', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=120, message='Ingresa una edad válida')
    ])

