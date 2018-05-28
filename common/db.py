# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sqlite3

from common.log import get_logger


g_databases = {}

LOG = get_logger(__name__)


def get_connection(path, timeout=0.5):
    global g_databases
    if path not in g_databases:
        conn = sqlite3.connect(path, timeout=timeout)
        g_databases[path] = conn

    return g_databases[path]


def create(conn, sql):
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except BaseException as e:
        LOG.error(str(e))
        return False
    finally:
        if cur:
            cur.close()


def select(conn, sql):
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except BaseException as e:
        LOG.error(str(e))
        return None
    finally:
        if cur:
            cur.close()


def insert(conn, sql):
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.rowcount() > 0
    except BaseException as e:
        LOG.error(str(e))
        return False
    finally:
        if cur:
            cur.close()


def update(conn, sql):
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.rowcount() > 0
    except BaseException as e:
        LOG.error(str(e))
        return False
    finally:
        if cur:
            cur.close()
