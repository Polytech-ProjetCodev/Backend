from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codev_back_user:W?9422$8+},3>3378@localhost:3306/codev_back'
db = SQLAlchemy(app)

db.create_all()

class user(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   mail_address = db.Column(db.String(50))

def __init__(self, name, mail_address):
   self.name = name
   self.mail_address = mail_address