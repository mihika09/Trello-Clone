class Query:

	@staticmethod
	def get_all_lists():
		return "SELECT * FROM list"

	@staticmethod
	def get_list_by_id(id):
		return "SELECT * FROM list WHERE id = '{}'".format(id)

	@staticmethod
	def add_list(data):
		keys = ', '.join(key for key, _ in data.items())
		values = ', '.join("'{}'".format(value) if type(value) == str else str(value) for _, value in data.items())

		return "INSERT INTO list ({}) VALUES ({})".format(keys, values)

	@staticmethod
	def edit_list(data, id):
		keys = list([key for key, _ in data.items()])
		values = list(["'{}'".format(value) if type(value) == str else str(value) for _, value in data.items()])

		set = ', '.join("{}={}".format(key, value) for key, value in zip(keys, values))
		return "UPDATE list SET {} WHERE id = '{}'".format(set, id)

	@staticmethod
	def delete_list(id):
		return "DELETE FROM list WHERE id = '{}'".format(id)
