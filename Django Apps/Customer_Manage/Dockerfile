FROM python:slim-buster
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get upgrade -y
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
RUN python manage.py migrate
# CMD [ "python manage.py runserver" ]