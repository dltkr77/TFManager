# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import argparse

import requests

from common.cli import cmd
from common.config import *


check_agent_parser = argparse.ArgumentParser()
@cmd(check_agent_parser)
def agent(args):
    """check agent server"""
    config = get_config()
    host = config[AGENT_SERVER_HOST]
    port = config[AGENT_SERVER_PORT]
    url = 'http://{}:{}/v1/check?server=agent'.format(host, port)

    try:
        response = requests.get(url)
        print(response.status_code, response.json(), response.elapsed)
    except requests.exceptions.ConnectionError:
        print('Agent is not running')


check_manager_parser = argparse.ArgumentParser()
@cmd(check_manager_parser)
def manager(args):
    """check manager server"""
    config = get_config()
    host = config[MANAGER_SERVER_HOST]
    port = config[MANAGER_SERVER_PORT]
    url = 'http://{}:{}/v1/check?server=manager'.format(host, port)

    try:
        response = requests.get(url)
        print(response.status_code, response.json(), response.elapsed)
    except requests.exceptions.ConnectionError:
        print('Manager is not running')