docker build -t hemantdindi/redis-py .
docker  push hemantdindi/redis-py
docker run --network redis-nw hemantdindi/redis-py
