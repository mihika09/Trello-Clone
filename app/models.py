"""from app import db
# from flask import url_for


class PaginatedAPIMixin(object):
	@staticmethod
	def to_collection_dict(query, page, per_page, endpoint, **kwargs):
		resources = query.paginate(page, per_page, False)
		data = {
			'items': [item.to_dict() for item in resources.items],
			'_meta': {
				'page': page,
				'per_page': per_page,
				'total_pages': resources.pages,
				'total_items': resources.total
			},
			'_links': {
				'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
				'next': url_for(endpoint, page=page+1, per_page=per_page, **kwargs) if resources.has_next else None,
				'prev': url_for(endpoint, page=page-1, per_page=per_page, **kwargs) if resources.has_prev else None
			}
		}

		return data


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
	list_id = db.Column(db.String(10), db.ForeignKey('list.id'))

	def to_dict(self):
		data = {
			'id': self.id,
			'title': self.title,
			'description': self.title,
			'list_id': self.list_id
		}
		return data

	def from_dict(self, cid, data):
		setattr(self, 'id', cid)
		for field in ['title', 'description', 'list_id']:
			if field in data:
				setattr(self, field, data[field])"""
