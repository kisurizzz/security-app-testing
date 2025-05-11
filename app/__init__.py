# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
import secrets

# Initialize Flask extensions
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = secrets.token_hex(32)  # Generate a secure secret key
    app.config['WTF_CSRF_ENABLED'] = True
    
    # Initialize Talisman for security headers
    Talisman(app,
        content_security_policy={
            'default-src': "'self'",
            'script-src': "'self'",
            'style-src': "'self'",
            'img-src': "'self'",
            'font-src': "'self'",
        },
        force_https=False,  # Set to True in production
        strict_transport_security=True,
        session_cookie_secure=True,
        feature_policy={
            'geolocation': "'none'",
            'camera': "'none'",
            'microphone': "'none'",
            'payment': "'none'",
            'usb': "'none'"
        }
    )
    
    # Initialize CSRF protection
    csrf.init_app(app)
    
    # Initialize extensions with app
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()  # This will only create tables if they don't exist
        
        # Add initial user if it doesn't exist
        from app.models import User
        if not User.query.filter_by(username='admin').first():
            initial_user = User(username='admin', password='admin123')
            db.session.add(initial_user)
            db.session.commit()
    
    return app