from redis.sentinel import Sentinel
import redis
#sentinel = Sentinel([('node01', 26379),('node02',26379),('node03',26379)],password='laSQL2019',socket_timeout=0.5)
sentinel = Sentinel([('redis-sentinel', 26379)],password='laSQL2019',socket_timeout=0.5)
host, port = sentinel.discover_master('master-node')
print(host)
print(port)
redis_client = redis.StrictRedis(host=host,port=port,password='laSQL2019')
redis_client.set('harbor', 'docker-registry')
value=redis_client.get('harbor')
print(value)
