
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nimble.settings')

app = Celery('nimble', broker=os.getenv('REDIS_URL'))

app.autodiscover_tasks()
