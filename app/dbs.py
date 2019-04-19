import psycopg2
import psycopg2.extras
import sys
import logging
import psycopg2
import urllib.parse as urlparse
import os
from flask import abort


class Database:

	con = None

	def __init__(self):
		url = urlparse.urlparse(os.environ['DATABASE_URL'])
		self.db = url.path[1:]
		self.username = url.username
		self.password = url.password
		self.host = url.hostname
		self.port = url.port

	@staticmethod
	def to_dict(keys, result):
		res = {}
		for i in range(len(keys)):
			res[keys[i]] = result[i]

		return res

	def open_connection(self):

		"""try:
			if self.con is None:
				self.con = psycopg2.connect(dbname=self.db, user=self.username, host=self.host, port=self.port, password=self.password)

			elif not self.con.open:
				self.con = psycopg2.connect(dbname=self.db, user=self.username, host=self.host, port=self.port)"""

		try:
			Database.con = psycopg2.connect(dbname=self.db, user=self.username, host=self.host, port=self.port,
									password=self.password)
			print("Database connection opened")

		except:
			logging.error("ERROR: Could not connect to Postgres.")
			sys.exit()

	def run_query(self, query):

		result = []
		error = None

		try:
			if Database.con is None or Database.con.closed > 0:
				self.open_connection()

			cur = self.con.cursor(cursor_factory=psycopg2.extras.DictCursor)

			try:
				cur.execute(query)
				self.con.commit()

			except (Exception, psycopg2.DatabaseError) as e:
				print("Error#1: ", e)
				cur.execute("ROLLBACK")
				self.con.commit()
				error = 400
				abort(400)

			try:
				result = cur.fetchall()
				cur.close()
				if result:
					keys = list(result[0].keys())
					result = [self.to_dict(keys, row) for row in result]

			except(Exception, psycopg2.ProgrammingError) as e:
				print("Error#2: ", e)

		except (Exception, psycopg2.DatabaseError) as e:
			print("Error#3: ", e)
			if error is not None:
				abort(error)
			abort(500)

		"""finally:
			if self.con is not None:
				self.con.close()
				print('Database connection closed.')"""

		return result
