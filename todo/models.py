from . import db


# initial database models


class User(db.Model):
	'''This is a user model for authentication'''
	__tabelname__ = 'todo_users'

	id = Column(Integer, primary_key=True)
	username = Column(String(32), nullable=False, unique=True)
	password = Column(String(128), nullable=False)

class Post(db.Model):
	'''This is Task model for describe task and create task object
	'''
	__tabelname__ = 'Post'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	description = Column(String(255), nullable=False)
	created =  Column(DateTime(timezone=True), server_default=func.now())
	updated =  Column(DateTime(timezone=True), onupdate=func.now())