from redis.sentinel import Sentinel
import redis
#sentinel = Sentinel([('node01', 26379),('node02',26379),('node03',26379)],password='F9HaeCD6df24nLpn',socket_timeout=0.5)
sentinel = Sentinel([('redis-sentinel', 26379)],password='7cBEcwf6mV36Rx3S',socket_timeout=0.5)
host, port = sentinel.discover_master('redis-cache')
print(host)
print(port)
redis_client = redis.StrictRedis(host=host,port=port,password='7cBEcwf6mV36Rx3S')
redis_client.set('key', 'value')
value=redis_client.get('key')
print(value)
