from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '23665c64bfbb07f4a55c1893136e966d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\pedro\\OneDrive\\Escritorio\\intranet\\datos.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes

