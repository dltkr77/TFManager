# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import unittest
import os
import sys


class FactoryTest(unittest.TestCase):
    def setUp(self):
        cur_dir = os.path.dirname(os.path.relpath(__file__))
        sys.path.insert(0, os.path.join(cur_dir, '../'))

    def tearDown(self):
        pass

    def test_create_model(self):
        from models.factory import create_model

        model = create_model('LSTMRecommender', {})
        self.assertTrue(model is not None)

        model = create_model('garbage', {})
        self.assertTrue(model is None)
