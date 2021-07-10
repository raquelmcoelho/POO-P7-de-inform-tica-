from flask import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = '12345'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://Raquel:12345678@127.0.0.1:3306/av07"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO "] = True

from __Avaliação07.application.Controller.default import *