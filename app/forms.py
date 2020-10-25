from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class registerForm(FlaskForm):
	nombre = TextField(validators=[DataRequired(), Length(min=1)])

	email = StringField(validators=[DataRequired(), Email()])

	password = PasswordField(validators=[DataRequired(), Length(min=8, max=16)])

	confirmpassword = PasswordField(validators=[DataRequired(), EqualTo('password'), Length(min=8, max=16)])

	enviar = SubmitField('Registrar Usuario')

	def validate_nombre(self, nombre):
		user = User.query.filter_by(nombre=nombre.data).first()
		if user:
			raise ValidationError('Usuario Existente, intente con otro Nombre')

	def validare_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Correo Existente, intente con otro.')

class LoginForm(FlaskForm):
	email = StringField(validators=[DataRequired(), Email()])

	password = PasswordField(validators=[DataRequired(), Length(min=8, max=16)])

	remember = BooleanField('Mantener la Sesión Iniciada')

	enviar = SubmitField('Iniciar Sesión')
