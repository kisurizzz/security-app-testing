# run.py
import os
import sys
from app import create_app

# Set the Python interpreter path explicitly
os.environ['PYTHON'] = sys.executable

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)