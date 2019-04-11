from app import app, db
from flask import jsonify, request, url_for
import random
import string
from app.models import Card
import uuid


def generate_random_string():
	rand = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])
	return rand


@app.route('/trillo/cards/<id>', methods=['GET'])
def get_card(id):
	# return 'Hello, World'
	return jsonify(Card.query.get_or_404(id).to_dict())


@app.route('/trillo/cards', methods=['GET'])
def get_cards():
	page = request.args.get('page', 1, type=int)
	per_page = min(request.args.get('per_page', 100, type=int), 100)
	data = Card.to_collection_dict(Card.query, page, per_page, 'get_cards')
	return jsonify(data)
	pass


@app.route('/trillo/cards', methods=['POST'])
def create_card():
	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title of the card'
	cid = str(uuid.uuid1())
	cid = cid[0:9]
	card = Card()
	card.from_dict(cid, data)
	db.session.add(card)
	db.session.commit()
	response = jsonify(card.to_dict())
	response.status_code = 201
	response.headers['Location'] = url_for('get_card', id=card.id)
	return response


@app.route('/trillo/card/<id>', methods=['PUT'])
def update_card(id):
	pass
