from flask import Flask
import os
import psycopg2

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

con = psycopg2.connect("dbname='trillodb' user='mallikamohta' host='localhost' port=5432")
cur = con.cursor()
cur.execute("create table person (id BIGSERIAL NOT NULL PRIMARY KEY, first_name VARCHAR(50) NOT NULL);")
cur.execute("SELECT * FROM person")
items = cur.fetchall()
con.commit()
cur.close()
con.close()

from app import routes
