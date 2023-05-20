FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python","./stda/manage.py", "runserver"]
