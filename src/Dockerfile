FROM python:3.10

COPY app.py model.py sql_api.py sql_connection.py requirements.txt /app/

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
