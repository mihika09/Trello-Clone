from app.lists import bp
from app.lists.queries import Query
from app.dbs import Database
from flask import jsonify, request, abort
from app.cards.queries import CardQuery
import uuid


@bp.route('/trillo/lists/<id>/cards', methods=['GET'])
def get_list(id):
	query = Query().get_list_by_id(id)
	list = Database().run_query(query)

	if not list:
		abort(404)

	query = CardQuery().get_list_cards(id)
	list[0]['cards'] = Database().run_query(query)

	return jsonify({'lists': list})


@bp.route('/trillo/lists', methods=['POST'])
def create_list():
	data = request.get_json() or {}

	if 'title' not in data or 'board_id' not in data:
		abort(400)

	cid = str(uuid.uuid1())
	data['id'] = cid

	query = Query().add_list(data)
	Database().run_query(query)

	query = Query().get_list_by_id(cid)
	list = Database().run_query(query)

	return jsonify({'lists': list}), 201


@bp.route('/trillo/lists/<id>', methods=['PUT'])
def update_list(id):
	data = request.get_json() or {}

	if not data:
		abort(400)

	query = Query().get_list_by_id(id)
	list = Database().run_query(query)

	if not list:
		abort(404)

	query = Query().edit_list(data, id)
	Database().run_query(query)

	query = Query().get_list_by_id(id)
	list = Database().run_query(query)

	return jsonify({'lists': list})


@bp.route('/trillo/lists/<id>', methods=['DELETE'])
def delete_list(id):
	query = Query().get_list_by_id(id)
	list = Database().run_query(query)

	if not list:
		abort(404)

	query = Query().delete_list(id)
	Database().run_query(query)

	return "Delete successful"
