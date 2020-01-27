FROM python:3.8-slim

COPY regex-check.py regex-check.py

CMD [ "python", "./regex-check.py" ]
