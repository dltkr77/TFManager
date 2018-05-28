# -*- coding: utf-8 -*-


from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import tensorflow as tf


def make_lstm_cell(num_hidden, forget_bias=1.0, dropout=None):
    """
    Make LSTM cells
    :param num_hidden: The number of units int the LSTM cells.
    :param forget_bias: Biases of the forget gate
    :param dropout: Float between 0 and 1 for DropoutWrapper (output_keep_prob)
    :return: LSTM cells
    """
    if dropout and type(dropout) is float:
        # Dropout을 사용하는 경우 DropoutWrapper로 한번 감싸준다.
        cell = tf.nn.rnn_cell.LSTMCell(num_hidden,
                                       forget_bias=forget_bias,
                                       activation=tf.tanh,
                                       reuse=tf.get_variable_scope().reuse)
        return tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=dropout)

    # Dropout 미사용
    return tf.nn.rnn_cell.LSTMCell(num_hidden,
                                   forget_bias=forget_bias,
                                   activation=tf.tanh,
                                   reuse=tf.get_variable_scope().reuse)