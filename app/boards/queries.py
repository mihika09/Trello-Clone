class BoardQuery:

	@staticmethod
	def get_all_boards():
		return "SELECT * FROM board"

	@staticmethod
	def get_board_by_id(id):
		return "SELECT * FROM board WHERE id = '{}'".format(id)

	@staticmethod
	def create_board(data):
		keys = ', '.join(key for key, _ in data.items())
		values = ', '.join("'{}'".format(value) if type(value) == str else str(value) for _, value in data.items())

		return "INSERT INTO board ({}) VALUES ({})".format(keys, values)

	@staticmethod
	def update_board(data, id):
		keys = list([key for key, _ in data.items()])
		values = list(["'{}'".format(value) if type(value) == str else str(value) for _, value in data.items()])

		set = ', '.join("{}={}".format(key, value) for key, value in zip(keys, values))
		return "UPDATE board SET {} WHERE id = '{}'".format(set, id)

	@staticmethod
	def delete_board(id):
		return "DELETE FROM board WHERE id = '{}'".format(id)
