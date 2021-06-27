from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRES_URI)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://atya:14091989@127.0.0.1:5432/flask'
db = SQLAlchemy(app)

from app import views
