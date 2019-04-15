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
