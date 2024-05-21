FROM python:3.11.8

WORKDIR /task_tracker

COPY ../requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ../start.fastapi.sh /start.fastapi.sh
RUN chmod +x /start.fastapi.sh

COPY . ./
