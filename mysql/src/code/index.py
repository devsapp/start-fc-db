# -*- coding: utf-8 -*-
import logging
import pymysql
import os
import sys

logger = logging.getLogger()


def getConnection():
    try:
        conn = pymysql.connect(
            host=os.environ['MYSQL_HOST'],       # 替换为您的HOST名称。
            port=int(os.environ['MYSQL_PORT']),  # 替换为您的端口号。
            user=os.environ['MYSQL_USER'],       # 替换为您的用户名。
            passwd=os.environ['MYSQL_PASSWORD'],  # 替换为您的用户名对应的密码。
            db=os.environ['MYSQL_DBNAME'],       # 替换为您的数据库名称。
            connect_timeout=5)
        return conn
    except Exception as e:
        logger.error(e)
        logger.error(
            "ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()


def handler(event, context):
    try:
        conn = getConnection()
        with conn.cursor() as cursor:
            sql = "REPLACE INTO users (id, name) VALUES(%s, %s)"
            cursor.execute(sql, ('2', 'wan'))
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchone()
            logger.info(result)
            return result
    finally:
        conn.close()
