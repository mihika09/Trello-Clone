import psycopg2
import psycopg2.extras
import sys
import logging


class Database:

	def __init__(self):
		self.username = 'mallikamohta'
		self.host = 'localhost'
		self.port = 5432
		self.db = 'trillodb'
		self.con = None

	@staticmethod
	def to_dict(keys, result):
		res = {}
		for i in range(len(keys)):
			res[keys[i]] = result[i]

		return res

	def open_connection(self):

		try:
			if self.con is None:
				self.con = psycopg2.connect(dbname=self.db, user=self.username, host=self.host, port=self.port)

			elif not self.con.open:
				self.con = psycopg2.connect(dbname=self.db, user=self.username, host=self.host, port=self.port)

		except:
			logging.error("ERROR: Could not connect to Postgres.")
			sys.exit()

	def run_query(self, query):

		print("#######################################")
		print("Query: ", query)
		print("#######################################")
		result = []
		try:
			self.open_connection()
			cur = self.con.cursor(cursor_factory=psycopg2.extras.DictCursor)
			cur.execute(query)
			self.con.commit()
			try:
				result = cur.fetchall()
				cur.close()
				if result:
					keys = list(result[0].keys())
					result = [self.to_dict(keys, row) for row in result]

			except(Exception, psycopg2.ProgrammingError) as error:
				pass

		except (Exception, psycopg2.DatabaseError) as error:
			print("Error: ", error)

		finally:

			if self.con is not None:
				self.con.close()
				print('Database connection closed.')

		return result
