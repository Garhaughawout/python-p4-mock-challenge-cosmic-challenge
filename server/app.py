#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return ''

@app.route('/scientists', methods=['GET'])
def get_scientists():
    scientists = Scientist.query.all()
    return jsonify([scientist.serialize() for scientist in scientists])

@app.route('/scientists', methods=['POST'])
def create_scientist():
    data = request.json
    scientist = Scientist(**data)
    db.session.add(scientist)
    db.session.commit()
    return jsonify(scientist.serialize())

@app.route('/scientists/<int:id>', methods=['GET'])
def get_scientist(id):
    scientist = Scientist.query.get(id)
    return jsonify(scientist.serialize()) 



if __name__ == '__main__':
    app.run(port=5555, debug=True)
