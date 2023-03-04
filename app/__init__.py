# This file defines the app package together with the directory it is in (app/)
# All variables in this file, like "app" in app = Flask(__name__) are members of this
# package "app"
from flask import Flask

app = Flask(__name__)

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# set configuration for Flask-app using the "app.config" dictionary.
# load all the attributes of Config class into it using from_object(...)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

# finally we import the routes package
from app import routes, models