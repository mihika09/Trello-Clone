from flask import Blueprint

bp = Blueprint('boards', __name__)

from app.boards import routes