FROM python:3.9.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN /usr/local/bin/python -m pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
