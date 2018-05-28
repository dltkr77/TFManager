# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import tensorflow as tf

from common.utils import make_lstm_cell
from . import Model


class LSTMRecommender(Model):
    """
    LSTM for recommendation system
    """
    def __init__(self, config):
        super().__init__(config)

    def build_graph(self, input_tensor, label_tensor, concat_tensor=None):
        """
        init lstm recommender
        :param input_tensor: input tensor(x)
        :param label_tensor: label tensor(y)
        :param config: configuration(dict)
        :param concat_tensor: add optional inputs without sequence
            input_tensor [x_0, x_1, ,,, x_seq]
                -> dynamic_rnn
                -> cancat with concat_tensor
                -> layers
                -> output
        """
        forget_bias = self.config.get('forget_bias', 1.0)
        dropout = self.config.get('dropout', None)
        hiddens = self.config.get('hiddens', [16])
        k = self.config.get('k', 50)
        bidirectional = self.config.get('bidirectional', False)

        # requirement configuration for softmax
        if 'num_classes' not in self.config:
            raise Exception('not found `num_classes` key')
        num_classes = self.config['num_classes']

        with tf.name_scope('injection'):
            self.input_tensor = input_tensor
            self.label_tensor = label_tensor

        with tf.variable_scope('layers'):
            self.cells = tf.nn.rnn_cell.MultiRNNCell(
                [make_lstm_cell(h, forget_bias=forget_bias,
                                dropout=dropout) for h in hiddens])

            if bidirectional:
                self.backward_cells = tf.nn.rnn_cell.MultiRNNCell(
                    [make_lstm_cell(h, forget_bias=forget_bias,
                                    dropout=dropout) for h in hiddens])

                self.output, _ = tf.nn.bidirectional_dynamic_rnn(self.cells,
                                                              self.backward_cells,
                                                              self.input_tensor,
                                                              dtype=tf.float64)
            else:
                self.output, _ = tf.nn.dynamic_rnn(self.cells, self.input_tensor, dtype=tf.float64)

            try:
                dim = sum([int(x.shape[-2] * x.shape[-1]) for x in self.output])
            except TypeError:
                dim = int(self.output.shape[-2] * self.output.shape[-1])
            self.flatten = tf.reshape(self.output, [-1, dim])

            if concat_tensor is not None:
                self.flatten = tf.concat([self.flatten, concat_tensor], 1)

            self.logits = tf.layers.dense(self.flatten, num_classes,
                                          reuse=tf.get_variable_scope().reuse)
            self.softmax = tf.nn.softmax(self.logits)

        with tf.name_scope('loss'):
            self.cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.label_tensor,
                                                                                logits=self.logits)
            self.loss = tf.reduce_mean(self.cross_entropy)

        with tf.name_scope('infer'):
            self.argmax = tf.argmax(self.softmax, 1)
            self.corrects = tf.equal(self.argmax, self.label_tensor)
            self.accuracy = tf.reduce_mean(tf.cast(self.corrects, tf.float32))
            self.top_k = tf.nn.top_k(tf.cast(self.softmax, tf.float32), k=k)