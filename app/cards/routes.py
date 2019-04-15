from app.cards import bp
from flask import jsonify, request, render_template
from app.dbs import Database
import uuid
from app.cards.queries import Query


@bp.route('/trillo/cards/', methods=['GET'])
def get_cards():
	query = Query().get_all_cards()
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['GET'])
def get_card(id):
	query = Query().get_card_by_id(id)
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards', methods=['POST'])
def create_card():

	data = request.get_json() or {}
	print(type(data))
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title and list_id of the card'
	cid = str(uuid.uuid1())[0:9]
	data['id'] = cid

	query = Query().add_card(data)
	Database().run_query(query)

	query = Query().get_card_by_id(cid)
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['PUT'])
def update_card(id):

	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title and list_id of the card'

	query = Query().edit_card(data, id)
	Database().run_query(query)

	query = Query().get_card_by_id(id)
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['DELETE'])
def delete_card(id):

	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title and list_id of the card'

	query = Query().delete_card(id)

	Database().run_query(query)

	query = Query().get_card_by_id(id)
	result = Database().run_query(query)
	if not result:
		return "Successfully Deleted the item"
	else:
		return "Delete unsuccessful"
