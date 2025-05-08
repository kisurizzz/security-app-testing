from app import create_app, db
from sqlalchemy import inspect

def check_tables():
    app = create_app()
    with app.app_context():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print("Available tables:", tables)
        
        for table in tables:
            print(f"\nTable: {table}")
            columns = inspector.get_columns(table)
            for column in columns:
                print(f"Column: {column['name']}, Type: {column['type']}")

if __name__ == '__main__':
    check_tables() 