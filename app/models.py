"""from app import db


class Collection(object):
	@staticmethod
	def to_collection_dict(query):
		data = {
			'items': [item.to_dict() for item in query]
		}
		return data


class Board(db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	visibility = db.Column(db.String(32), index=True)
	cards = db.relationship('List', backref='board', cascade='all,delete', lazy='dynamic')


class List(db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	board_id = db.Column(db.String(10), db.ForeignKey('board.id'))
	items = db.relationship('Card', backref='list', cascade='all,delete', lazy='dynamic')


class Card(Collection, db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	description = db.Column(db.String(250))
	list_id = db.Column(db.String(10), db.ForeignKey('list.id'))"""
