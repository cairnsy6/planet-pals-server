web: gunicorn backend.backend.wsgi
heroku ps:scale web=1 
heroku config:set DISABLE_COLLECTSTATIC=1
heroku run python manage.py migrate

