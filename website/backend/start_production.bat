@echo off
REM Production Startup Script for Website Genuineness Verification System
REM This script starts the application with Gunicorn in production mode

echo.
echo ===================================================================
echo  Website Genuineness Verification System - Production Start
echo ===================================================================
echo.

REM Check if we're in the backend directory
if not exist wsgi.py (
    cd backend
)

REM Start Gunicorn server
echo Starting server with Gunicorn...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8001
echo.

gunicorn --bind 0.0.0.0:8000 --workers 4 --threads 2 --worker-class gthread --timeout 120 --access-logfile logs/access.log --error-logfile logs/error.log wsgi:app

pause
