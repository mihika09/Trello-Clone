class Query:

	@staticmethod
	def get_all_cards():
		return "SELECT * FROM card"

	@staticmethod
	def get_card_by_id(id):
		return "SELECT * FROM card WHERE id = '{}'".format(id)

	@staticmethod
	def add_card(data):
		keys = ', '.join(key for key, _ in data.items())
		values = ', '.join("'{}'".format(value) if type(value) == str else str(value) for _, value in data.items())

		return "INSERT INTO card ({}) VALUES ({})".format(keys, values)

	@staticmethod
	def edit_card(data, id):
		keys = list([key for key, _ in data.items()])
		values = list(["'{}'".format(value) if type(value) == str else str(value) for _, value in data.items()])

		set = ', '.join("{}={}".format(key, value) for key, value in zip(keys, values))
		return "UPDATE card SET {} WHERE id = '{}'".format(set, id)

	@staticmethod
	def delete_card(id):
		return "DELETE FROM card WHERE id = '{}'".format(id)
