# -*- coding: utf-8 -*-

from .lstm import LSTMRecommender
from common.log import get_logger


__all__ = ['LSTMRecommender']

LOG = get_logger('tf-agent-server')


def create_model(model_name, config):
    try:
        return globals()[model_name](config)
    except KeyError:
        LOG.error('Not found model: {}'.format(model_name))
        return None