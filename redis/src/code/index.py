# -*- coding: utf-8 -*-
import os
import redis

conn_pool = None


def initializer(context):
    global conn_pool
    conn_pool = redis.ConnectionPool(
        host=os.environ['REDIS_HOST'], password=os.environ['REDIS_PASSWORD'],
        port=os.environ['REDIS_PORT'], db=1, decode_responses=True)


def handler(event, context):
    global conn_pool
    r = redis.Redis(connection_pool=conn_pool)

    counter = r.get('counter')

    if counter is None:
        counter = 0
    else:
        counter = int(counter)

    print('counter: ' + str(counter))

    r.set('counter', str(counter + 1))
    return counter
