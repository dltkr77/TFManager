# -*- coding: utf-8 -*-


class Model(object):
    def __init__(self, config):
        self.config = config

    def build_graph(self, input_tensor, label_tensor, **kwargs):
        raise NotImplementedError('must to implement build_graph')