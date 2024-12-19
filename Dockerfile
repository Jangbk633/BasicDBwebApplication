FROM python:3.12

WORKDIR /app

COPY ./app /app
COPY requirments.txt /app/requirments.txt
COPY wait-for-it.sh /app/wait-for-it.sh

RUN pip install --no-cache-dir -r /app/requirments.txt

CMD ["python", "server.py"]