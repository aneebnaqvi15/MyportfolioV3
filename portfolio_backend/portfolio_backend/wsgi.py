"""
WSGI config for portfolio_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

try:
    # Explicitly set the Django settings module for production
    os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_backend.production_settings'
    logger.info(f"Using settings module: {os.environ['DJANGO_SETTINGS_MODULE']}")
    
    # Initialize WSGI application
    application = get_wsgi_application()
    logger.info("WSGI application initialized successfully")
    
except Exception as e:
    logger.error(f"Error initializing WSGI application: {str(e)}")
    raise
