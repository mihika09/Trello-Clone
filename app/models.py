"""from app import db


class Board(db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	visibility = db.Column(db.String(32), index=True)
	cards = db.relationship('Card', backref='board', cascade='all,delete', lazy='dynamic')


class Card(db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	board_id = db.Column(db.String(10), db.ForeignKey('board.id'))
	items = db.relationship('List', backref='card', cascade='all,delete', lazy='dynamic')


class List(db.Model):
	id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(64))
	description = db.Column(db.String(250))
	card_id = db.Column(db.String(10), db.ForeignKey('card.id'))"""
