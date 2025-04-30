from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HudsonWayne'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobboard.db'
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .routes import main
    app.register_blueprint(main)
    
    from jobboard.routes.auth import auth
    app.register_blueprint(auth)
    
    return app