FROM python:3.12

WORKDIR /code

COPY ./requirments.txt /code/requirments.txt

RUN pip install --no-cache-dir -r /code/requirments.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]