# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import sys
import unittest


class LogTest(unittest.TestCase):
    def setUp(self):
        cur_dir = os.path.dirname(os.path.relpath(__file__))
        sys.path.insert(0, os.path.join(cur_dir, '../'))
        import common.log as log
        self.log_config = log.DEFAULT_LOG_CONFIG
        self.log_path = '../logs/test.log'

    def tearDown(self):
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def test_default(self):
        import common.log as log
        self.assertTrue(log.LOG_DIR in self.log_config,
                        msg='default config is not exist: {}'.format(log.LOG_DIR))
        self.assertTrue(log.LOG_LEVEL in self.log_config,
                        msg='default config is not exist: {}'.format(log.LOG_LEVEL))
        self.assertTrue(log.LOG_FORMAT in self.log_config,
                        msg='default config is not exist: {}'.format(log.LOG_FORMAT))
        self.assertTrue(log.LOG_HANDLER in self.log_config,
                        msg='default config is not exist: {}'.format(log.LOG_HANDLER))

        handler_key = self.log_config[log.LOG_HANDLER]
        handler = self.log_config[handler_key]
        self.assertTrue(log.MODE in handler,
                        msg='default config is not exist: {}'.format(log.MODE))
        self.assertTrue(log.MAX_BYTES in handler,
                        msg='default config is not exist: {}'.format(log.MAX_BYTES))
        self.assertTrue(log.BACKUP_COUNT in handler,
                        msg='default config is not exist: {}'.format(log.BACKUP_COUNT))
        self.assertTrue(log.ENCODING in handler,
                        msg='default config is not exist: {}'.format(log.ENCODING))
        self.assertTrue(log.DELAY in handler,
                        msg='default config is not exist: {}'.format(log.DELAY))

    def test_log(self):
        import common.log as log
        logger = log.get_logger('test')
        logger.info('TEST!!!')
        with open(self.log_path, 'r') as fd:
            self.assertTrue(len(fd.read()) > 1)