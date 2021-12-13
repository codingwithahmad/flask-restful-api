from flask import Blueprint
from . import db
from .models import Post
from sqlalchemy import Column, Integer, String, DateTime
from flask_restful import Resource, Api
from sqlalchemy.sql import func


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class Index(Resource):

	def get(self):
		return {'message': 'Hello'}

api.add_resource(Index, '/api')


