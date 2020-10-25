from datetime import datetime
from __main__ import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	maquinas = db.relationship('Maquinas', backref='user', lazy=True)


	def __repr__(self):
		return f"User('{self.nombre}', '{self.email}', '{self.image_file}')"

class Maquinas(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tipoGrua = db.Column(db.String(100), nullable=False)
	marca = db.Column(db.String(100), nullable=False)
	modelo = db.Column(db.String(100), nullable=False)
	serie = db.Column(db.String(100), nullable=False)
	combustible = db.Column(db.String(100), nullable=False)
	patente = db.Column(db.String(100), nullable=False)
	neumatico = db.Column(db.String(100), nullable=False)
	motor = db.Column(db.String(100), nullable=False)
	fechaRegistro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"User('{self.tipoGrua}', '{self.marca}', '{self.modelo}', '{self.serie}', '{self.combustible}', '{self.patente}', '{self.neumatico}', '{self.motor}', '{self.fechaRegistro}')"