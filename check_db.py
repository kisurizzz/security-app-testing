from app import create_app, db
from app.models import SearchableContent

def check_db():
    app = create_app()
    with app.app_context():
        # Query all items
        items = SearchableContent.query.all()
        print(f"Number of items in database: {len(items)}")
        print("\nFirst 5 items:")
        for item in items[:5]:
            print(f"\nTitle: {item.title}")
            print(f"Description: {item.description}")

if __name__ == '__main__':
    check_db() 