# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import argparse

import requests

from common.cli import cmd
from common.config import *


list_model_parser = argparse.ArgumentParser()
list_model_parser.add_argument('--limit', default=100, type=int, help='limit of rows')
@cmd(list_model_parser)
def list(args):
    """list models"""
    config = get_config()
    limit = args.limit

    host = config[AGENT_SERVER_HOST]
    port = config[AGENT_SERVER_PORT]
    url = 'http://{}:{}/v1/model?limit={}'.format(host, port, limit)

    response = requests.get(url)
    print(response.status_code, response.text, response.elapsed)


add_model_parser = argparse.ArgumentParser()
add_model_parser.add_argument('name', type=str, help='name of model')
add_model_parser.add_argument('model', type=str, help='class of model')