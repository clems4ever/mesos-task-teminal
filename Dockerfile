FROM python:3.6.3

WORKDIR /app

ADD requirements.yml requirements.yml
RUN pip install -r requirements.yml
ADD scripts/entrypoint.sh /entrypoint.sh

ADD src src

ENTRYPOINT ["/entrypoint.sh"]
