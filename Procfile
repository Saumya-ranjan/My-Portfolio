web: gunicorn myportfolio.wsgi --log-file - --log-level debug
heroku ps:scale web=1
python manage.py collectstatic --noinput
python manage.py migrate