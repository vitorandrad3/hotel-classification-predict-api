FROM python:3.11.4

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--port=80" ]
