from flask import Flask

def create_app(app):
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://property_api_dev:password1234@127.0.0.1:5432/property_api'