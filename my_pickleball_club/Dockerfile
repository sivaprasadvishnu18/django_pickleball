FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /auth_code
WORKDIR /auth_code
COPY . /auth_code/
RUN pip install --no-cache-dir -r requirements.txt
COPY .env /auth_code/.env