import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from application import constants

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + constants.LOCAL_SQLITE_FILENAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from application.models import User


if os.environ.get('FLASK_ENV') == 'development' and not os.path.isfile(constants.LOCAL_SQLITE_FILENAME):
    db.create_all()
