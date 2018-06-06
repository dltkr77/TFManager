# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from common.db import *
from common.config import *


def select_model(limit=100):
    config = get_config()
    db_path = config[AGENT_DB_PATH]
    sql = (
        "SELECT "
        "id, model_name, model_class, model_config, model_path ",
        "FROM ",
        "tbl_model ",
        "LIMIT {}".format(limit)
    )

    conn = get_connection(db_path)
    return select(conn, sql)


def insert_model(name, class_name, config_str, path):
    config = get_config()
    db_path = config[AGENT_DB_PATH]
    sql = (
        "INSERT INTO ",
        "tbl_model(mode_name, model_class, model_config, model_path) ",
        "VALUES ({}, {}, {}, {})".format(name, class_name, config_str, path)
    )

    conn = get_connection(db_path)
    return insert(conn, sql)