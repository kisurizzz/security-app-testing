# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'your-secret-key'  # Intentionally weak for demo
    
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