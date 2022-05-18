
FROM python:3.8-slim

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/

EXPOSE 80

ENTRYPOINT ["python", "app.py"]