# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import json

from . import *
from agent.api.v1.model import *


@app.route('/v1/model', methods=['GET'])
def list():
    req = flask.request.values
    models = select_model(limit=req['limit'])

    if models is None:
        return flask.Response(response='Not found model table', status=404)

    response = {
        'models': models
    }
    return flask.jsonify(response)


@app.route('/v1/model', methods=['POST'])
def make():
    args = json.loads(flask.request.data)
    requirements = ['model_name', 'model_class', 'config', 'model_path']
    for req in requirements:
        if req not in args:
            return flask.Response(response='Require keys: {}'.format(', '.join(requirements)), status=400)

    return flask.jsonify(args)