FROM python:3.5

COPY ./service /service

WORKDIR ./service

RUN pip install -r requirements.txt

CMD ['python', './service/manage.py', 'runserver', '0.0.0.0:8000']