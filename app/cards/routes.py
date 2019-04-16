from app.cards import bp
from flask import jsonify, request, abort
from app.dbs import Database
import uuid
from app.cards.queries import CardQuery


# remove this later
@bp.route('/trillo/cards/', methods=['GET'])
def get_cards():
	query = CardQuery().get_all_cards()
	cards = Database().run_query(query)

	return jsonify({'cards': cards})


@bp.route('/trillo/cards/<id>', methods=['GET'])
def get_card(id):
	query = CardQuery().get_card_by_id(id)
	card = Database().run_query(query)

	if not card:
		abort(404)

	return jsonify({'cards': card})


@bp.route('/trillo/cards', methods=['POST'])
def create_card():

	data = request.get_json() or {}

	if 'title' not in data or 'list_id' not in data:
		abort(400)

	cid = str(uuid.uuid1())[0:9]
	data['id'] = cid

	query = CardQuery().add_card(data)
	Database().run_query(query)

	query = CardQuery().get_card_by_id(cid)
	card = Database().run_query(query)

	return jsonify({'cards': card}), 201


@bp.route('/trillo/cards/<id>', methods=['PUT'])
def update_card(id):

	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		abort(400)

	query = CardQuery().get_card_by_id(id)
	card = Database().run_query(query)

	if not card:
		abort(404)

	query = CardQuery().edit_card(data, id)
	Database().run_query(query)

	query = CardQuery().get_card_by_id(id)
	card = Database().run_query(query)

	return jsonify({'items': card})


@bp.route('/trillo/cards/<id>', methods=['DELETE'])
def delete_card(id):

	query = CardQuery().get_card_by_id(id)
	card = Database().run_query(query)
	if not card:
		abort(404)

	query = CardQuery().delete_card(id)
	Database().run_query(query)

	return "Delete successful"
