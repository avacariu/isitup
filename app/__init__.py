from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.template_filters import backends
from social.apps.flask_app.models import init_social

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

app.register_blueprint(social_auth)
init_social(app, db)

lm = LoginManager()
lm.init_app(app)

from app import views, models, forms
