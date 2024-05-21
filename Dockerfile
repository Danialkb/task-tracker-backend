FROM python:3.11.4

WORKDIR /task_tracker

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install uv

RUN uv pip install -r requirements.txt
