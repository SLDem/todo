How to start **the todo** app:

Start Django:

`python manage.py runserver`

Run migrations:

`python manage.py makemigrations`

`python manage.py migrate`

Start celery beat and worker in seperate terminals:

`celery -A todotesttask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

`celery -A todotesttask.celery worker --loglevel=info -P eventlet`

Go to http://127.0.0.1:8000/ and register your account.

Now you can create some tasks and check the worker terminal for alerts regarding the task. The alerts will come 1 minute before the deadline and one final one will display after the time to complete the task is over.