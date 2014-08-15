from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), index=True, unique=True)
    openid = db.Column(db.String(200))
    things = db.relationship('Thing', backref='owner', lazy='dynamic')

    def __init__(self, email, openid):
        self.email = email
        self.openid = openid

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
