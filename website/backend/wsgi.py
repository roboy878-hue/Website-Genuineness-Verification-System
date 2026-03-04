"""
WSGI Entry Point for Production Deployment
This file is used by Gunicorn to start the Flask application in production
"""

import os
import sys

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app

if __name__ == "__main__":
    app.run()
