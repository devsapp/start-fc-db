# -*- coding: utf-8 -*-
import logging
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

logger = logging.getLogger()


def handler(event, context):
    logger.info("start to test Lindorm ")
    addr_str = os.environ['DATABASE_ADDR']
    cluster = Cluster(
        # 配置连接地址。
        contact_points=addr_str.split(","),
        # 配置用户名和密码。
        auth_provider=PlainTextAuthProvider(os.environ['USER'], os.environ['PASSWORD']))
    session = cluster.connect()
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS testKeyspace WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};")
    session.execute(
        "CREATE TABLE IF NOT EXISTS testKeyspace.testTable (id int PRIMARY KEY, name text,age int,address text);")
    session.execute(
        "INSERT INTO testKeyspace.testTable (id, name, age, address) VALUES ( 1, 'testname', 11, 'hangzhou');")
    rows = session.execute("SELECT * FROM testKeyspace.testTable ;")
    for row in rows:
        logger.info("# row: {}".format(row))

    session.shutdown()
    cluster.shutdown()
