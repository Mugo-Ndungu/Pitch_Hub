from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(100))
    pitches_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    interview = db.Column(db.String(1000))
    product = db.Column(db.String(1000))
    funds = db.Column(db.String(1000))
    business = db.Column(db.String(1000))
    sales = db.Column(db.String(1000))
    users = db.relationship('User', backref = 'pitch', lazy="dynamic")

    def __repr__(self):
        return f'User {self.pitch}'
