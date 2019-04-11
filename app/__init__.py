from flask import Flask
import os
# import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

"""con = psycopg2.connect("dbname='trillodb' user='mallikamohta' host='localhost' port=5432")
cur = con.cursor()
cur.execute("create table person (id BIGSERIAL NOT NULL PRIMARY KEY, first_name VARCHAR(50) NOT NULL);")
cur.execute("SELECT * FROM person")
items = cur.fetchall()
con.commit()
cur.close()
con.close()"""

from app import routes
