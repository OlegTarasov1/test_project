FROM python

COPY ./uptradertest /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "127.0.0.0.0:8000"]