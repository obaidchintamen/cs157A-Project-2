from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

<<<<<<< HEAD
@app.route('/')
def hello():
    return 'Hello World!'
=======
from app import routes
>>>>>>> 2d1dfd767f7a2728941968e354f67766b89ed666

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()