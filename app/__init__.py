from flask import Flask
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

from app.cards import bp as cards_bp
app.register_blueprint(cards_bp)

from app.lists import bp as lists_bp
app.register_blueprint(lists_bp)

from app.boards import bp as boards_bp
app.register_blueprint(boards_bp)

from app import create_db, routes, dbs
