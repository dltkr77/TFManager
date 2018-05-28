# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import unittest
import os
import sys


class CheckTest(unittest.TestCase):
    def setUp(self):
        cur_dir = os.path.dirname(os.path.relpath(__file__))
        sys.path.insert(0, os.path.join(cur_dir, '../'))

    def tearDown(self):
        pass

    def test_check(self):
        from agent.api.v1.check import check_server
        self.assertFalse(check_server('localhost', 10101))