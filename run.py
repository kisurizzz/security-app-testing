# run.py
import os
import sys
from app import create_app

# Set the Python interpreter path explicitly
os.environ['PYTHON'] = sys.executable

app = create_app()

if __name__ == '__main__':
    # Get host and port from environment variables, with defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')  # Bind to all interfaces by default
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # For DAST scanning, we want to disable some security features
    if os.getenv('DAST_SCAN', 'False').lower() == 'true':
        app.config['WTF_CSRF_ENABLED'] = False
        # Disable strict security headers for scanning
        app.config['TALISMAN_FORCE_HTTPS'] = False
        app.config['TALISMAN_STRICT_TRANSPORT_SECURITY'] = False
        app.config['TALISMAN_SESSION_COOKIE_SECURE'] = False
    
    app.run(host=host, port=port, debug=debug, use_reloader=False)