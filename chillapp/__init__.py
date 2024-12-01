from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os

from flask_login import LoginManager


app = Flask(__name__, instance_relative_config=True)



app.config.from_mapping(
    SECRET_KEY = 'fd0d31e1b327f2ecd3ad42cd22d71690 ',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
login_manager.login_message="Nuh uh thats not very chill of you, please login first"

from chillapp import routes