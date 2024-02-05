Start Django:
`python manage.py runserver`

Start celery beat and worker:
# beat
`celery -A todotesttask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

# worker
`celery -A todotesttask.celery worker --loglevel=info -P eventlet`
