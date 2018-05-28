# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import flask
from flask_cors import CORS

from common.log import get_logger


__all__ = ['flask', 'app']


# logging integration을 위해 root logger에 handler를 추가한다.
app = flask.Flask('tf-agent-server')
logger = get_logger('tf-agent-server')
[app.logger.root.addHandler(handler) for handler in logger.handlers]
CORS(app)


__SERVICES__ = ['check', 'train']
for service in __SERVICES__:
    __import__('agent.server.' + service)