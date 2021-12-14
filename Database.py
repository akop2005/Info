from flask import Flask
import sys
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///second.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
class Clients(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    surname=db.Column(db.String(80),nullable=False)
    name=db.Column(db.String(80),nullable=False)
    phone_number=db.Column(db.String(80),nullable=True)
    
    def __repr__(self):
        return f'{self.id}{self.surname}{self.name}'

class Goods(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    good_name=db.Column(db.String(80),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    avaliable=db.Column(db.Integer,nullable=False)
    description=db.Column(db.String(300),nullable=True)

    def __repr__(self):
        return f'{self.id}{self.good_name}'

class Orders(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    client_id=db.Column(db.Integer,db.ForeignKey('clients.id'),nullable=False)
    client=db.relationship('clients',backref=db.backref('orders'))
    data=db.Column(db.DateTime,nullable=False)
    order_price=db.Column(db.Integer,nullable=True)
    good_id=db.Column(db.Integer,db.ForeignKey('goods.id'),nullable=False)
    good=db.relationship('goods',backref=db.backref('orders'))

    def __repr__(self):
        return f'{self.id}'
    


db.create_all()
client=Clients(sername='Watson',name='Richard')
sb.session.add(client)
db.session.commit()
#Courses.query.all()
