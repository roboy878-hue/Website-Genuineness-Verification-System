"""
Production Configuration for Website Genuineness Verification System

Use this file to override settings for production environment
"""

import os
from datetime import timedelta

class Config:
    """Base configuration"""
    # Flask Settings
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///verification.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Security
    MAX_CONTENT_LENGTH = 1024 * 1024  # 1MB max request size
    JSON_SORT_KEYS = False
    
    # API Settings
    API_TIMEOUT = 30  # seconds
    MAX_WORKERS = int(os.getenv('WORKERS', 4))
    THREADS_PER_WORKER = int(os.getenv('THREADS', 2))
    
    # Logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/verification.log'
    LOG_MAX_BYTES = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT = 10


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    FLASK_ENV = 'development'
    SESSION_COOKIE_SECURE = False
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True


# Select configuration based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

selected_config = config.get(os.getenv('FLASK_ENV', 'development'))
