from app.boards import bp
from app.boards.queries import BoardQuery
from app.dbs import Database
from flask import request, abort, jsonify
import uuid
from app.lists.queries import Query
from app.cards.queries import CardQuery


@bp.route('/trillo/boards', methods=['GET'])
def get_boards():
	query = BoardQuery().get_all_boards()
	boards = Database().run_query(query)

	return jsonify({'boards': boards})


@bp.route('/trillo/boards/<id>/lists', methods=['GET'])
def get_board(id):
	query = BoardQuery().get_board_by_id(id)
	board = Database().run_query(query)

	if not board:
		abort(404)

	query = Query().get_board_lists(id)
	lists = Database().run_query(query)
	for l in lists:
		query = CardQuery().get_list_cards(l['id'])
		l['cards'] = Database().run_query(query)

	board[0]['lists'] = lists
	return jsonify({'boards': board})


@bp.route('/trillo/boards', methods=['POST'])
def create_board():
	data = request.get_json() or {}

	if 'title' not in data:
		abort(400)

	cid = str(uuid.uuid1())
	data['id'] = cid

	query = BoardQuery().create_board(data)
	Database().run_query(query)

	query = BoardQuery().get_board_by_id(cid)
	board = Database().run_query(query)

	return jsonify({'boards': board}), 201


@bp.route('/trillo/boards/<id>', methods=['PUT'])
def update_board(id):
	data = request.get_json() or {}

	if not data:
		abort(400)

	query = BoardQuery().get_board_by_id(id)
	board = Database().run_query(query)

	if not board:
		abort(404)

	query = BoardQuery().update_board(data, id)
	Database().run_query(query)

	query = BoardQuery().get_board_by_id(id)
	board = Database().run_query(query)

	return jsonify({'boards': board})


@bp.route('/trillo/boards/<id>', methods=['DELETE'])
def delete_board(id):
	query = BoardQuery().get_board_by_id(id)
	board = Database().run_query(query)

	if not board:
		abort(404)

	query = BoardQuery().delete_board(id)
	Database().run_query(query)

	return "Delete successful"


