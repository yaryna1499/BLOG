from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import os

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Import routes after initializing migration
from routes import *

if __name__ == "__main__":
    # Create tables in DB if not exist
    with app.app_context():
        db.create_all()
    app.run(host="localhost", port=5050, debug=True)
