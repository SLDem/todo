import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todotesttask.settings')


app = Celery('todotesttask')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-10-seconds': ({
        'task': 'notify',
        'schedule': 10.0,
        # 'args': (16, 16)
    },
    {
        'task': 'alert',
        'schedule': 10.0
    })
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('world') every 10 seconds
    sender.add_periodic_task(10.0, notify.s(), expires=10)
    sender.add_periodic_task(10.0, alert.s(), expires=10)


@app.task
def notify():
    from todo.models import Item
    import datetime
    items = Item.objects.all()
    for i in items:
        if i.finish_by.replace(tzinfo=None) - datetime.datetime.now() <= datetime.timedelta(minutes=1):
            print('Upcoming event!')


@app.task
def alert():
    from todo.models import Item
    import datetime
    items = Item.objects.all()
    for i in items:
        if i.finish_by.replace(tzinfo=None) < datetime.datetime.now():
            i.is_completed = True
            i.save()
            print('Event now!')
