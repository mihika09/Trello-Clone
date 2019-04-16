from flask import Blueprint

bp = Blueprint('lists', __name__)

from app.lists import routes
