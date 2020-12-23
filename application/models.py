from application import db
from datetime import datetime

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    shop_id = db.Column('shop_id', db.Integer, db.ForeignKey('shop.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    books = db.relationship('Books', backref='users')

class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    books = db.relationship('Books', backref='shops')

