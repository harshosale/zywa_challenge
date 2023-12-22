FROM python:3.9.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/zywa_challenge

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/zywa_challenge/App