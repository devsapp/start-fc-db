# -*- coding: utf-8 -*-
import logging
import pymssql
import os

logger = logging.getLogger()


def getConnection():
    try:
        conn = pymssql.connect(
            host=os.environ['MSSQL_SERVER'],
            port=int(os.environ['MSSQL_PORT']),
            user=os.environ['MSSQL_USER'],
            password=os.environ['MSSQL_PASSWORD'],
            database=os.environ['MSSQL_DATABASE'],
            charset='utf8')
        return conn
    except Exception as e:
        logger.error(e)
        logger.error(
            "ERROR: Unexpected error: Could not connect to SQL Server instance.")
        raise Exception(str(e))


def handler(event, context):
    conn = getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchone()
            logger.info(result)
            return result
    finally:
        conn.close()
