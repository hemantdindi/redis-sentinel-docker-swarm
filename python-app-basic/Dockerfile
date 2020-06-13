FROM python:alpine3.7
RUN pip install redis
RUN mkdir /app
COPY connect2redis.py /app
WORKDIR /app
CMD python ./connect2redis.py
