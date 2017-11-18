FROM python:3.6.3

WORKDIR /app

ADD requirements.yml requirements.yml
RUN pip install -r requirements.yml

ADD src src


CMD ["python", "src/app.py"]
