# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from . import *
from common.config import *
from agent.api.v1.check import check_server


@app.route('/v1/check', methods=['GET'])
def check():
    config = get_config()
    req = flask.request.values

    if req['server'] == 'agent':
        host = config[AGENT_SERVER_HOST]
        port = config[AGENT_SERVER_PORT]
    elif req['server'] == 'manager':
        host = config[MANAGER_SERVER_HOST]
        port = config[MANAGER_SERVER_PORT]
    else:
        return flask.Response(response='Not implemented server type: {}'.format(req['server']), status=404)

    status = check_server(host, port)
    response = {
        req['server']: {
            'host': host,
            'port': port,
            'status': status
        }
    }

    return flask.jsonify(response)