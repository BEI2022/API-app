from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.properties_controller  import  properties_bp
from controllers.comment_controller import comments_bp
from controllers.feature_controller import feature_bp
from marshmallow.exceptions import ValidationError
import os





def create_app():
    app = Flask(__name__)

    @app.errorhandler(ValidationError) 
    def bad_request(err):
        return {'error' :err.message}, 400

    @app.errorhandler(400) 
    def bad_request(err):
        return {'error': str(err)}, 400

    @app.errorhandler(404) 
    def not_found(err):
        return {'error': str(err)}, 404

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    @app.errorhandler(KeyError)
    def Key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(properties_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(feature_bp)


    return app


