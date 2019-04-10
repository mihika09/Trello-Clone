from app import app
import random
import string


def generate_random_string():
	rand = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])
	return rand


@app.route('/')
def index():  # Login/ Registration
	return "Hello, World"
