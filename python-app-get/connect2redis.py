import sys
from redis.sentinel import Sentinel
import redis
#sentinel = Sentinel([('node01', 16379),('node02',16379),('node03',16379)],password='F9HaeCD6df24nLpn',socket_timeout=0.5)
sentinel = Sentinel([('redis-sentinel', 26379)],password='laSQL2019',socket_timeout=0.5)
host, port = sentinel.discover_master('master-node')
redis_client = redis.StrictRedis(host=host,port=port,password='laSQL2019')
value=redis_client.get(sys.argv[1])
print(value)

