from app import db
from social.apps.flask_app.default import models
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    things = db.relationship('Thing', backref='owner', lazy='dynamic')
    active = db.Column(db.Boolean, default=True)

    def __init__(self, email, username="Nameless"):
        self.email = email
        self.username = username

    def is_active(self):
        return self.active

    def __repr__(self):
        return '<User %r>' % (self.email)


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    uuid = db.Column(db.String(36), index=True, unique=True)
    name = db.Column(db.String(100))
    delta = db.Column(db.Integer)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, delta, uuid):
        self.name = name
        self.delta = delta
        self.uuid = uuid
