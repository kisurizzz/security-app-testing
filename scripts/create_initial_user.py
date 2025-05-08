# scripts/create_initial_user.py
from app import create_app, db
from app.models import User

def create_initial_user():
    app = create_app()
    with app.app_context():
        if not User.query.first():
            initial_user = User(username='admin', password='admin123')
            db.session.add(initial_user)
            db.session.commit()
            print("Initial user created successfully!")
        else:
            print("Initial user already exists!")

if __name__ == '__main__':
    create_initial_user()