import redis

client = redis.Redis(host='127.0.0.1', port=6379)

client.set('key', 'value')
result = client.get('key')

print(result)
print(result.decode())
