python ./AI-Image-classifiers-on-Django-with-RESTAPI/manage.py makemigrations
python ./AI-Image-classifiers-on-Django-with-RESTAPI/manage.py migrate
python ./AI-Image-classifiers-on-Django-with-RESTAPI/manage.py collectstatic --no-input
python ./AI-Image-classifiers-on-Django-with-RESTAPI/manage.py runserver 0.0.0.0:8000
