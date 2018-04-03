# coding:utf8
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://nan:test123456@139.196.102.39/movie_project"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)


# 会员登录日志
class Userlog(db.model):
    __tablename__ = "userlog"
