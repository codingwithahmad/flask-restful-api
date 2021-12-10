from flask import Blueprint
from . import db
from sqlalchemy import Column, Integer, String
from flask_restful import Resource, Api


main = Blueprint('main', __name__)
api = Api(main)


class User(db.Model):
	__tabelname__ = 'todo_users'

	id = Column(Integer, primary_key=True)
	username = Column(String(32), nullable=False, unique=True)
	password = Column(String(128), nullable=False)


class Index(Resource):

	def get(self):
		return {'message': 'Hello'}

api.add_resource(Index, '/')
