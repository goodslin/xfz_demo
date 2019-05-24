from redis import Redis

cache = Redis(host='127.0.0.1', port=6379)

# cache.set('username', 'abc')

# print(cache.get('username'))

# 列表操作
# cache.lpush('languages', 'java')
# cache.lpush('languages', 'python')
# cache.lpush('languages', 'html')
# print(cache.lrange('languages', 0, -1))

# 集合操作
# cache.sadd('team', 'li')
# cache.sadd('team', 'zhang')
# cache.sadd('team', 'wang')
# print(cache.smembers('team'))

# 哈希操作
# cache.hset('website', 'baidu', 'www.baidu.com')
# cache.hset('website', 'google', 'www.google.com')
# cache.hset('website', 'yahoo', 'www.yahoo.com')
# print(cache.hgetall('website'))

# 事务操作
# pip = cache.pipeline()
# pip.set('username', 'goodslin')
# pip.set('password', '111111')
# pip.execute()


# 发布与订阅功能
# 异步发送邮件的功能
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        print(item)
