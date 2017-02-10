from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object('config')
login_maneger = LoginManager()
login_maneger.init_app(app)

db = SQLAlchemy(app)
from app.controllers import default
