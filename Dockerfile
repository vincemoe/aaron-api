FROM python:3

RUN pip install flask-restful

COPY . /app

CMD ["python3", "./app/app.py"]