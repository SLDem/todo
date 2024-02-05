How to start the **ToDo** app:

1. Clone the Repo:

`git clone https://github.com/SLDem/todo`

2. Start Django:

`python manage.py runserver`

3. Run migrations:

`python manage.py makemigrations`

`python manage.py migrate`

4. Start celery beat and worker in seperate terminals:

`celery -A todotesttask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

`celery -A todotesttask.celery worker --loglevel=info -P eventlet`

5. Go to http://127.0.0.1:8000/ and register your account.

Now you can create some tasks and check the worker terminal for alerts regarding the task. The alerts will come 1 minute before the deadline and one final one will display after the time to complete the task is over.