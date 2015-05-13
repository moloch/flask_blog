__author__ = 'Dario Coco'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
migrate = Migrate(app, db)
manager = Manager(app)
