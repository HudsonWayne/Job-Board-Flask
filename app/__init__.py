from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Create extension instances
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Config settings
    app.config['SECRET_KEY'] = 'HudsonWayne'  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobboard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.routes.auth import auth

    app.register_blueprint(auth)

    return app
