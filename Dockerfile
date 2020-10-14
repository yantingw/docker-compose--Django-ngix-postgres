# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY ./AI-Image-classifiers-on-Django-with-RESTAPI/requirements.txt /opt/services/djangoapp/src/
# RUN  pip install -r /opt/services/djangoapp/src/requirements.txt
RUN  pip install  --no-cache-dir -r /opt/services/djangoapp/src/requirements.txt



# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["sh", "/opt/services/djangoapp/src/start.sh"]
CMD ["gunicorn", "--chdir", "AI-Image-classifiers-on-Django-with-RESTAPI", "--bind", ":8000", "AI.wsgi:application"]
