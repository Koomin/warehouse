from django.core.management import call_command

from config import celery_app


@celery_app.task()
def async_imports(**kwargs):
    call_command(kwargs.get('command'))
