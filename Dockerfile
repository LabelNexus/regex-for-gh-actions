FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

COPY regex-check.py /app/regex-check.py

CMD [ "python", "/app/regex-check.py" ]
