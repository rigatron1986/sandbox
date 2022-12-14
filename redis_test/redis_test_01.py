import redis
import time

r = redis.Redis(host='192.168.1.171', port=6379, db=1)

# Establish a connection to the Redis database 1 at
# redis_test://localhost:6379

# SET hello world
r.set('hello', 'world')  # True
r.set('v001', 'contains cache for version 01')  # True
r.set('asset_version', 'contains cache for asset version')  # True
# GET hello
world = r.get('hello')
print(world.decode())  # "world"
# SET bye "In 60 seconds, I'll self-delete" EX 60
r.set('bye', "In 60 seconds, I'll self-delete", ex=60)  # True
expiring_message = r.get('bye')
print(expiring_message.decode())  # "In 60 seconds, I'll self-delete"
# Wait 60 seconds
# time.sleep(30)
# GET bye
# expired_message = r.get('bye')
# print(expired_message.decode())  # "None"
# DEL hello
# r.delete('hello')
# print(r.get('hello').decode())  # "None"
