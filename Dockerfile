FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install -v --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]