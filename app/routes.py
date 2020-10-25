from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import registerForm, LoginForm
from app.models import User, Maquinas
from flask_login import login_user, current_user

@app.route('/')
def index():
	return render_template('index.html', title="Intranet")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash(f'Bienvenido')
			return redirect(url_for('main'))

		else:
			flash(f'Correo o Contraseña Incorrecta, favor verificar los datos ingresados')
		
	return render_template('login.html', title="Registrar Usuario", form=form)
	
@app.route('/main')
def main():
	return render_template('main.html', title="Menú Principal")

@app.route('/camiones.html')
def camiones():
    return render_template('camiones.html', title="Camiones")

@app.route('/maquinas.html')
def maquinas():
    return render_template('maquinas.html', title="Máquinas") 

@app.route('/registro', methods=['GET', 'POST'])
def registro():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = registerForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(nombre=form.nombre.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Cuenta creada correctamente ')
		return redirect(url_for('login'))
	return render_template('registro.html', title="Registrar Usuario", form=form)