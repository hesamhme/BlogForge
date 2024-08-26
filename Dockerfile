FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app
COPY requirements.txt /app



RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./core /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

