import sys
from redis.sentinel import Sentinel
import redis
#sentinel = Sentinel([('node01', 26379),('node02',26379),('node03',26379)],password='F9HaeCD6df24nLpn',socket_timeout=0.5)
sentinel = Sentinel([('redis-sentinel', 26379)],password='7cBEcwf6mV36Rx3S',socket_timeout=0.5)
host, port = sentinel.discover_master('redis-cache')
redis_client = redis.StrictRedis(host=host,port=port,password='7cBEcwf6mV36Rx3S')
print(sys.argv[1])
print(sys.argv[2])
redis_client.set(sys.argv[1], sys.argv[2])
