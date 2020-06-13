FROM python:alpine3.7
RUN pip install redis
RUN mkdir /app
COPY connect2redis.py /app
WORKDIR /app
ENTRYPOINT ["python","/app/connect2redis.py"]
