# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


MANAGER_SERVER_HOST = 'manager_server_host'
MANAGER_SERVER_PORT = 'manager_server_port'
MANAGER_DB_PATH = 'manager_db_path'
AGENT_SERVER_HOST = 'agent_server_host'
AGENT_SERVER_PORT = 'agent_server_port'
AGENT_DB_PATH = 'agent_db_path'
DEBUG = 'debug'
LOG_CONFIG = 'log_config'


DEFAULT_CONFIG = {
    MANAGER_SERVER_HOST: 'localhost',
    MANAGER_SERVER_PORT: 9091,
    MANAGER_DB_PATH: '../manager.db',
    AGENT_SERVER_HOST: 'localhost',
    AGENT_SERVER_PORT: 9092,
    AGENT_DB_PATH: '../agent.db',
    LOG_CONFIG: '../etc/log_config.json',
    DEBUG: True,
}

g_config = DEFAULT_CONFIG


def get_config():
    global g_config
    return g_config


def set_config(key, value):
    global g_config
    g_config[key] = value