# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import unittest
import os
import sys


class DBTest(unittest.TestCase):
    def setUp(self):
        cur_dir = os.path.dirname(os.path.relpath(__file__))
        sys.path.insert(0, os.path.join(cur_dir, '../'))
        from common.db import get_connection
        self.conn = get_connection('../test.db')

    def tearDown(self):
        self.conn.close()

    def test_create(self):
        from common.db import create
        sql = """
          CREATE TABLE IF NOT EXISTS test (
          id integer primary key,
          contents text
        )"""
        self.assertTrue(create(self.conn, sql))