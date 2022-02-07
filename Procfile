web: gunicorn backend.backend.wsgi --log-file -
heroku ps:scale web=1 
heroku run python manage.py migrate
heroku config:set DISABLE_COLLECTSTATIC=1
