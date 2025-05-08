from app import create_app, db
from app.models import User

def add_user():
    app = create_app()
    with app.app_context():
        # Check if user already exists
        if not User.query.filter_by(username='secret').first():
            # Create new user
            new_user = User(username='secret', password='shoebaru')
            db.session.add(new_user)
            db.session.commit()
            print("User 'secret' added successfully!")
        else:
            print("User 'secret' already exists!")

if __name__ == '__main__':
    add_user() 