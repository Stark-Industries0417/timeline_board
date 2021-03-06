import os
from flask import Flask
from api import board
from db_connect import db
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(board)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://root:{os.getenv('password')}@localhost/free_board"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "asodfajsdofijac"

db.init_app(app)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(debug=True)


# "0.0.0.0", 5000,
