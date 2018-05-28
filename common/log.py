# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import json
import logging

from logging import handlers

from .config import *

#TODO: deprecate this code, use logging.config.fileConfig

# keys
LOG_DIR = 'log_dir'
LOG_LEVEL = 'log_level'
LOG_FORMAT = 'log_format'
LOG_HANDLER = 'log_handler'
MODE = 'mode'
MAX_BYTES = 'max_bytes'
BACKUP_COUNT = 'backup_count'
ENCODING = 'encoding'
DELAY = 'delay'

# defaults
with open(get_config()[LOG_CONFIG], 'r') as fd:
    DEFAULT_LOG_CONFIG = json.load(fd)

DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_LOG_FORMATTER = '%(asctime)s %(levelname)s %(filename)s(%(process)s) %(module)s[%(funcName)s:%(lineno)s] %(msg)s'
DEFAULT_LOG_HANDLER = 'RotatingHandler'


logging.basicConfig(
    level=DEFAULT_LOG_LEVEL,
    format=DEFAULT_LOG_CONFIG[LOG_FORMAT]
)
logging.getLogger()

# global variables
g_loggers = {}


def get_rotating_handler(path,
                         level=DEFAULT_LOG_LEVEL,
                         formatter=DEFAULT_LOG_FORMATTER,
                         mode=None,
                         max_bytes=None,
                         backup_count=0,
                         encoding=None,
                         delay=None):
    handler_config = DEFAULT_LOG_CONFIG[DEFAULT_LOG_HANDLER]

    mode = mode if mode else handler_config[MODE]
    max_bytes = max_bytes if max_bytes else handler_config[MAX_BYTES]
    backup_count = backup_count if backup_count else handler_config[BACKUP_COUNT]
    encoding = encoding if encoding else handler_config[ENCODING]
    delay = delay if delay else handler_config[DELAY]

    log_dir = os.path.dirname(path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    handler = handlers.RotatingFileHandler(path,
                                           mode=mode,
                                           maxBytes=max_bytes,
                                           backupCount=backup_count,
                                           encoding=encoding,
                                           delay=delay)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(formatter))

    return handler


def get_logger(name, level='INFO', propagate=False):
    global g_loggers
    if name not in g_loggers:
        log_dir = DEFAULT_LOG_CONFIG[LOG_DIR]
        logger = logging.getLogger(name)
        logger.propagate = propagate
        handler = get_rotating_handler(os.path.join(log_dir, name + '.log'))
        logger.addHandler(handler)
        logger.setLevel(level)
        g_loggers[name] = logger

    return g_loggers[name]