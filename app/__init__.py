from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()