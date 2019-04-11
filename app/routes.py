from app import app
from flask import jsonify, request, url_for
import random
import string
from app.dbs import Database
import uuid


def generate_random_string():
	rand = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])
	return rand


@app.route('/trillo/cards', methods=['GET'])
def get_cards():
	query = "SELECT * FROM card"
	result = {'items': Database().run_query(query)}
	print("Result: ", result)
	return jsonify(result)


@app.route('/trillo/cards/<id>', methods=['GET'])
def get_card(id):
	return 'Hello, World'


@app.route('/trillo/cards', methods=['POST'])
def create_card():
	"""data = request.get_json() or {}
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
	return response"""
	pass


@app.route('/trillo/card/<id>', methods=['PUT'])
def update_card(id):
	pass

