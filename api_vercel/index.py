import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidly.settings")

# Vercel looks specifically for a variable called 'app'
app = get_wsgi_application()
