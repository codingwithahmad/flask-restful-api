import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	app.config.from_mapping(
		SECRET_KEY=os.environ.get('SECRET_KEY'),
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
	)	

	db.init_app(app)

	from . import api 
	app.register_blueprint(api.api_blueprint)

	return app