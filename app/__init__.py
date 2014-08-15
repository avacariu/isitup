from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
oid = OpenID(app, safe_roots=[])

from app import views, models, forms
