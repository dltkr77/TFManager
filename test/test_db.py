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
        from common.db import close_connection
        close_connection('../test.db')

    def test_create(self):
        from common.db import create
        sql = """
          CREATE TABLE IF NOT EXISTS test (
            id integer primary key,
            contents text
        )"""
        self.assertTrue(create(self.conn, sql))

    def test_insert(self):
        from common.db import insert
        sql = """
          INSERT INTO test VALUES(
            0,
            'test_text'
          )"""
        self.assertTrue(insert(self.conn, sql))

    def test_update(self):
        from common.db import update
        sql = """UPDATE test SET contents='test_text2' WHERE id=0"""
        self.assertTrue(update(self.conn, sql))

    def test_delete(self):
        from common.db import delete
        sql = """DELETE FROM test"""
        self.assertTrue(delete(self.conn, sql))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DBTest('test_create'))
    suite.addTest(DBTest('test_insert'))
    suite.addTest(DBTest('test_update'))
    suite.addTest(DBTest('test_delete'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())