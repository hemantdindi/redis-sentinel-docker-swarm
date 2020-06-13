docker build -t hemantdindi/redis-py-set .
docker  push hemantdindi/redis-py-set
docker run --network redis-nw hemantdindi/redis-py-set sampleKey sampleValue
