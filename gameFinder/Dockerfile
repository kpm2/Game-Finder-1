FROM python:3.10
EXPOSE 8000

WORKDIR /app
COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
