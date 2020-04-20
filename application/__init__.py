import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# Constants
LOCAL_SQLITE_FILENAME = 'db.sqlite3'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + LOCAL_SQLITE_FILENAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
if os.environ.get('FLASK_ENV') == 'development' and not os.path.isfile(LOCAL_SQLITE_FILENAME):
    db.create_all()

bcrypt = Bcrypt(app)