from app.cards import bp
from flask import jsonify, request, render_template
from app.dbs import Database
import uuid


@bp.route('/trillo/cards/', methods=['GET'])
def get_cards():
	query = "SELECT * FROM card"
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['GET'])
def get_card(id):
	query = "SELECT * FROM card WHERE id = '{}'".format(id)
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

	keys = ', '.join(key for key, _ in data.items())
	values = ', '.join("'{}'".format(value) if type(value) == str else str(value) for _, value in data.items())

	query = "INSERT INTO card ({}) VALUES ({})".format(keys, values)
	Database().run_query(query)

	query = "SELECT * FROM card WHERE id = '{}'".format(cid)
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['PUT'])
def update_card(id):

	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title and list_id of the card'

	keys = list([key for key, _ in data.items()])
	values = list(["'{}'".format(value) if type(value) == str else str(value) for _, value in data.items()])

	set = ', '.join("{}={}".format(key, value) for key, value in zip(keys, values))
	query = "UPDATE card SET {} WHERE id = '{}'".format(set, id)

	Database().run_query(query)

	query = "SELECT * FROM card WHERE id = '{}'".format(id)
	result = {'items': Database().run_query(query)}
	return jsonify(result)


@bp.route('/trillo/cards/<id>', methods=['DELETE'])
def delete_card(id):

	data = request.get_json() or {}
	if 'title' not in data or 'list_id' not in data:
		return 'Bad Request: Must include title and list_id of the card'

	query = "DELETE FROM card WHERE id = '{}'".format(id)

	Database().run_query(query)

	query = "SELECT * FROM card WHERE id = '{}'".format(id)
	result = Database().run_query(query)
	if not result:
		return "Successfully Deleted the item"
	else:
		return "Delete unsuccessful"
