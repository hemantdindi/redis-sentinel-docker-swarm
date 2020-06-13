docker build -t hemantdindi/redis-py-get .
docker  push hemantdindi/redis-py-get
docker run --network redis-nw hemantdindi/redis-py-get sampleKey
#docker run --network redis-nw hemantdindi/redis-py
