# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import unittest
import os
import sys

import tensorflow as tf


class LSTMTest(unittest.TestCase):
    def setUp(self):
        cur_dir = os.path.dirname(os.path.relpath(__file__))
        sys.path.insert(0, os.path.join(cur_dir, '../'))

        self.config = {
            'num_classes': 10,
            'bidirectional': True,
            'k': 5,
            'hiddens': [16]
        }
        self.input_tensor = tf.placeholder(tf.float64, [None, 4, 1])
        self.label_tensor = tf.placeholder(tf.int64, [None])

    def tearDown(self):
        tf.reset_default_graph()

    def _train(self, bidirectional=False):
        from models.lstm import LSTMRecommender
        self.config['bidirectional'] = bidirectional
        lstm = LSTMRecommender(self.config)
        lstm.build_graph(self.input_tensor, self.label_tensor)

        with tf.name_scope('train'):
            optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
            train = optimizer.minimize(lstm.loss)

        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            nodes = [lstm.loss, lstm.accuracy, lstm.top_k, train, lstm.argmax]
            accuracy = 0
            for i in range(100):
                loss, accuracy, top_k, _, argmax = sess.run(nodes,
                                                            feed_dict={
                                                                self.input_tensor: [[[1], [2], [3], [4]],
                                                                                    [[1], [2], [3], [4]]],
                                                                self.label_tensor: [3, 2]})
        return accuracy

    def test_train_bidirectional(self):
        accuracy = self._train(bidirectional=True)
        self.assertTrue(accuracy >= 0.5, 'train fail! accuracy: {}'.format(accuracy))

    def test_train(self):
        accuracy = self._train()
        self.assertTrue(accuracy >= 0.5, 'train fail! accuracy: {}'.format(accuracy))


if __name__ == '__main__':
    unittest.main()